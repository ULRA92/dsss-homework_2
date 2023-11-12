import random
def generate_Integer(min, max):    
    """ 
    Generates a random integer within the min-max range.
    """    
    return random.randint(min, max)

def random_arithmetic_Operator():
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
    ScoredPoints = 0
    t_questions = 3
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_questions):
        
        n1 = generate_Integer(1, 10)
        n2 = generate_Integer(1, 5)
        operator = random_arithmetic_Operator()
        Operation,answer = calculate_numbers(n1, n2, operator)       
        print(f"\n Operation: {Operation}")
        
        try:
          useranswer = int(input("Your answer: "))
        except ValueError:
          useranswer = 0
    
        if useranswer == answer:
            print("Correct! You earned a point.")
            ScoredPoints += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {ScoredPoints}/{t_questions}")

if __name__ == "__main__":
    math_quiz()
