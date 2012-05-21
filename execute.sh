#!/bin/bash
#PBS -l nodes=3
source /opt/torque/etc/openmpi-setup.sh

mpirun $HOME/bin/python $HOME/austin-game-taxonomy/PythonMPISkeleton.py

