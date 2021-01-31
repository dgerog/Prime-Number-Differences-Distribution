# Prime Number Distribution Clustering
I came up with a crazy idea... is there a pattern in the distribution of consecutive prime numbers? So I decided to conduct an experiment.  At first, a dataset with the first 5.000.000 prime numbers was loaded (see the acknowledgements for more details). Then, iteratively, subsets were created of that set, containing **consecutive** prime numbers and for this subset, computed a distance matrix `S[i,j] = (p[i] - p[j])^2` was computed, where `p[i]` and `p[j]` are the i-th and j-th prime of the subset mentioned earlier. Finally, for the distance matrix `S` the eigenvalues were computed and with a heuristic method (_knee detection_) the number of potential clusters was computed.

What is a remarkable observation is that for datasets with more than **100 consecutive** prime numbers (no matter which are this prime numbers - large or small), their differences can be grouped in 3 (in a few cases) or 4 clusters! Moreover, the related eigenvectors preserve >80% of the variance of the variables!

Files:
* _functions.py_: Utility functions I used in my experiments.
* _main.py_: The main code of the experiment.

## Acknowledgments
The list of primes I used was extracted from files downloaded from [https://primes.utm.edu/lists/small/millions/]https://primes.utm.edu/lists/small/millions/. I wish to thank Dr. [https://www.utm.edu/staff/caldwell/] Chris K. Caldwell for maintaining the repository with files with list of prime numbers.