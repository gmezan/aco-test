import numpy as np
from vmp_impl import *

NUMBER_OF_ANTS = 8
N_ITERS = 75
ALPHA = 0
BETA = 1.2
RHO = 0.03
KP_FIRST = False
PLOT = True
W1 = 1
W2 = 1
W3 = 1.5

c = [[96.0, 96.0], [32.0, 24.0], [96.0, 128.0], [8.0, 128.0], [8.0, 128.0], [24.0, 128.0], [96.0, 40.0], [24.0, 32.0], [8.0, 32.0], [24.0, 40.0], [40.0, 256.0], [24.0, 96.0]]
p = [1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 2, 1, 1, 1, 1, 1]
w = [[12.0, 10.0], [24.0, 1.0], [8.0, 32.0], [1.0, 0.5], [0.5, 2.0], [2.0, 1.0], [2.0, 64.0], [8.0, 1.0], [24.0, 8.0], [1.0, 6.0], [6.0, 1.0], [24.0, 4.0], [2.0, 12.0], [2.0, 10.0], [2.0, 4.0], [12.0, 2.0], [6.0, 2.0], [24.0, 0.5], [1.0, 64.0], [0.5, 2.0], [2.0, 0.5], [1.0, 32.0], [1.0, 2.0], [2.0, 2.0], [2.0, 24.0], [4.0, 12.0], [12.0, 24.0], [8.0, 8.0], [0.5, 8.0], [6.0, 6.0]]
oc = [[16.0, 5.0], [16.0, 5.0], [16.0, 5.0], [16.0, 5.0], [16.0, 5.0], [16.0, 5.0], [16.0, 5.0], [16.0, 5.0], [16.0, 5.0], [16.0, 5.0], [16.0, 5.0], [16.0, 5.0]]

#print(np.sum(p))
aco_for_vmp(p=p, c=c, w=w, oc=oc, n_ants=NUMBER_OF_ANTS, max_iter=N_ITERS, alpha=ALPHA, beta=BETA, rho=RHO, kp_first=KP_FIRST, plot=PLOT, w1=W1, w2=W2, w3=W3)
