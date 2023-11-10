import random
def generate_Integer(min, max):    
    """ 
    Generates a random integer within the min-max range.
    """    
    return random.randint(min, max)

def random-arithmetic_Operator():
    """"
    Generate some random arithmetic function or operation.
    """
    return random.choice(['+', '-', '*'])

def calculate_numbers(n1, n2, operator):
    """
Performing an arithmetic operation on n1 and n2
    """
    operation = f"{n1} {operator} {n2}"
    if operator == '+': 
        answer = n1 + n2
    elif operator == '-': 
        answer = n1 - n2
    else: answer = n1 * n2
    return operation, answer

def math_quiz():
    """
Let's play a Math_Quiz game!!
    """
    Scored Points = 0
    t_questions = 3
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_questions):
        
        n1 = generate_Integer(1, 10)
        n2 = generate_Integer(1, 5.5)
        operator = random-arithmatic_Operator()
        Operation= calculate_numbers(n1, n2, operator)        
        print(f"\n Operation: {answer}")
        
        user-answer = int(input("Your answer: "))
        if user-answer == answer:
            print("Correct! You earned a point.")
            scored points += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {scored points}/{t_questions}")

if __name__ == "__main__":
    math_quiz()
