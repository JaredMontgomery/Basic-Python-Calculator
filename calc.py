import re

# Used to limit the size of an input. 64 is arbitrary, so you can set it to
# whatever you want.
LEN_LIMIT: int = 64

print("""Hello. This is a basic calculator made with Python. It supports and can
do pretty much anything you want. Enter q (or Q) to quit at any time.\n""")

while True:
    # Short for math expression.
    math_exp: str = input("Enter some math: ")

    # The following if statement is used to ensure that math_exp is a valid
    # math expression. Doesn't check syntax, though.

    # Used to end the loop and end the program.
    if math_exp == 'q' or math_exp == 'Q':
        break
    # Used to prevent function calls and any dangerous imports.
    elif re.search("[a-zA-Z]", math_exp):
        print("No letters allowed.\n")
        continue
    elif len(math_exp) > LEN_LIMIT:
        print(f"Expression length exceeds {LEN_LIMIT} char limit.\n")
        continue
    
    # Executes and prints the results of the math expression... if valid.
    try:
        print(f"{math_exp} = {eval(math_exp)}\n")
    except SyntaxError:
        print("Syntax Error. Expression was invalid.\n")