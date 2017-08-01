#!/bin/bash

old_pwd=$(pwd)
cd ~/

if [[ -e y2-venv ]]; then
    source ~/y2-venv/bin/activate
    pip install -r $old_pwd/requirements.txt
else
     sudo apt-get install virtualenv
     virtualenv -p $(which python3) y2-venv
     source ~/y2-venv/bin/activate
     pip install -r $old_pwd/requirements.txt
fi
cd $old_pwd

if [ ! -f ngrok ]; then
  wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
  unzip ngrok-stable-linux-amd64.zip
fi

export FLASK_APP=app.py
export FLASK_DEBUG=1