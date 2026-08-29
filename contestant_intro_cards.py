# Andrey Dya
# Portfolio exercise 1
# Contestant Introduction Card:
# Collects information on three contestants and generates an introduction card for the TV Gameshow host
# Each card includes the following contestant details: name, current occupation, and main hobby

# Create a list to store contestant information
contestants = []

# Collect information for each contestant
for i in range(1, 4):
    print(f"\nContestant {i}:")
    name = input("  Enter name: ")
    occupation = input("  Enter current occupation: ")
    hobby = input("  Enter main hobby: ")

    # Store contestant info as a dictionary
    contestant_info = {"name": name, "occupation": occupation, "hobby": hobby}
    contestants.append(contestant_info)

# Print introduction cards
print("\n--------- Introduction Cards ---------\n")
for index, contestant in enumerate(contestants, start=1):
    print(f"Contestant {index} Introduction Card")
    print("--------------------------------------")
    print(f"Name:        {contestant['name']}")
    print(f"Occupation:  {contestant['occupation']}")
    print(f"Main Hobby:  {contestant['hobby']}")
    print("\nHost's Script:")
    print(
        f"Let's welcome {contestant['name']}, who is a(n) {contestant['occupation']} and enjoys {contestant['hobby']} in their free time!\n"
    )

# Exception handling