from typing import Dict
from itertools import zip_longest


class Category:
    def __init__(self, category):
        self.category = category
        # instructions say ledger must be a list of dictionary entries, this make print method more complicated than if simple dictionary
        self.ledger = list()
        self.balance = 0

    def deposit(self, amount, description = ""):
        if amount is not None:
            self.balance += amount
            self.ledger.append({"amount":amount, "description":description})
        return None    
    
    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        else:
            return False    

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount":-amount, "description":description})
            self.balance -= amount
            withdrawn = True
        else:
            withdrawn = False    
        return withdrawn

    def get_balance(self):
        return self.balance

    def transfer(self, amount, transfer_category):
        """
        A `transfer` method that accepts an amount and another budget category as arguments. 
        The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]".
        The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". 
        If there are not enough funds, nothing should be added to either ledgers. This method should return `True` if the transfer took place, and `False` otherwise.
        """
        description = f"Transfer to {transfer_category.category}"
        dest_descript = f"Transfer from {self.category}"
        if self.check_funds(amount):
            self.withdraw(amount, description)
            transfer_category.deposit(amount, dest_descript)
            processed = True
        else:
            processed = False
        return processed        

    def __str__(self):
        budget_string = "{:*^30s}".format(self.category) + "\n"
        for element in range(len(self.ledger)):
            budget_string += "{:<23}".format(self.ledger[element]["description"][0:23])
            budget_string += "{:>7.2f}".format(self.ledger[element]["amount"]) + "\n"   
        budget_string += "Total: {:.2f}".format(self.get_balance())     
        return budget_string




def create_spend_chart(categories):
    spends = list()
    names = list()
    for cat in categories:
        names.append(cat.category)
        spent = 0
        for i in range(len(cat.ledger)):
            # if i == 0:
            #     totals.append(cat.ledger[i]['amount'])
            #elif cat.ledger[i]['amount'] < 0:
            if cat.ledger[i]['amount'] < 0:
                spent += -cat.ledger[i]['amount']
        spends.append(spent)       
    prop_spent = list()
    total = 0
    for s in spends:
        total += s
    for s in spends:
        prop_spent.append(int(s/total * 100)) 
    y_axis = list(range(100,-1,-10))
    bar_chart = "Percentage spent by category\n"  
    lines = list()
    for y in range(len(y_axis)):
        lines.append("{:>3}|".format(str(y_axis[y])))
        for i in range(len(prop_spent)):
            if prop_spent[i] >= y_axis[y]:
                char = "o"
            else:
                char = " "    
            if i == 0:
                lines[y] += " " + char  
            else:         
                lines[y] += "  " + char    
    bar_chart += '  \n'.join(lines)  
    bar_chart += '  \n'
    bar_chart += "    " + "-"*(len(spends)*2) + "-" + "-"*(len(spends)) + "\n"
    
    words = list()
    for name in names:
        letters = list()
        for letter in name:
            letters.append(letter)
        words.append(letters)    
    for item in zip_longest(*words, fillvalue = ' '):
        for i in range(len(item)):
            if i == 0:
                bar_chart += "     " + item[i]
            else:
                bar_chart += "  " + item[i]
        bar_chart += "  \n"    
    bar_chart = bar_chart[:-1]    
    return bar_chart            
