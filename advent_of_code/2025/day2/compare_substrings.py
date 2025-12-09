
def compare_substrings(size: int, string: str, n: int):
    """
    Docstring for compare_substrings

    :param size: Size of the +string+
    :param string: The +string+ itself
    :param n: The number of partitions that the string is split into
    """
    partition_len = int(size / n)
    partition = string[0:partition_len]
    for k in range(1, n):
        start_index = k * partition_len
        end_index   = start_index + partition_len
        if partition != string[start_index:end_index]:
            return False
    return True
