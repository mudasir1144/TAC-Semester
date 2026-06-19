from tokenizer import tokenize


def main():
    expression = input("Enter Expression: ")

    tokens = tokenize(expression)

    print("\nTokens:")
    print(tokens)


if __name__ == "__main__":
    main()