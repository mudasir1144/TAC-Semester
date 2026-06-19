temp_count = 0


def new_temp():
    global temp_count
    temp_count += 1
    return f"t{temp_count}"


def generate_tac(tokens):

    if len(tokens) != 5:
        print("Only expressions like a = b * c or a = b / c are supported")
        return

    target = tokens[0]
    left = tokens[2]
    operator = tokens[3]
    right = tokens[4]

    if operator not in ["*", "/"]:
        print("Only multiplication and division supported currently")
        return

    temp = new_temp()

    print("\nThree Address Code:\n")

    print(f"{temp} = {left} {operator} {right}")
    print(f"{target} = {temp}")