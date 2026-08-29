## --------------------------------------
# Calculate compound interest for savings
## --------------------------------------

# Variables with meaningful names
principal = 1000.0  # Initial amount
rate = 0.05  # 5% annual interest rate
time = 3  # 3 years
compound_frequency = 12  # Monthly compounding

# Calculate compound interest
final_amount = principal * (1 + rate / compound_frequency) ** (
    compound_frequency * time
)
interest_earned = final_amount - principal

print(f"Initial investment: {principal:.2f}")
print(f"Interest earned: {interest_earned:.2f}")
print(f"Final amount: {final_amount:.2f}")
