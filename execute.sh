#!/bin/bash
#PBS -l nodes=3
source /opt/torque/etc/openmpi-setup.sh

mpirun /home/wsl/git/austin-game-taxonomy/virtual-python/bin/python /home/wsl/git/austin-game-taxonomy/game-taxonomy/python-mpi-skeleton.py

