def quicksort(parcel_weights: list[float]) -> list[float]:
    assert isinstance(parcel_weights, list)
    assert all(isinstance(w, (int, float)) and w > 0 for w in parcel_weights)

    if len(parcel_weights) <= 1:
        return parcel_weights

    pivot = parcel_weights[len(parcel_weights) // 2]
    less = [x for x in parcel_weights if x < pivot]
    equal = [x for x in parcel_weights if x == pivot]
    greater = [x for x in parcel_weights if x > pivot]

    sorted_list = quicksort(less) + equal + quicksort(greater)

    assert len(sorted_list) == len(parcel_weights)
    assert all(
        sorted_list[i] <= sorted_list[i + 1] for i in range(len(sorted_list) - 1)
    )

    return sorted_list
