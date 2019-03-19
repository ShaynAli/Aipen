def partition(original_list, *proportions):
    """
    Splits a list into sub-lists based on the indices.
    """
    indices = partition_indices(original_list, *proportions)
    return [original_list[start:end] for start, end in zip(indices[:-1], indices[1:])]


def partition_indices(original_list, *proportions):
    from itertools import accumulate
    length = len(original_list)
    return [0] + list(accumulate([int(p * length) for p in proportions])) + [length]
