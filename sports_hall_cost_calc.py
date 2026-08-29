# Andrey Dya
# Portfolio exercise 3
# Sports Hall Cost Calculation
# A program that calculates total rental fee of the sports hall depending on the number of people.


# Constants
SPORTS_HALL_CAPACITY = 200  # maximum person capacity of a hall
BASE_BOOKING_FEE = 18000
FLAT_FEE = 86000
PRICE_SMALL_GROUP = 4280  # per person for 1-10 people
PRICE_MEDIUM_GROUP = 2850  # per person for 11–20 people


# Define a function to collect the number of people, validate, return
def get_people():
    while True:
        try:
            people = int(input("\nRegister the number of people: "))
            if people <= 0:
                print("Enter a valid positive quantity.")
                continue
            if people > SPORTS_HALL_CAPACITY:
                print(f"Maximum capacity is {SPORTS_HALL_CAPACITY}. Try again.")
                continue

            while True:
                confirm = (
                    input(f"Your requested number is {people}. Proceed? (Y/N): ")
                    .strip()  # Ignore accidental blank spaces
                    .lower()  # Add response case insensitivity
                )
                if confirm == "y":
                    return people
                elif confirm == "n":
                    print("Edit your selection.")
                    break  # break the confirmation loop, go back to outer loop
                else:
                    print('Invalid input. Please confirm with "Y" or "N".')
                    continue  # re-ask for Y/N
        except ValueError:
            print("Invalid input. Please enter an integer value.")


# Define a function to calculate total hire fee based on the number of people
def calc_hire_fee(people):
    # Small group: 1 - 10 people
    if people <= 10:
        price = BASE_BOOKING_FEE + people * PRICE_SMALL_GROUP
    # Medium group: 11 - 20 people
    elif people <= 20:
        price = BASE_BOOKING_FEE + people * PRICE_MEDIUM_GROUP
    # Large group: > 21 people
    else:
        price = FLAT_FEE
    return price


# Define a function to output total hire fee,
def main():
    while True:
        people = get_people()
        total_fee = calc_hire_fee(people)
        print("=" * 47)
        print(
            f"Total hire fee for {people} people: {total_fee:,} ₸"
        )  # Add a divider for thousands

        while True:
            redo = input("\nWould you like to calculate again? (Y/N): ").strip().lower()
            if redo == "y":
                break  # Restart the outer loop
            elif redo == "n":
                print("\nExiting program. Bye.")
                return  # End the entire function (and the program)
            else:
                print('Invalid input. Please confirm with "Y" or "N".')


main()
