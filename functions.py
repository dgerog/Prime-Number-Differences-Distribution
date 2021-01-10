import numpy as np

def kneeThresholding(_Y):
    """
        Perform knee (or elbow) thresholding.
        
        To determine the number of clusters:
            1. Order the input.
            2. Plot the input (x-axis: input index, y-axis: input)
            3. Compute the line crosses the points marked by the first and last
                input of the previous plot.
            4. Compute the distances of all the points of the previous plot
                to the line computed in step 3.
            5. Detect the point with the largest distance (knee detection).
            6. The index of the point coresponds to expected threshold.

        _kernelCov: A string with the preprocessing on the data. None for no preprocessing.
        _oFName: The full path to save the plots. None for no ploting
                        
        RETURN: Number of clusters (estimated)
    """
    # diagonal line (equation)
    _X = range(0,_Y.shape[0])
    P1 = np.array([0         , _Y[0]])
    P2 = np.array([_X[_Y.shape[0]-1], _Y[_Y.shape[0]-1]])
        
    l = (P2[1] - P1[1])/(P2[0] - P1[0])
    b = P2[1] - l*P2[0]
        
    # find distances (Euclidean)
    d = []
    Q = np.sqrt(l*l + 1)
    for i in range(0,_Y.shape[0]):
        d.append(np.abs(l*i - _Y[i] + b)/Q)
        
    # find max
    x_max = np.argmax(d)
    P0 = [_X[x_max], _Y[x_max]] # this is the point with max distance
    
    return(P0[0]+1)