#Imported tokenizer to divide expression in token
from tokenizer import tokenize 
from tac_generator import generate_tac

#Defining a function
def main():

    expression = input("Enter Expression: ")
    #Send expression to tokenize function , convert expression to token

    tokens = tokenize(expression)

    print("\nTokens:")
    print(tokens)

    print("\nThree Address Code:")
    #send token to function to generate_tac
    generate_tac(tokens)

#Check whether the file is directly running or imported 
#if directly run then runs in (main)
if __name__ == "__main__":
    main()