import random
import numpy as np
import math
import matplotlib.pyplot as plt

from  functions import *

PRIMES_TO_READ = ['1','2','3','4','5'] # define the file to read to load the list with prime numbers
DATA_PATH = './data/primes%s.txt'

STORAGE_PATH = './results/iter-%s.eps'

ITEARATIONS = 100000
NUBERS_TO_KEEP_MIN = 100
NUBERS_TO_KEEP_MAX = 1000

#
# 1. read ALL the primes
# 
numbsALL = []
for i in range(0,len(PRIMES_TO_READ)):
    p = DATA_PATH % (PRIMES_TO_READ[i])
    n = np.genfromtxt(fname=p,skip_header=4)
    numbsALL = np.concatenate((numbsALL, np.ndarray.flatten(n)))


#
# 2. Knee thresholding
#    Repeat multiple times - Extract number of significant eigenvectors
number_of_principal_axis = np.zeros((ITEARATIONS,1))
preserved_variance = np.zeros((ITEARATIONS,1))
for iters in range(0,ITEARATIONS):
    # keep fraction of numbers
    numbs_to_keep = random.randint(NUBERS_TO_KEEP_MIN, NUBERS_TO_KEEP_MAX)
    start = random.randint(0, len(numbsALL) - numbs_to_keep)
    numbs = numbsALL[start:start + numbs_to_keep]

    print('ITERATION %5d/%5d - %4d Numbers selected (start from %7d)...' % (iters+1, ITEARATIONS, numbs_to_keep, start))

    # compute correlation
    K = len(numbs)
    s = np.zeros((K,K))
    for i in range(0,K):
        for j in range(i+1,K):
            d = numbs[i]-numbs[j]
            s[i,j] = d * d
            s[j,i] = s[i,j]

    # eigenvalues
    [v,e] = np.linalg.eig(s)
    vv = np.abs(v)

    # knee thresolding
    number_of_principal_axis[iters] = kneeThresholding(vv)
    preserved_variance[iters] = math.floor(100*np.sum(vv[:int(number_of_principal_axis[iters])])/np.sum(vv))

#
# 3. plot result
#
xind = list(range(1,ITEARATIONS+1))
fig, axs = plt.subplots(2)
fig.suptitle(('Summary of Experiments [%d ITERATIONS]')%ITEARATIONS)

axs[0].plot(xind, number_of_principal_axis,'-')
axs[0].set_ylabel('# of clusters')
axs[0].set_yticks([3, 4, 5])

axs[1].plot(xind,preserved_variance,'-')
axs[1].set_ylabel('% of var')
axs[1].set_xlabel('Iteration')

plt.savefig(STORAGE_PATH%(ITEARATIONS))
plt.close()