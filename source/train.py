#!/usr/bin/env python
# coding: utf-8

# # Define Imports
#%%
import json
import os
import tensorflow as tf
import numpy as np
import h5py
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.layers import GlobalAveragePooling2D
import argparse


# # Change dir in jupyter notebook

# # Define Argparser
#%%
print()
print('Tensorflow runs on the GPU: ', tf.config.list_physical_devices('GPU'))
print()
parser = argparse.ArgumentParser();

#%%
# define the training
parser.add_argument('-lr', '--learning-rate', type=float, help='', default=0.0001)
parser.add_argument('-b','--batch-size', type=int, help='', default=64)
parser.add_argument('--num-of-epochs', type=int, help='', default=1000);

#%%
# define the model structure
parser.add_argument('--activation-function', type=str, help='', default='relu')
parser.add_argument('--kernel-width', type=int, help='', default=3)
parser.add_argument('--average-kernels', type=int, help='', default=32)
parser.add_argument('--num-of-conv-layers', type=int, help='', default=5)
parser.add_argument('--kernel-increasing-factor', type=float, help='', default=1.2)
parser.add_argument('--maxpool-after-n-layer', type=int, help='', default=0)
parser.add_argument('--dropout-factor-after-conv', type=float, help='', default=0.1)
parser.add_argument('--dropout-factor-after-maxp', type=float, help='', default=0.25);

#%%
args = parser.parse_args()


# # Define the model
#%%
# define the model
padding = 'same'

#%%
kernel2d = (args.kernel_width, args.kernel_width)

#%%
model = Sequential()
for i in range(args.num_of_conv_layers):
    kernels = args.average_kernels * (args.kernel_increasing_factor ** (i-(args.num_of_conv_layers/2.)))
    kernels = int(kernels+0.5)
    
    if i == 0:
        input_shape = list([96,96,3])
        # use_cropping:
        input_shape[0] -= 10
        input_shape[1] -= 10 
        
        model.add(Conv2D(kernels, kernel2d, padding=padding,
                 input_shape=input_shape))
    else:
        model.add(Conv2D(kernels, kernel2d, padding=padding))
    model.add(Activation(args.activation_function))
    if args.maxpool_after_n_layer > 0 and (i+1) % args.maxpool_after_n_layer == 0:
        model.add(MaxPooling2D(pool_size=(2, 2)))
        if args.dropout_factor_after_maxp > 0:
            model.add(Dropout(args.dropout_factor_after_maxp))
    elif args.dropout_factor_after_conv > 0:
        model.add(Dropout(args.dropout_factor_after_conv))

model.add(GlobalAveragePooling2D())
if args.dropout_factor_after_maxp > 0:
    model.add(Dropout(args.dropout_factor_after_maxp))


model.add(Flatten())
model.add(Dense(2))
model.add(Activation('softmax'))

optimizer = tf.keras.optimizers.Adam(args.learning_rate)
model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy',tf.keras.metrics.AUC()])

model.summary()


# # Define Data Loader
#%%
def next_data_pcam(x_path,y_path,bz=args.batch_size):
    x = h5py.File(x_path,'r', libver='latest',swmr=True)['x']
    y = h5py.File(y_path,'r', libver='latest', swmr=True)['y']

    datalen = len(x)
    while True:
        indizies = None
        while indizies is None or len(indizies) == bz:
            indizies = list(np.unique(sorted(np.random.randint(datalen,size=bz))))
        
        x_data = np.array(x[indizies])
        
        # normalize_input
        x_data = x_data/256.0
        
        #use_cropping
        r = np.random.randint(10)
        r2 = np.random.randint(10)
        x_data = x_data[:,r:-10+r,r2:-10+r2]
        
        # flip_input
        if np.random.randint(2) == 1:
            x_data = x_data[:,::-1]
        if np.random.randint(2) == 1:
            x_data = x_data[:,:,::-1]
        
        yield x_data, np.array([[1,0],[0,1]])[y[indizies][:,0,0,0]]


# # Train the model
#%%
tensorboard = tf.keras.callbacks.TensorBoard('tensorboard')
history = model.fit_generator(next_data_pcam(
                             'data/camelyonpatch_level_2_split_train_x.h5',
                             'data/camelyonpatch_level_2_split_train_y.h5'),
                        validation_steps=10,
                        steps_per_epoch=30,
                        epochs=args.num_of_epochs,
                        validation_data=next_data_pcam(
                             'data/camelyonpatch_level_2_split_valid_x.h5',
                             'data/camelyonpatch_level_2_split_valid_y.h5'),
                        workers=1,
                        verbose=2,
                        use_multiprocessing=False,
                        callbacks=[tensorboard])

model.save_weights('tf_model.h5')


# # Save output files
#%%
if not os.path.exists('outputs'):
    os.mkdir('outputs')

#%%
with open('outputs/all-history.json','w') as f:
    json.dump(str(history.history),f)

params = {}
for p in history.history:
    if p.find('loss') >= 0:
        params[p] = np.min(history.history[p])
    else:
        params[p] = np.max(history.history[p])
        
with open('outputs/history-summary.json','w') as f:
    json.dump(str(params),f)

#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%



