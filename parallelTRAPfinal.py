# The goal of this work was to first parallelize the trapezoid method code
# then run the new parallel version on Hyperion, a super computer with 4 AMD-based quad core nodes.
# Experiments were done by changing the cluster configuration then taking time measurements
# to observe how the program scales with the number of processors it can use

# A general summary of how the sequential algorithm was parallelized is that a single core
# was designated as the master or server while the rest were designated as workers.
# In this layout, the total work is divided amongst the workers who then send their
# results as messages via network links to the server. The interface used to assign
# ranks and to send/receive messages was an MPI (Message Passing Interface) from the mpi4py library.




from mpi4py import MPI
import time

SERVER = 0
TAG = 11000

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def f(x):
    return x*x

def main():
    if rank == SERVER:
        begin = time.time()
    traps = 10000000
    start, end = 0.0, 1.0
    trap_width = (end - start) / traps
    local_work = traps / (size - 1)

    local_start = start + ((local_work * trap_width) * (rank - 1))
    local_end = local_start + local_work * trap_width

    total = 0
    area = 0

    if rank == SERVER:
        for i in range(1, size):
            total += comm.recv(source = i, tag = TAG)
        finish = time.time()
        print ("Final area = %f" % total)
        print finish - begin

    else:
        while local_start < local_end:
            low_x = start + local_start
            high_x = local_start + trap_width
            low_y = f(low_x)
            high_y = f(high_x)
            area += trap_width * (low_y + high_y) * 0.5
            local_start += trap_width
        comm.send(area, dest = SERVER, tag = TAG)

for i in range(1):
    if __name__ == '__main__':
        main()