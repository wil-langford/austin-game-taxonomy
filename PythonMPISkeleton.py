#!/home/wsl/virtual-python/bin/python

import numpy as np
from mpi4py import MPI
import os

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    # All shall bow before me, for I am the master node!
    print "master"
    BASEDIR = os.path.expanduser('~/austin-game-taxonomy')
    DATADIR = BASEDIR + '/data'

    with open(DATADIR + "/master.dat", 'w') as f:
        f.write("my rank is {0}".format(rank))

else:
    # I am a minion node!
    print "worker {0}".format(rank)
