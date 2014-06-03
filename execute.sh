#!/bin/bash
#PBS -l nodes=3
source $HOME/local/x86_64/python/venv/bin/activate
source /opt/torque/etc/openmpi-setup.sh

mpirun python $HOME/austin-game-taxonomy/PythonMPISkeleton.py
