points = 174

if points <= 50:
    result = "Congratulations! You won a wooden rabbit!"
elif points <= 150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    result = "Congratulations! You won a wafer-thin mint!"
else:
    result = "Congratulations! You won a penguin!"

print(result)


# GUESS MY NUMBER

answer = 60
guess = 100   # this is just a sample answer and guess

if guess < answer:
    result = "Oops!  Your guess was too low."
elif guess > answer:
   result = "Oops!  Your guess was too high."
elif guess==answer:
    result = "Nice!  Your guess matched the answer!"
print(result)

# TAX PURCHASE
# Depending on where an individual is from we need to
# tax them appropriately. The states of CA, MN, and NY have taxes of 7.5%, 9.5%,
# and 8.9% respectively. Use this information to take the amount of a purchase and
# the corresponding state to assure that they are taxed by the right amount.

state = "CA"
purchase_amount = 20.00

if state == "CA":
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == "MN":
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state,total_cost)

elif state == "NY":
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {} , your total cost is {}.".format(state,total_cost)

print(result)










