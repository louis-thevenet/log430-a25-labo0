#!/usr/bin/env bash

set -e
pkill -f "calculator.py" || true

cd ~
rm -rf log430-a25-labo0
git clone https://github.com/louis-thevenet/log430-a25-labo0.git
cd  log430-a25-labo0/

sudo apt -y install python3 python3-venv
python3 -m venv .venv/labo0
source .venv/labo0/bin/activate

pip install -r requirements.txt

cd src/
python3 calculator.py
