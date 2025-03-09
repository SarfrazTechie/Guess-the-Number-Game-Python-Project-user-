import random

def guess_the_number():
    print("Welcome to the Guess the Number Game!")
    print("Think of a number between 1 and 100, and I will try to guess it!")
    
    low = 1
    high = 100
    guess = random.randint(low, high)
    
    while True:
        print(f"Is your number {guess}?")
        feedback = input("Enter H if too high, L if too low, or C if correct: ").lower()
        
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        elif feedback == "c":
            print(f"Yay! I guessed your number {guess} correctly!")
            break
        else:
            print("Invalid input. Please enter H, L, or C.")
        
        guess = random.randint(low, high)  # Make a new guess based on updated range

if __name__ == "__main__":
    guess_the_number()
