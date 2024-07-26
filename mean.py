def mean(list):
    """Return mean of list"""
    sum = 0
    count = 0
    for item in list:
        sum = sum + item
        count = count + 1
    return sum / count