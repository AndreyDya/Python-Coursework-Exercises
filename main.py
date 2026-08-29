from input_handling import fetch_weights_list
from sorting import quicksort
from display import print_with_separators
from config import MAXIMUM_PARCEL_WEIGHT


def main():
    parcel_weights = fetch_weights_list()

    assert len(parcel_weights) > 0
    assert all(isinstance(w, (int, float)) for w in parcel_weights)

    sorted_list = quicksort(parcel_weights)

    assert len(sorted_list) == len(parcel_weights)
    assert all(sorted_list[0] <= w for w in parcel_weights)

    minimum = sorted_list[0]

    assert minimum > 0
    assert minimum <= MAXIMUM_PARCEL_WEIGHT

    count = parcel_weights.count(minimum)
    assert 1 <= count <= len(parcel_weights)

    result_line = (
        f"The lightest parcel weighs {minimum} kg ({count} parcels share this weight)."
        if count > 1
        else f"The lightest parcel weighs {minimum} kg."
    )

    print_with_separators(
        [
            f"Original weight list: {parcel_weights}",
            f"Sorted by weight (ascending): {sorted_list}",
            "",
            result_line,
        ]
    )


if __name__ == "__main__":
    main()
