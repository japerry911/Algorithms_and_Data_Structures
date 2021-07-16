def is_perfect_square(num: int) -> bool:
    """determine if input is perfect quare or not
    :param int num: the input number being checked
    :returns: value saying whether input number is perfect square or not
    :rtype: bool
    """
    for i in range(1, num + 1):
        if i * i == num:
            return True
        elif i * i > num:
            return False

    return False
