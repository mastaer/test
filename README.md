# dvc-cc-sample-pcam-9.0
This is a sample project that demonstrates the usage of DVC-CC. To find out more about DVC-CC, take a look at section three of this README.

## 1. How this repository was build

1. create a new repository
2. call "dvc-cc init"
3. add source code for downloading the pcam dataset ("source/download_pcam.sh")
4. using sshfs to connect to the data storage server (`dvc-cc sshfs annusch@dt1.f4.htw-berlin.de:/mnt/md0/annusch/data_storage data`)
5. create a dvc file for downloading the file and run it (`dvc run ... sh source/download_pcam.sh`)
6. create the source code ("source/train.ipynb")
7. create a .hyperopt file (`dvc-cc hyperopt new ... 'python source/train.py ...'`)
8. commit and push to git
9. run experiments with `dvc-cc run`

For a video tutorial to curious containers 8 you can find at [https://github.com/deep-projects/dvc-cc-sample-pcam](https://github.com/deep-projects/dvc-cc-sample-pcam).

## 2. Use this repository

What you can do with this git repository depends on your rights.

1. If you have read access to this git repository, you can switch to a resulting branch, a git branch that begins with 'rcc_'. You can do this by calling 'git checkout rcc_...'. In the README.md you find all pieces of information about the docker in which the experiment ran, **and you find the ways to reproduce the experiment locally**.
2. If you have also read access to the dvc storage server, you can get all output files, including large files.
    - For this, you can switch to a resulting branch and call 'dvc pull'. You will see now all the output files for this branch.
    - You can also take a look at multiple experiments/branches. To do this, you need first to sync all git branches with "dvc-cc git sync" and then pull, for example, the tensorboard folders of the 5th to 7th experiment with the command: 'dvc-cc output-to-tmp tensorboard -p 5:7'.
3. If you have rights to the agency, you can check the status of the last experiments with "dvc-cc status".
4. If you have all read and write rights, you can run new jobs with different parameters by calling "dvc-cc run expname".

## 3. About DVC-CC

In this git repository, the software tool DVC-CC is used. This software tool makes it possible to defining experiment pipelines and runs these pipelines in a cluster. The goal of DVC-CC is to make the defined pipelines scalable, by running multiple experiments parallel in a cluster, and reproducibility, by calculating checksums for input and output files or directories.

To handle the scalability, DVC-CC uses the software Curious Containers (CC). CC allows it to start experiments in a cluster by only defining one RED file. DVC-CC creates GIT input branches that begin with "cc_". In this input branches, all hyperparameters are set and a RED file is generated. In the cluster, a DVC-CC docker image is started that downloads the source code from the GIT repository of the input branch, runs the pipeline and pushes the result to a new branch that begins with rcc_. [Here](https://www.curious-containers.cc) you can read more about Curious Containers.

To define reproducible pipelines and handle large files, DVC-CC use the Software Data Version Control (DVC). DVC outsource large output files from git to a storage server and save large files with checksums. Take a look at [this site](https://dvc.org/) to read more about DVC.

You can install the used DVC and DVC-CC version with:

```
pip install --upgrade dvc=0.88.0
pip install --upgrade dvc-cc=0.9.2
```

If you want to find out more about DVC-CC you can visit [this GitHub site](https://github.com/deep-projects/dvc-cc/tree/master/dvc-cc).

## About DVC-CC
This branch was automated created with the tool DVC-CC. This tool connects DVC (https://dvc.org/) to CC (www.curious-containers.cc) to run your defined stages with DVC in a docker on your cloud system with CC. [More information about DVC-CC](https://github.com/deep-projects/dvc-cc)

## DVC-Status


<details><summary>Before Execution</summary>
<p>

```
WARNING: Output 'tensorboard'(Stage: 'dvc/train.dvc') is missing version info. Cache for it will not be collected. Use dvc repro to get your pipeline up to date.
WARNING: Output 'tf_model.h5'(Stage: 'dvc/train.dvc') is missing version info. Cache for it will not be collected. Use dvc repro to get your pipeline up to date.
WARNING: Output 'outputs/all-history.json'(Stage: 'dvc/train.dvc') is missing version info. Cache for it will not be collected. Use dvc repro to get your pipeline up to date.
WARNING: Output 'outputs/history-summary.json'(Stage: 'dvc/train.dvc') is missing version info. Cache for it will not be collected. Use dvc repro to get your pipeline up to date.
Data and pipelines are up to date.

```

</p>
</details>




<details><summary>After Execution</summary>
<p>

```
	new:                tensorboard
	new:                tensorboard/train/events.out.tfevents.1584080903.b1a63f52ccb9.209.491.v2
	new:                tensorboard/train/events.out.tfevents.1584080904.b1a63f52ccb9.profile-empty
	new:                tensorboard/train/plugins/profile/2020-03-13_06-28-24/local.trace
	new:                tensorboard/validation/events.out.tfevents.1584080928.b1a63f52ccb9.209.2188.v2
	new:                tf_model.h5
	new:                outputs/all-history.json
	new:                outputs/history-summary.json

```

</p>
</details>



## How to rerun this experiment:
The following sections describe how you can rerun the dvc stages yourself.


<span style="color:red">Warning: During execution a folder was included via sshfs.</span>


### Pure command line (run the experiment local)
```
sh source/download_pcam.sh
python source/train.py --learning-rate 0.01 --batch-size 128 --num-of-epochs 2 --activation-function relu --kernel-width 3 --average-kernels 16 --num-of-conv-layers 2 --kernel-increasing-factor 1 --maxpool-after-n-layer 1 --dropout-factor-after-conv 0.1 --dropout-factor-after-maxp 0.1

```
### Using DVC (run the experiment local)
```
dvc repro -P
```
### Using CC (run the experiment on a server)
```
faice exec cc_execution_file.red.yml
```
## Executed System
The scipt ran on the following system:


<details><summary>GPU(s)</summary>
<p>

```
                          name    memory.total [MiB]
====================================================
           GeForce GTX 1080 Ti             11175 MiB

```

</p>
</details>




<details><summary>Other Hardware</summary>
<p>

```
H/W path            Device  Class       Description
===================================================
/0/0                        memory      62GiB System memory
/0/1                        processor   AMD Ryzen 7 1800X Eight-Core Processor

```

</p>
</details>




<details><summary>Software</summary>
<p>

```
Package              Version      
-------------------- -------------
absl-py              0.9.0        
appdirs              1.4.3        
asciimatics          1.11.0       
asn1crypto           0.24.0       
astor                0.8.1        
atpublic             1.0          
attrs                19.3.0       
backcall             0.1.0        
bcrypt               3.1.7        
bleach               3.1.0        
cachetools           4.0.0        
certifi              2019.11.28   
cffi                 1.13.2       
chardet              3.0.4        
colorama             0.4.3        
configobj            5.0.6        
configparser         4.0.2        
contextlib2          0.5.5        
cryptography         2.8          
cycler               0.10.0       
decorator            4.4.1        
defusedxml           0.6.0        
distro               1.4.0        
dvc                  0.60.1+ee976a
dvc-cc-agent         0.8.9        
dvc-cc-connector     0.8.1        
entrypoints          0.3          
flufl.lock           3.2          
funcy                1.14         
future               0.18.2       
gast                 0.2.2        
gitdb2               2.0.6        
GitPython            3.0.5        
google-auth          1.11.0       
google-auth-oauthlib 0.4.1        
google-pasta         0.1.8        
grandalf             0.6          
grpcio               1.26.0       
h5py                 2.10.0       
humanize             0.5.1        
idna                 2.6          
importlib-metadata   1.4.0        
inflect              4.0.0        
ipykernel            5.1.3        
ipython              7.11.1       
ipython-genutils     0.2.0        
ipywidgets           7.5.1        
jedi                 0.15.2       
Jinja2               2.10.3       
joblib               0.14.1       
jsonpath-ng          1.4.3        
jsonschema           3.2.0        
jupyter              1.0.0        
jupyter-client       5.3.4        
jupyter-console      6.1.0        
jupyter-core         4.6.1        
Keras-Applications   1.0.8        
Keras-Preprocessing  1.1.0        
keyring              10.6.0       
keyrings.alt         3.0          
kiwisolver           1.1.0        
Markdown             3.1.1        
MarkupSafe           1.1.1        
matplotlib           3.1.2        
mistune              0.8.4        
mock                 3.0.5        
nanotime             0.5.2        
nbconvert            5.6.1        
nbformat             5.0.4        
networkx             2.4          
notebook             6.0.3        
numpy                1.18.1       
oauthlib             3.1.0        
opt-einsum           3.1.0        
packaging            20.1         
pandas               0.25.3       
pandocfilters        1.4.2        
paramiko             2.7.1        
parso                0.5.2        
pathspec             0.7.0        
pexpect              4.8.0        
pickleshare          0.7.5        
Pillow               7.0.0        
pip                  20.0.2       
ply                  3.11         
prometheus-client    0.7.1        
prompt-toolkit       3.0.2        
protobuf             3.11.2       
ptyprocess           0.6.0        
pyasn1               0.4.8        
pyasn1-modules       0.2.8        
pycparser            2.19         
pycrypto             2.6.1        
pyfiglet             0.8.post1    
Pygments             2.5.2        
pygobject            3.26.1       
pyjson               1.3.0        
PyNaCl               1.3.0        
pyparsing            2.4.6        
pyrsistent           0.15.7       
python-dateutil      2.8.1        
pytz                 2019.3       
pyxdg                0.25         
PyYAML               5.3          
pyzmq                18.1.1       
qtconsole            4.6.0        
red-connector-ssh    1.0          
requests             2.22.0       
requests-oauthlib    1.3.0        
rsa                  4.0          
ruamel.yaml          0.16.6       
ruamel.yaml.clib     0.2.0        
schema               0.7.1        
scikit-learn         0.22.1       
scipy                1.4.1        
scp                  0.13.2       
seaborn              0.10.0       
SecretStorage        2.3.1        
Send2Trash           1.5.0        
setuptools           45.1.0       
shortuuid            0.5.0        
six                  1.14.0       
sklearn              0.0          
smmap2               2.0.5        
tensorboard          2.1.0        
tensorflow-estimator 2.1.0        
tensorflow-gpu       2.1.0        
termcolor            1.1.0        
terminado            0.8.3        
testpath             0.4.4        
torch                1.4.0        
torchvision          0.5.0        
tornado              6.0.3        
tqdm                 4.42.0       
traitlets            4.3.3        
treelib              1.5.5        
urllib3              1.25.8       
wcwidth              0.1.8        
webencodings         0.5.1        
Werkzeug             0.16.0       
wheel                0.30.0       
widgetsnbextension   3.5.1        
wrapt                1.11.2       
zipp                 2.1.0        

```

</p>
</details>


