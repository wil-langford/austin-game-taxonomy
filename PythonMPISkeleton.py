#!/home/wsl/virtual-python/bin/python
"""
This is a skeleton/example Python MPI program.

- Wil Langford
"""

import numpy as np
from mpi4py import MPI
import os

def debug(filename, datadir="/home/wsl/austin-game-taxonomy/data"):
    fullname = datadir + "/" + filename
    with open(fullname,"w") as f:
        f.write("blah blah blah")

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    # All shall bow before me, for I am the master node!
    print "master"
    BASEDIR = os.path.expanduser('~/austin-game-taxonomy')
    DATADIR = BASEDIR + '/data'
    MASTERFILE = DATADIR + '/master.dat'

    debug("masternode")

    size = comm.Get_size()

    with open(MASTERFILE, 'a') as f:
        f.write("I am Process ID {0}.\nMy MPI rank is {1}\n".format(os.getpid(), rank))

        for minionrank in range(1, size):
            S = np.empty([2, 2])
            S.fill(minionrank)
            R = np.zeros([2, 2])
            
            comm.Send(S, dest=minionrank, tag=minionrank)
            comm.Recv(R, source=minionrank, tag=minionrank)
            f.write("To minion {0} I sent: {1}\nMinion {0} replied with: {2}\n".format(minionrank, S[0,0], R[0,0]))

else:
    # I am a minion node!
    print "worker {0}".format(rank)

    debug("workernode{}".format(rank))

    R = np.zeros([2, 2])
    comm.Recv(R, source=0, tag=rank)
    comm.Send(-1*R, dest=0, tag=rank)
