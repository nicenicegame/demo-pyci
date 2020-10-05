def variance(data):
    """Returns the population variance of a list (array) of numbers in data.
    
    The variance is the sum of squared differences between data values
    and their mean, divided by the number of items in the list (n).
    This is different from the Python library function statistics.variance
    which returns the sample variance, where the sum is divided by (n-1).

    Example: variance([1,5]) is ((1-3)**2 + (5-3)**2)/2 = 4.

    (These are Google style comments for arguments, returns, and exceptions.)
    
    Args:
        data: list of numbers for which variance will be computed. 
           Must contain at least one element.
    Returns:
        population variance of values in data list.
    Raises:
        ValueError if the data parameter is empty.

    >>> variance([1])
    0.0
    >>> variance([1, 1, 1, 1])
    0.0
    >>> variance([1, 2])
    0.25
    >>> variance([1000000, 1000004])
    4.0
    """
    # some deliberately misformatted code. Use flake8 to fix.
    n=len(data)  
    if n==0:
        raise TypeError( )
    average = sum(data)/n
    return sum( [(x-average)**2 for x in data] )/n

def stdev(data):
    """The population standard deviation of a list of data values."""
    return sqrt(variance(data))

