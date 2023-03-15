import math

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        
    def __str__(self):
        # DETERMINE STAR SPLIT FOR TITLE
        left_stars_count = math.floor((30 - len(self.name)) / 2)
        right_stars_count = math.ceil((30 - len(self.name)) / 2)

        # GENERATE TITLE LINE
        title_string = ""
        for i in list(range(left_stars_count)):
            title_string += "*"
        title_string += self.name
        for i in list(range(right_stars_count)):
            title_string += "*"
        title_string += "\n"

        # LINE ITEM GENERATION
        for i in range(len(self.ledger)):
            # 1ST - CONCAT DESCRIPTION
            if len(self.ledger[i]["description"]) < 23:
                title_string += self.ledger[i]["description"]
                # add blank space to end of description string if needed
                for j in list(range(23 - len(self.ledger[i]["description"]))):
                    title_string += " "
            else:
                title_string += self.ledger[i]["description"][0:23]
            # 2ND - CONCAT PRICE
            price_string = "{:.2f}".format(self.ledger[i]["amount"])
            title_string += price_string.rjust(7, " ")
            title_string += "\n"
        
        # GENERATE TOTAL AMOUNT LINE
        title_string += "Total: " + str(self.get_balance())

        return title_string 

    def deposit(self, amount, description = None):

        #BEGIN If description is none, set description to blank
        if description is None:
            description = ""
        #END
        
        self.ledger.append({"amount":amount, "description": description})

    def withdraw(self, amount, description = None):
        if self.get_balance() >= amount:
            #BEGIN handle null description
            if description is None:
                description = ""
            #END

            self.ledger.append({"amount":amount * -1, "description": description})
            return True
        else:
            return False

    def transfer(self, amount, target_category):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, "Transfer to " + target_category.name)
        target_category.deposit(amount, "Transfer from " + self.name)
        return True

    def get_balance(self):
        sum = 0
        for i in range(len(self.ledger)):
            sum += self.ledger[i]["amount"]
        return sum
    
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

def create_spend_chart(categories):
    cat_spent_totals = []
    total_spent_overall = 0
    final_string = "Percentage spent by category\n"

    for category in categories:
        cat_spent = 0

        # Calculate the total spent and store values
        for line_item in category.ledger:
            if line_item["amount"] < 0:
                cat_spent += line_item["amount"]
        cat_spent_totals.append(cat_spent)
        total_spent_overall += cat_spent
    
    # Print out the percentiles chart
    percentile = 100
    while percentile >= 0:
        final_string += str(percentile).rjust(3, " ") + "|"
        for i in range(len(cat_spent_totals)):
            if (cat_spent_totals[i] / total_spent_overall) * 100 >= percentile:
                final_string += " o "
            else:
                final_string += "   "
        final_string += " \n"
        percentile = percentile - 10

    # Print hash line
    final_string += "    "
    for i in range(len(categories)):
        final_string += "---"
    final_string += "-\n"

    # Print category names
    cat_name_len = []
    longest_len = 0
    for cat in categories:
        cat_name_len.append(len(cat.name))
        if len(cat.name) > longest_len:
            longest_len = len(cat.name)
    
    for i in range(longest_len):
        final_string += "    "
        for cat in categories:             
            if i < len(cat.name):
                final_string += " " + cat.name[i] + " "
            else:
                final_string += "   "
        if i < longest_len - 1:
            final_string += " \n"
        else:
            final_string += " "
    
    return final_string