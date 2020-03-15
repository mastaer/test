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
Data and pipelines are up to date.

```

</p>
</details>




<details><summary>After Execution</summary>
<p>

```
	new:                tensorboard
	new:                tensorboard/train/events.out.tfevents.1584258781.a088415ba33f.263.373.v2
	new:                tensorboard/train/events.out.tfevents.1584258784.a088415ba33f.profile-empty
	new:                tensorboard/train/plugins/profile/2020_03_15_07_53_04/a088415ba33f.input_pipeline.pb
	new:                tensorboard/train/plugins/profile/2020_03_15_07_53_04/a088415ba33f.overview_page.pb
	new:                tensorboard/train/plugins/profile/2020_03_15_07_53_04/a088415ba33f.tensorflow_stats.pb
	new:                tensorboard/train/plugins/profile/2020_03_15_07_53_04/a088415ba33f.trace.json.gz
	new:                tensorboard/validation/events.out.tfevents.1584258799.a088415ba33f.263.2285.v2
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
python source/train.py --learning-rate 0.0001 --batch-size 83 --num-of-epochs 3 --activation-function relu --kernel-width 3 --average-kernels 32 --num-of-conv-layers 5 --kernel-increasing-factor 1.2 --maxpool-after-n-layer 0 --dropout-factor-after-conv 0.1 --dropout-factor-after-maxp 0.25

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
H/W path              Device  Class       Description
=====================================================
/0/0                          memory      62GiB System memory
/0/1                          processor   AMD Ryzen 7 1800X Eight-Core Processor

```

</p>
</details>




<details><summary>Software</summary>
<p>

```
Package                Version        
---------------------- ---------------
absl-py                0.9.0          
appdirs                1.4.3          
asn1crypto             0.24.0         
astunparse             1.6.3          
atpublic               1.0            
attrs                  19.3.0         
bcrypt                 3.1.7          
cachetools             4.0.0          
certifi                2019.11.28     
cffi                   1.14.0         
chardet                3.0.4          
cloudpickle            1.3.0          
colorama               0.4.3          
configobj              5.0.6          
cryptography           2.8            
cycler                 0.10.0         
decorator              4.4.2          
distro                 1.4.0          
dvc                    0.88.0         
dvc-cc-agent           0.9.6          
dvc-cc-connector       0.8.1          
flatten-json           0.1.7          
flufl.lock             3.2            
funcy                  1.14           
future                 0.18.2         
gast                   0.3.3          
gitdb                  4.0.2          
GitPython              3.1.0          
google-auth            1.11.2         
google-auth-oauthlib   0.4.1          
google-pasta           0.1.8          
grandalf               0.6            
grpcio                 1.27.2         
h5py                   2.10.0         
humanize               2.0.0          
idna                   2.6            
importlib-metadata     1.5.0          
inflect                3.0.2          
joblib                 0.14.1         
jsonpath-ng            1.5.1          
jsonschema             3.2.0          
Keras-Preprocessing    1.1.0          
keyring                10.6.0         
keyrings.alt           3.0            
kiwisolver             1.1.0          
Markdown               3.2.1          
matplotlib             3.2.0          
nanotime               0.5.2          
networkx               2.3            
numpy                  1.18.1         
oauthlib               3.1.0          
opt-einsum             3.2.0          
packaging              20.3           
pandas                 1.0.1          
paramiko               2.7.1          
pathspec               0.7.0          
pexpect                4.8.0          
Pillow                 7.0.0          
pip                    20.0.2         
ply                    3.11           
protobuf               3.11.3         
ptyprocess             0.6.0          
pyasn1                 0.4.8          
pyasn1-modules         0.2.8          
pycparser              2.20           
pycrypto               2.6.1          
pydot                  1.4.1          
pygobject              3.26.1         
pygtrie                2.3.2          
pyjson                 1.3.0          
PyNaCl                 1.3.0          
pyparsing              2.4.6          
pyrsistent             0.15.7         
python-apt             1.6.5+ubuntu0.2
python-dateutil        2.8.0          
pytz                   2019.3         
pyxdg                  0.25           
PyYAML                 5.1.2          
red-connector-ssh      1.2            
requests               2.23.0         
requests-oauthlib      1.3.0          
rsa                    4.0            
ruamel.yaml            0.16.10        
ruamel.yaml.clib       0.2.0          
scikit-learn           0.22.2.post1   
scipy                  1.4.1          
scp                    0.13.2         
seaborn                0.10.0         
SecretStorage          2.3.1          
setuptools             46.0.0         
shortuuid              1.0.1          
six                    1.14.0         
sklearn                0.0            
smmap                  3.0.1          
tensorboard            2.1.1          
tensorflow-estimator   2.1.0          
tensorflow-gpu         2.2.0rc0       
tensorflow-probability 0.9.0          
termcolor              1.1.0          
texttable              1.6.2          
torch                  1.4.0          
torchvision            0.5.0          
tqdm                   4.43.0         
treelib                1.6.1          
urllib3                1.25.8         
voluptuous             0.11.7         
Werkzeug               1.0.0          
wheel                  0.30.0         
wrapt                  1.12.1         
zc.lockfile            2.0            
zipp                   3.1.0          

```

</p>
</details>


