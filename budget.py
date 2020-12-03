class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __repr__(self):
        budget = """"""

        budget += f"{self.name:*^30}"

        for entry in self.ledger:
            budget += f"\n{entry['description']:23.23}"
            budget += f"{entry['amount']:>7.2f}"
        
        budget += f"\nTotal: {self.get_balance()}"

        return budget

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount,"description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, \
            "description": description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for entry in self.ledger:
            balance += entry["amount"]
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, \
            f"Transfer to {category.name}")
            category.deposit(amount, \
            f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

def create_spend_chart(categories):
    spend_chart = """Percentage spent by category\n"""
    amounts_spent = []
    display_bar = []

    for category in categories:
        amount_spent = 0

        for entry in category.ledger:
            if entry["amount"] < 0:
                amount_spent -= entry["amount"]
                
        amounts_spent.append(amount_spent)

        display_bar.append(False)

    total_spent = sum(amounts_spent)

    percentages_spent = [int(amount / total_spent * 100) for amount in amounts_spent]

    for i in range(len(percentages_spent)):
        percentages_spent[i] -= percentages_spent[i] % 10

    label = 100
    while (label >= 0):
        spend_chart += f"{label:>3d}|"

        for i in range(len(percentages_spent)):
            if percentages_spent[i] == label or display_bar[i]:
                spend_chart += " o "

                display_bar[i] = True
            else:
                spend_chart += "   "

        spend_chart += " \n"
        label -= 10

    spend_chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    category_names = [category.name for category in categories]
    
    longest_name = max(category_names, key=len)
    letter = 0

    while letter < len(longest_name):
        spend_chart += "     "

        for category in categories:
            try:
                spend_chart += f"{category.name[letter]}  "
            except IndexError:
                spend_chart += "   "
                
        if letter < len(longest_name) - 1:
            spend_chart += "\n"

        letter += 1

    return spend_chart