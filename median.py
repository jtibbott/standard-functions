def median(list):
    """ Calculates the median of a list of numbers.
The list must not be empty.
"""

    number_of_values = len(list)
    sorted_list = sorted(list)

    # Two cases, depending on whether the number of values is odd or even.
    quotient = number_of_values // 2
    remainder = number_of_values % 2
 
    if (remainder == 1):
        result = sorted_list[quotient]
    else:
        result = (sorted_list[quotient - 1] + sorted_list[quotient]) / 2
    return result