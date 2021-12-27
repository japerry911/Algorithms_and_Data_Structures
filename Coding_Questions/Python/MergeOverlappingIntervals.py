from typing import List

import pytest


def merge_overlapping_intervals(intervals: List[List]) -> List[List]:
    """Merges any overlapping intervals and returns new intervals, order
        does not matter

    :param List[List] intervals: input intervals
    :rtype: List[List]
    :returns: any overlapping intervals
    """
    intervals.sort(key=lambda x: x[0])

    overlapping_return_list = list()
    merge_interval = None

    for start_idx in range(len(intervals)):
        next_idx = start_idx + 1
        start_interval = intervals[start_idx]

        if merge_interval is None:
            merge_interval = start_interval

        if next_idx < len(intervals):
            # not the end of intervals
            next_interval = intervals[next_idx]

            if merge_interval[1] < next_interval[0]:
                overlapping_return_list.append(merge_interval)
                merge_interval = None
            elif next_interval[1] > merge_interval[1]:
                merge_interval[1] = next_interval[1]
        else:
            # end of the intervals
            overlapping_return_list.append(merge_interval)

    return overlapping_return_list


def test_merge_overlapping_intervals():
    input_test = [
        [1, 2],
        [3, 5],
        [4, 7],
        [6, 8],
        [9, 10]
    ]
    expected_output = [
        [1, 2],
        [3, 8],
        [9, 10]
    ]
    output = merge_overlapping_intervals(input_test)
    print(f"{output} == {expected_output}")
    assert output == expected_output

    input_test = [
        [1, 3],
        [2, 8],
        [9, 10]
    ]
    expected_output = [
        [1, 8],
        [9, 10]
    ]
    output = merge_overlapping_intervals(input_test)
    print(f"{output} == {expected_output}")
    assert output == expected_output

    input_test = [
        [1, 10],
        [10, 20],
        [20, 30],
        [30, 40],
        [40, 50],
        [50, 60],
        [60, 70],
        [70, 80],
        [80, 90],
        [90, 100]
    ]
    expected_output = [
        [1, 100]
    ]
    output = merge_overlapping_intervals(input_test)
    print(f"{output} == {expected_output}")
    assert output == expected_output

    input_test = [
        [1, 10],
        [11, 20],
        [21, 30],
        [31, 40],
        [41, 50],
        [51, 60],
        [61, 70],
        [71, 80],
        [81, 90],
        [91, 100]
    ]
    expected_output = [
        [1, 10],
        [11, 20],
        [21, 30],
        [31, 40],
        [41, 50],
        [51, 60],
        [61, 70],
        [71, 80],
        [81, 90],
        [91, 100]
    ]
    output = merge_overlapping_intervals(input_test)
    print(f"{output} == {expected_output}")
    assert output == expected_output

    input_test = [
        [100, 105],
        [1, 104]
    ]
    expected_output = [
        [1, 105]
    ]
    output = merge_overlapping_intervals(input_test)
    print(f"{output} == {expected_output}")
    assert output == expected_output

    input_test = [
        [89, 90],
        [-10, 20],
        [-50, 0],
        [70, 90],
        [90, 91],
        [90, 95]
    ]
    expected_output = [
        [-50, 20],
        [70, 95]
    ]
    output = merge_overlapping_intervals(input_test)
    print(f"{output} == {expected_output}")
    assert output == expected_output

    input_test = [
        [-5, -4],
        [-4, -3],
        [-3, -2],
        [-2, -1],
        [-1, 0]
    ]
    expected_output = [
        [-5, 0]
    ]
    output = merge_overlapping_intervals(input_test)
    print(f"{output} == {expected_output}")
    assert output == expected_output

    input_test = [
        [43, 49],
        [9, 12],
        [12, 54],
        [45, 90],
        [91, 93]
    ]
    expected_output = [
        [9, 90],
        [91, 93]
    ]
    output = merge_overlapping_intervals(input_test)
    print(f"{output} == {expected_output}")
    assert output == expected_output

    input_test = [
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0]
    ]

    expected_output = [
        [0, 0]
    ]
    output = merge_overlapping_intervals(input_test)
    print(f"{output} == {expected_output}")
    assert output == expected_output

    input_test = [
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 1]
    ]

    expected_output = [
        [0, 1]
    ]
    output = merge_overlapping_intervals(input_test)
    print(f"{output} == {expected_output}")
    assert output == expected_output

    input_test = [
        [1, 22],
        [-20, 30]
    ]

    expected_output = [
        [-20, 30]
    ]
    output = merge_overlapping_intervals(input_test)
    print(f"{output} == {expected_output}")
    assert output == expected_output

    input_test = [
        [20, 21],
        [22, 23],
        [0, 1],
        [3, 4],
        [23, 24],
        [25, 27],
        [5, 6],
        [7, 19]
    ]

    expected_output = [
        [0, 1],
        [3, 4],
        [5, 6],
        [7, 19],
        [20, 21],
        [22, 24],
        [25, 27]
    ]
    output = merge_overlapping_intervals(input_test)
    print(f"{output} == {expected_output}")
    assert output == expected_output

    input_test = [
        [2, 3],
        [4, 5],
        [6, 7],
        [8, 9],
        [1, 10]
    ]

    expected_output = [
        [1, 10]
    ]
    output = merge_overlapping_intervals(input_test)
    print(f"{output} == {expected_output}")
    assert output == expected_output


pytest.main(["MergeOverlappingIntervals.py"])
