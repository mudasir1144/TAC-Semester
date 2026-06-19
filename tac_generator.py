temp_count = 0


def new_temp():
    global temp_count
    temp_count += 1
    return f"t{temp_count}"


def generate_tac(tokens):

    if len(tokens) != 5:
        print("Only expressions like a = b * c are supported")
        return

    target = tokens[0]

    left_operand = tokens[2]
    plus_operator = tokens[3]

    middle_operand = tokens[4]
    multiply_operator = tokens[5]
    right_operand = tokens[6]

    if operator != "*":
        print("Only multiplication supported currently")
        return

    t1 = new_temp()
    print(f"\n{t1} = {middle_operand} * {right_operand}")

    t2 = new_temp()
    print(f"{t2} = {left_operand} + {t1}")

    print(f"{temp} = {left} * {right}")
    print(f"{target} = {temp}")