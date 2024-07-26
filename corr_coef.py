import math

def mean(list):
    """Return mean of list"""
    sum = 0
    count = 0
    for item in list:
        sum = sum + item
        count = count + 1
    return sum / count

def corr_coef(list_x, list_y):
    """ Return correlation between values in list_x and list_y.

    Lists must be of equal length.
    
    """
    
    x_bar = mean(list_x)
    y_bar = mean(list_y)
    sxy = 0
    sxx = 0
    syy = 0
    for index in range(len(list_x)):
        x = list_x[index]
        y = list_y[index]
        sxy = sxy + (x - x_bar) * (y - y_bar)
        sxx = sxx + (x - x_bar) * (x - x_bar)
        syy = syy + (y - y_bar) * (y - y_bar)
    return sxy / math.sqrt(sxx * syy)