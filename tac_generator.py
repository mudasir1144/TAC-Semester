temp_count = 0


def new_temp():
    global temp_count
    temp_count += 1
    return f"t{temp_count}"

# Generate unique temporary variables
def generate_tac(tokens):

    if len(tokens) == 9 and tokens[2] == "(" and tokens[6] == ")":

        target = tokens[0]

        left = tokens[3]
        operator = tokens[4]
        middle = tokens[5]

        final_operator = tokens[7]
        right = tokens[8]

        t1 = new_temp()
        print(f"\n{t1} = {left} {operator} {middle}")

        t2 = new_temp()
        print(f"{t2} = {t1} {final_operator} {right}")

        print(f"{target} = {t2}")

        return
    
    if len(tokens) == 7 and tokens[3] in ["+", "-"] and tokens[5] in ["+", "-"]:

        target = tokens[0]

        left = tokens[2]
        op1 = tokens[3]
        middle = tokens[4]
        op2 = tokens[5]
        right = tokens[6]

        t1 = new_temp()
        print(f"\n{t1} = {left} {op1} {middle}")

        t2 = new_temp()
        print(f"{t2} = {t1} {op2} {right}")

        print(f"{target} = {t2}")

    elif len(tokens) == 7 and tokens[3] == "+" and tokens[5] == "*":

        target = tokens[0]

        left = tokens[2]
        middle = tokens[4]
        right = tokens[6]

        t1 = new_temp()
        print(f"\n{t1} = {middle} * {right}")

        t2 = new_temp()
        print(f"{t2} = {left} + {t1}")

        print(f"{target} = {t2}")

    else:
        print("Expression not supported in current version")