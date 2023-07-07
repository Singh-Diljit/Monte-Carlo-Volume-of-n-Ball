"""Estimate the volume of a unit n-ball."""

import matplotlib.pyplot as plt
import random
from typing import List #Not required for python 3.9 and above

def generate_point(dimension: int) -> List[float]:
    """Randomly generate a random point in the unit hypercube.

    A point is in the unit hypercube if each coordinate is bounded
    by -1 and 1. This function rounds to 2 decimal places.

    Parameters
    ----------
    dimension : int
        Dimension of hypercube.

    Returns
    -------
    generate_point(dimension) : List
        A list with entries bounded by -1 and 1.
    """
    return [round(random.uniform(-1, 1), 2) for _ in range(dimension)]
    
def in_ball(point: List[float]) -> bool:
    """Determine if a point is in the unit n-ball.

    A point is in the unit n-ball iff the sum of its coordinates squared
    is less than one.
    
    Parameters
    ----------
    point : List
        A list of length n, representing a point in n-space.

    Returns
    -------
    in_ball(point) : bool
        True if the point is in the ball else False.

    """
    return True if sum([x**2 for x in point]) < 1 else False

def est_vol(dim: int, sample_size: int) -> float:
    """Return the estimated volume of a n dimensional ball.

    The logic of the code is as follows:

    1. Use Monte-Carlo methods to estimate R = vol(n-ball) / vol(hypercube),
    which is denoted R_est.

    2. Because R * vol(hypercube) = vol(n-ball) we estimate 'vol(n-ball)'
    by using 'R_est' instead of 'R'. That is we compute:
        R_est * vol(hypercube) = est_vol(n-ball).

    Parameters
    ----------
    dim : int
        The dimension of the n-ball.
    sample_size : int
        Number of samples to draw.

    Returns
    -------
    est_vol(dim, sample_size) : float
        The estimated volume of the n-ball.

    """
    if dim < 2: #dim = 0 gives vol = 1 and dim = 1 gives vol = 2
        return dim + 1
    
    vol_hypercube = 2**dim #Volume of n-dimensional hypercube

    inside = 0 #Counts how many points land in the n-ball
    for _ in range(sample_size):
        inside += in_ball(generate_point(dim))
        
    #Becuase the n-ball is contained in the hypercube,
    #we can estimate the ratio of volumes, vol(n-ball) / vol(hypercube),
    #by dividing points that landed in the n-ball to points that landed
    #in the hypercube (we sample from the hypercube so this is all points).
    est_ratio = inside / sample_size 

    #The ratio of volumes multiplied by the volume of the hypercube
    #estimates the volume of the n-ball.
    return est_ratio * vol_hypercube

def plot_ball_vol(N: int, accuracy: int):
    """Plots the estimated volume of a unit n-ball for dimensions 0 to N."""

    volumes = [est_vol(dim, accuracy) for dim in range(N)]
    dimensions = [dim for dim in range(N)]
    for dim, vol in enumerate(volumes):
        print(f'The {dim}-ball has volume {vol}')
        
    #Plot data
    plt.plot(dimensions, volumes, 'ro')
    plt.xticks(dimensions)
    plt.yticks([i for i in range(10)])
    
    #Label graph and axis
    plt.title("Estimated Volume of n-Ball")
    plt.xlabel("Dimension")
    plt.ylabel("Volume")

    #Generate plot
    plt.show()
    
