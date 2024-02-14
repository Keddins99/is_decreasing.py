def is_decreasing(lst, prev=float('inf')):
    if not lst:
        return True

    # check if current is less than current
    if lst[0] < prev:
        return is_decreasing(lst[1:], lst[0])
    else:
        # if the current is not less than the previous, list is not decreasing
        return False
