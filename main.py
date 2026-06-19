from tokenizer import tokenize
from tac_generator import generate_multiplication_tac


def main():

    expression = input("Enter Expression: ")

    tokens = tokenize(expression)

    print("\nTokens:")
    print(tokens)

    generate_multiplication_tac(tokens)


if __name__ == "__main__":
    main()