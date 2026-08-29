from config import MAXIMUM_PARCEL_WEIGHT


def fetch_weights_list() -> list[float]:
    parcel_weights = []
    print("Enter parcel weight (kg) one per line. Press Enter on empty line to finish:")

    while True:
        weight = input()
        if weight == "":
            if parcel_weights:
                assert len(parcel_weights) > 0
                assert all(w > 0 for w in parcel_weights)
                assert all(w <= MAXIMUM_PARCEL_WEIGHT for w in parcel_weights)
                return parcel_weights
            print("Enter at least one value.")
            continue

        try:
            value = float(weight)
            if value <= 0:
                print("Enter a non-zero positive value.")
                continue
            if value > MAXIMUM_PARCEL_WEIGHT:
                print(f"Maximum allowed weight is {MAXIMUM_PARCEL_WEIGHT} kg.")
                continue

            assert 0 < value <= MAXIMUM_PARCEL_WEIGHT
            parcel_weights.append(value)

        except ValueError:
            print("Please enter a valid number.")
