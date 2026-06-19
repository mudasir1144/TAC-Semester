temp_count = 0


def new_temp():
    global temp_count
    temp_count += 1
    return f"t{temp_count}"


def generate_tac(tokens):

    if len(tokens) != 7:
        print("Current version supports: a = b + c * d")
        return

    target = tokens[0]

    left_operand = tokens[2]
    plus_operator = tokens[3]

    middle_operand = tokens[4]
    multiply_operator = tokens[5]
    right_operand = tokens[6]

    if plus_operator != "+" or multiply_operator != "*":
        print("Only pattern: a = b + c * d is supported")
        return

    t1 = new_temp()
    print(f"\n{t1} = {middle_operand} * {right_operand}")

    t2 = new_temp()
    print(f"{t2} = {left_operand} + {t1}")

    print(f"{target} = {t2}")