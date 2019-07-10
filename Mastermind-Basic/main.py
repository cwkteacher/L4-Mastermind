import random
LENGTH = 4

def generate_sequence(letters):
    sequence = []
    for i in range(LENGTH):
        letter = random.choice(letters)
        while letter in sequence:
            letter = random.choice(letters)
        sequence.append(letter)
    
    return "".join(sequence)
    
def get_guess(letters):
    guess = input("Enter your guess:  ").upper()
    
    if len(guess) != LENGTH:
        print("Invalid length.  Sequence must be 4 letters.")
        guess = get_guess(letters)
    
    for letter in guess:
        if letter not in letters:
            print("Invalid letter.  Sequence can only contain A, B, C, D, E, F, G, and/or H.")
            guess = get_guess(letters)
            break
    
    return guess
    
def check_guess(sequence, guess):
    response = []
    imperfect = 0
    
    # check how many letters are in perfect or imperfect positions
    for i in range(LENGTH):
        if sequence[i] == guess[i]:
            response.append("P")
        elif sequence[i] in guess:
            imperfect += 1
    
    # add an imperfect markers to the end of the list
    for i in range(imperfect):
        response.append("O")
    
    # print out the response
    print("".join(response))
    
def main():
    letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
    print("Welcome to Mastermind!")
    sequence = generate_sequence(letters)
    print(sequence)
    
    guess_count = 0
    guess = ""
    
    while guess_count < 10 and guess != sequence:
        guess = get_guess(letters)
        check_guess(sequence, guess)
        guess_count += 1
    
    if guess == sequence:
        print("You guessed the sequence in {} guesses".format(guess_count))
    else:
        print("You are out of guesses.")
        
if __name__ == "__main__":
    main()
