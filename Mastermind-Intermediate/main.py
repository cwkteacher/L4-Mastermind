import random
LENGTH = 4

def new_game(letters):
    '''
    Starts a new game, Give users the option to read the rules, allow users to 
    check if they want to allow duplicates, and generates a new secret code.
    '''
    print("Welcome to Mastermind!")
    answer = input("Would you like to read the rules or start a new game?  ").lower()
    
    # get valid input
    while (answer != "rules") and (answer != "new"):
        print("I'm sorry, I don't understand that input.")
        answer = input("Please enter 'rules' or 'new'.  ").lower()
        
    # print the rules of the game
    if answer == "rules":
        print_rules()
        answer = input("Enter 'new' to start a new game.  ")
    
    # check if user wants duplicates
    answer = input("Do you want to allow duplicates in the sequence?  ").lower()
    while (answer != "yes") and (answer != "no"):
        answer = input("Please enter 'yes' or 'no'.  ").lower()
    if answer == "yes":
        duplicates = True
    else:
        duplicates = False
    sequence = generate_sequence(letters, duplicates)
    
    return sequence
        
def print_rules():
    print('''
    The object of the mastermind game is to guess a randomly generated sequence
    of 4 letters, some combination of A, B, C, D, E, F, G, and/or H.  By default,
    the sequence does not contain duplicates but you can select that option at
    the start of the game to make it more difficult.  To play the game, the user
    enters a sequence of letters.  For any letter that is in the sequence and 
    also in the correct spot, the computer prints an P.  For any letter that is
    in the sequence but in an incorrect spot, the computer prints an O.
    ''')
    
def generate_sequence(letters, duplicates):
    '''
    Generates a new sequence with or without duplicates.
    '''
    sequence = []
    if duplicates:
        for i in range(LENGTH):
            sequence.append(random.choice(letters))
    else:
        for i in range(LENGTH):
            letter = random.choice(letters)
            while letter in sequence:
                letter = random.choice(letters)
            sequence.append(letter)
    
    return "".join(sequence)
    
def get_guess(letters):
    '''
    Gets a guess from the user can checks if it is valid.
    '''
    guess = input("Enter your guess:  ").upper()
    
    if len(guess) != LENGTH:
        print("Invalid length.  Sequence must be 4 letters.")
        guess = get_guess(letters)
    
    for letter in guess:
        if letter not in letters:
            print("Invalid letter.  Sequence and only contain A, B, C, D, E, F, G, and/or H.")
            guess = get_guess(letters)
            break
    
    return guess
    
def check_guess(sequence, guess):
    '''
    Checks how many perfect and imperfect guesses there are.
    '''
    response = []
    perfect = 0
    imperfect = 0
    
    sCopy = list(sequence)
    gCopy = list(guess)
    
    # check how many letters are in perfect positions
    i = 0
    while i < len(gCopy):
        if sCopy[i] == gCopy[i]:
            response.append("P")
            perfect += 1
            sCopy.pop(i)
            gCopy.pop(i)
        else:
            i += 1
          
    # check how many letters are in imperfect positions
    while len(gCopy) > 0:
        if gCopy[0] in sCopy:
            imperfect += 1
            sCopy.remove(gCopy[0])
        gCopy = gCopy[1:]
        
    # add an imperfect markers to the end of the list
    for i in range(imperfect):
        response.append("O")
    
    # print out the response
    print("".join(response))
    
    # check for winning the game
    if perfect == LENGTH:
        return True
        
    return False
    
def main():
    letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
    sequence = new_game(letters)
    
    guess_count = 0
    win = False
    
    while guess_count < 10 and not win:
        guess = get_guess(letters)
        win = check_guess(sequence, guess)
        guess_count += 1
    
    if win:
        print("You guessed the sequence in {} guesses".format(guess_count))
    else:
        print("You are out of guesses.")
        
    answer = input("Would you like to play again?  ").lower()
    if answer == "yes":
        main()
        
if __name__ == "__main__":
    main()
