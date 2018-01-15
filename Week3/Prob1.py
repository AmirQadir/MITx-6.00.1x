def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...

    found = False
    for i in secretWord:
        for j in lettersGuessed:
            if (j == i):
                found = True
                break
            else:
                found = False

        if (found):
            continue
        else:
            break
    if(found):
        return True
    else:
        return False

secretWord = input("Please Enter the secret word")
lettersGuessed = input("Enter the guessed letters")
print(isWordGuessed(secretWord, lettersGuessed))
