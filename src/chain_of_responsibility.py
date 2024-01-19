class Dispenser:
    def __init__(self, next_dispenser, bill_value):
        self.withdrawals = []
        self.next_dispenser = next_dispenser
        self.bill_value = bill_value

    def set_withdraw(self, num_bills):
        self.withdrawals.append([num_bills, self.bill_value])

    def dispense(self, amount):
        num_bills = amount // self.bill_value
        remaining_amount = amount % self.bill_value

        if num_bills > 0:
            self.withdrawals.append([num_bills, self.bill_value])

        if remaining_amount > 0 and self.next_dispenser:
            lower_withdrawals = self.next_dispenser.dispense(remaining_amount)
            if lower_withdrawals:
                self.withdrawals.extend(lower_withdrawals)
            else:
                self.withdrawals = None
        elif remaining_amount > 0 and self.next_dispenser is None:
            return False

        return self.withdrawals


# Create dispensers for different bill denominations
min_denomination = 5

d5 = Dispenser(None, min_denomination)
d10 = Dispenser(d5, 10)
d20 = Dispenser(d10, 20)
d50 = Dispenser(d20, 50)

# Handle the dispensing request
amount = 85
print(f"Dispensing ${amount}:")
response = d50.dispense(amount)

if response:
    for r in response:
        print(f"Dispensing {r[0]} ${r[1]} bills")
else:
    print(f"Invalid Denomination entered, Please enter denomination in multiples of ${min_denomination}")

# Dispensing $85:
# Dispensing 1 $50 bills
# Dispensing 1 $20 bills
# Dispensing 1 $10 bills
# Dispensing 1 $5 bills
