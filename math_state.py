def arithmetic_arranger(problems, sol = False):
    #initial values
    states = []
    arranged_problems = None

    if len(problems) > 5:
        arranged_problems = "Error: Too many problems."
        return arranged_problems
    else:
        for prob in problems:
            states.append(SimpleState(prob))
            # Test for errors after object creation. If found, return the error.
            if states[len(states) - 1].error:
                arranged_problems = states[len(states) - 1].error
                return arranged_problems
        arranged_problems = print_string(states, sol)
    return arranged_problems


def print_string(statements, print_sol):
    final_print = ""
    #Need 4 loops to generate 4 rows of data. Num1, OP + Num2, ----, Answer(???)

    #Loop 1
    i = 0
    while i < len(statements):
        final_print += statements[i].getNum1String()
        if i == len(statements) - 1:
            final_print += "\n"
        else:
            final_print += "    "
        i += 1

    #Loop 2
    i = 0
    while i < len(statements):
        final_print += statements[i].getNum2String()
        if i == len(statements) - 1:
            final_print += "\n"
        else:
            final_print += "    "
        i += 1

    #Loop 3
    i = 0
    while i < len(statements):
        final_print += statements[i].getBar()
        if i != len(statements) - 1:
            final_print += "    "
        elif print_sol and i == len(statements) - 1:
            final_print += "\n"
        i += 1

    #Loop 4 if necessary
    i = 0
    while print_sol and i < len(statements):
        final_print += statements[i].getSolString()
        if i != len(statements) - 1:
            final_print += "    "
        i += 1

    return final_print


class SimpleState:

    def __init__(self, math_state):
        #First, split the statement
        split_state = math_state.split(" ")

        if len(split_state[0]) > 4 or len(split_state[2]) > 4:
            self.error = "Error: Numbers cannot be more than four digits."
        elif not self.isValidOp(split_state[1]):
            self.error = "Error: Operator must be '+' or '-'."
        elif not self.isValidNum(split_state[0], split_state[2]):
            self.error = "Error: Numbers must only contain digits."
        else:
            self.error = None

        if self.error is None:
            self.num1 = split_state[0]
            self.num2 = split_state[2]
            self.op = split_state[1]
            self.line_len = self.calcLineLen()
            self.solution = self.calcSol()

    def isValidOp(self, op):
        if op == "+" or op == "-":
            return True
        else:
            return False

    def isValidNum(self, *nums):
        for num in nums:
            if num.isnumeric():
                continue
            else:
                return False
        return True


    def calcLineLen(self):
        if len(self.num1) > len(self.num2):
            return len(self.num1) + 2
        else:
            return len(self.num2) + 2

    def getNum1String(self):
        num1Str = ""

        i = 0
        while i < self.line_len - len(self.num1):
            num1Str += " "
            i += 1

        num1Str += self.num1
        return num1Str

    def getNum2String(self):
        num2Str = self.op + " "

        i = 0
        while i < self.line_len - 2 - len(self.num2):
            num2Str += " "
            i += 1

        num2Str += self.num2
        return num2Str

    def getBar(self):
        bar = ""

        i = 0
        while i < self.line_len:
            bar += "-"
            i += 1

        return bar

    def calcSol(self):
        if self.op == "+":
            return str(int(self.num1) + int(self.num2))
        elif self.op == "-":
            return str(int(self.num1) - int(self.num2))
        else:
            return ""
        
    def getSolString(self):
        sol_string = ""

        i = 0
        for i in range(0, self.line_len - len(self.solution)):
            sol_string += " "
        return sol_string + self.solution