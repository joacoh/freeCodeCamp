# %%
def truncate(n):
    multiplier = 10
    return int(n*multiplier)/multiplier

def get_totals(categories):
    total = 0
    breakdown = []
    for category in categories:
        total += category.get_withdrawls()
        breakdown.append(category.get_withdrawls)
    rounded = list(map(lambda x: truncate(x()/total), breakdown))
    return rounded

def create_spend_chart(categories):
    res = 'Percentage spent by category\n'
    i = 100
    totals = get_totals(categories)
    while i >= 0:
        cat_spaces = ' '
        for total in totals:
            if total*100 >= i:
                cat_spaces += 'o  '
            else:
                cat_spaces += '   '
        res += str(i).rjust(3) + '|' + cat_spaces + '\n'
        i -= 10
    dashes = '-' + '---'*len(categories)
    names = []
    x_axis = ''
    for category in categories:
        names.append(category.name)
    maxi = max(names, key=len)
    for x in range(len(maxi)):
        name_str = '     '
        for name in names:
            if x >= len(name):
                name_str += '   '
            else:
                name_str += name[x] + '  '
        if (x != len(maxi)-1):
            name_str += '\n'
        x_axis += name_str
    res += dashes.rjust(len(dashes)+4) + '\n' + x_axis
    return res

class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = list()
    
    def __str__(self):
        title = f'{self.name:*^30}\n'
        items = ''
        total = 0
        for i in self.ledger:
            items += f"{i['description'][0:23]:23}" + f"{i['amount']:>7.2f}" + '\n'
            total += i['amount']
        output = title + items + 'Total: {}'.format(str(total))
        return output

    def check_funds(self, amount):
        if (self.get_balance() >= amount):
            return True
        return False  
  
    def get_balance(self):
        total = 0
        for i in self.ledger:
            total += i['amount']
        return total
    
    def transfer(self, amount, category):
        if (self.check_funds(amount)):
            self.withdraw(amount, 'Transfer to {}'.format(category.name))
            category.deposit(amount, 'Transfer from {}'.format(self.name))
            return True
        return False

    def deposit(self, amount, desc=''):
        self.ledger.append({'amount': amount, 'description': desc})

    def withdraw(self, amount, desc=''):
        if (self.check_funds(amount)):
            self.ledger.append({'amount': -amount, 'description': desc})
            return True
        return False
    
    def get_withdrawls(self):
        total = 0
        for i in self.ledger:
            if i['amount'] < 0:
                total += i['amount']
        return total

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))
# %%
