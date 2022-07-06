# DVC - Deep Learning - Tensorflow - AIOPS - CNN_VGG16

# comands -  
## Step 01: Create a New environments
```bash
conda create --prefix ./env python=3.7 -y    
```
## Step 02: Activate new environments  
```bash
conda activate ./env
```
## Step 03: DVC initialization
```bash
git init
dvc init  
```
## step 04: Create empty files and folders- 
```bash
mkdir -p src/utils config
touch src/__init__.py src/utils/__init__.py 
src/stage_01_load_save.py src/utils/all_utils.py
touch README.md, .gitignore setup.py dvc.yaml params.yaml
``` 
