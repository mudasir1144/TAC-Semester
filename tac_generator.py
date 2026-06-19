temp_count = 0


def new_temp():
    global temp_count
    temp_count += 1
    return f"t{temp_count}"