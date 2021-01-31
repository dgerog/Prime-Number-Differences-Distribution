import random
import numpy as np
import math
import matplotlib.pyplot as plt

from  functions import *

PRIMES_TO_READ = ['1','2','3','4','5'] # define the file to read to load the list with prime numbers
DATA_PATH = './data/primes%s.txt'

STORAGE_PATH = './results/E3-%s.eps'

START_NUMBER_IND = 0
END_NUMBER_IND   = 1000
MIN_CARDINALITY = 100 #-> Minimum number of concecutive primes to check

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
M = END_NUMBER_IND - START_NUMBER_IND
number_of_principal_axis = np.zeros((M,1))
preserved_variance = np.zeros((M,1))
for n in range(START_NUMBER_IND,END_NUMBER_IND):
    # keep fraction of numbers
    numbs = numbsALL[START_NUMBER_IND:n + MIN_CARDINALITY]

    print('ITERATION %5d/%5d...' % (n+1, M))

    # compute correlation
    K = len(numbs)
    s = np.zeros((K,K))
    for i in range(0,K):
        for j in range(i+1,K):
            d = numbs[i]-numbs[j]
            s[i,j] = d * d
            s[j,i] = s[i,j]

    if n == 0 or n%100 == 0:
        #show the distance matrix every 100 iterations + the first (-> make sure at least one image is produced)
        plt.imshow(s)
        plt.savefig(STORAGE_PATH%('-cov-' + str(n+1)))
        plt.close()

    # eigenvalues
    [v,e] = np.linalg.eig(s)
    vv = np.abs(v)

    # knee thresolding
    number_of_principal_axis[n] = kneeThresholding(vv)
    preserved_variance[n] = math.floor(100*np.sum(vv[:int(number_of_principal_axis[n])])/np.sum(vv))

#
# 3. plot result
#
xind = list(range(1,M+1))
fig, axs = plt.subplots(2)
fig.suptitle(('Summary of Experiments [Start:%d, End:%d, Min Cardinality:%d]')%(numbsALL[START_NUMBER_IND],numbsALL[END_NUMBER_IND], MIN_CARDINALITY))

axs[0].plot(xind, number_of_principal_axis,'-')
axs[0].set_ylabel('# of clusters')
axs[0].set_yticks([3, 4, 5])

axs[1].plot(xind,preserved_variance,'-')
axs[1].set_ylabel('% of var')
axs[1].set_xlabel('Group')

plt.savefig(STORAGE_PATH%(M))
plt.close()