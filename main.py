from tokenizer import tokenize
from tac_generator import generate_tac


def main():

    expression = input("Enter Expression: ")

    tokens = tokenize(expression)

    print("\nTokens:")
    print(tokens)

    print("\nThree Address Code:")

    generate_tac(tokens)


if __name__ == "__main__":
    main()