# Andrey Dya
# Portfolio exercise 2
# Speed Control Display:
# A program that displays a message to a driver if they are travelling more than 70 mph / less than 70 mph.
# Additional features: In case of speeding, the program calculates and displays the amount of the speeding ticket based on Kazakhstani traffic laws.


# Define a function to calculate the speeding ticket amount, in accordance with Kazakhstani traffic rules (in km/h)
# Function returns MCI value based on the severity of the speeding
def calc_speeding_ticket_amount(speed):
    kmph_speed = speed / 0.621371
    speed_limit = 70 / 0.621371
    # No need to account for kmph_speed <= speed_limit, function is only called when speeding
    if kmph_speed <= speed_limit + 20:
        fine = 5  # in MCI
    elif kmph_speed <= speed_limit + 40:
        fine = 10
    elif kmph_speed <= speed_limit + 60:
        fine = 20
    else:
        fine = 40
    return fine, kmph_speed  # Return both the fine and the km/h speed for further use


# Current Monthly Calculation Index (MCI) in Kazakhstan (in Tenge)
MCI = 3932


# Define a function to display the speeding ticket details
def speeding_ticket(speed):
    fine, kmph_speed = calc_speeding_ticket_amount(speed)
    title = "\n-------------- Speeding Ticket --------------"
    print(title)
    # Display recorded speed in both mph and km/h (hence returning kmph_speed in calc_speeding_ticket_amount)
    print(f"Recorded speed: {speed} mph / {kmph_speed:.2f} km/h")
    # Fine amount is calculated by multiplying the fine in MCI by the current MCI value
    print(f"Speeding ticket amount: KZT {fine*MCI:,}")
    # Format with comma to separate thousands
    print("-" * len(title.strip()))
    # Print the lower border the same length as the title


# Define a function to get the user's speed and provide feedback
def get_speed():
    while True:
        try:
            speed = float(input("Enter your speed in mph: "))
            if speed <= 0:
                print("\nAre you even driving?")
                continue
            elif speed <= 70:
                print(
                    "\nYou're driving safely"
                    if speed < 70
                    else "\nYou're driving at the speed limit, be cautious!"
                )
            # Simulated speed of the fastest car in the world: 330 mph
            elif speed >= 330:
                print("\nImpossible speed. Please enter a realistic speed.")
                continue
            else:
                print("\nYou're speeding!")
                speeding_ticket(speed)
            break
            # Could return speed for future use, but in this case its redundant
        except ValueError:
            print("Invalid input. Please enter a numeric value for speed.")


# Call the function to check speed and display result
get_speed()
