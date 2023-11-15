import numpy as np


def get_dominant_eigenvalue_and_eigenvector(data, num_steps):
    """
    data: np.ndarray – symmetric diagonalizable real-valued matrix
    num_steps: int – number of power method steps

    Returns:
    eigenvalue: float – dominant eigenvalue estimation after `num_steps` steps
    eigenvector: np.ndarray – corresponding eigenvector estimation
    """
    ### YOUR CODE HERE
    r = [1]*data.shape[0]
    for i in range(num_steps):
        r = data.dot(r)/np.linalg.norm(data.dot(r))
    mu = float(r.T.dot(data.dot(r))/r.T.dot(r))
    return mu, r
