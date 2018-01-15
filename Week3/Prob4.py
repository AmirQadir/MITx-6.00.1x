def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    x = "abcdefghijklmnopqrstuvwxyz"
    haha = ''
    ans = ''
    found = True
    for i in range(len(x)):
        found = False
        for j in range(len(lettersGuessed)):
            if (x[i] == lettersGuessed[j]):
                found = True
        if(found):
            haha += "haha"
        else:
            ans+=x[i]
    return ans

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...

    found = False
    ans = ''
    ans += "'"
    for i in secretWord:
        for j in lettersGuessed:
            if (j == i):
                found = True
                break
            else:
                found = False

        if (found):
            ans+=i
        else:
            ans+="_ "

    ans += "'"
    finalans = ''
    for i in range(1,len(ans)-1):
        finalans+=ans[i]
    return finalans

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

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many
      letters the secretWord contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(secretWord), "letters long.")
    mistakesMade = 0
    lettersGuessed = []

    while 8 - mistakesMade > 0:
        if (isWordGuessed(secretWord, lettersGuessed)):
            print('------------')
            print('Congratulations, you won!')
            break
        else:
        	print('------------')
        	print('You have', 8 - mistakesMade, 'guesses left.')
        	print('Available letters:', getAvailableLetters(lettersGuessed))
        	guess = str(input('Please guess a letter:')).lower()
        	if guess in secretWord and guess not in lettersGuessed:
        		lettersGuessed.append(guess)
        		print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
        	elif guess in lettersGuessed:
        		print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
        	elif guess not in secretWord:
        		print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
        		lettersGuessed.append(guess)
        		mistakesMade += 1
        if 8 - mistakesMade == 0:
        	print('------------')
        	print('Sorry, you ran out of guesses. The word was', secretWord)
        	break
        else:
        	continue


secretWord = str(input("Please Enter the secret word to play hangman game"))
print(hangman(secretWord))
