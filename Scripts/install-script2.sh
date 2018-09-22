#!/bin/bash

sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get install unzip

conda install -y numpy scipy ipython mkl jupyter seaborn
conda install -y pytorch-cpu torchvision-cpu -c pytorch

jupyter notebook --generate-config
echo "c = get_config()" >> .jupyter/jupyter_notebook_config.py 
echo "c.NotebookApp.ip = '*'" >> .jupyter/jupyter_notebook_config.py
echo "c.NotebookApp.open_browser = False" >> .jupyter/jupyter_notebook_config.py
echo "c.NotebookApp.port = 7000" >> .jupyter/jupyter_notebook_config.py
echo "c.NotebookApp.token='deeplearning'" >> .jupyter/jupyter_notebook_config.py