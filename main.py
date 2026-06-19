from tokenizer import tokenize
from tac_generator import new_temp


def main():
    expression = input("Enter Expression: ")

    tokens = tokenize(expression)

    print("\nTokens:")
    print(tokens)

    print("\nGenerated Temporary Variables:")

    print(new_temp())
    print(new_temp())
    print(new_temp())


if __name__ == "__main__":
    main()