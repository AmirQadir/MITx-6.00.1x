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

secretWord = input("Enter the secret word")
lettersGuessed = input("Enter the letters guessed")
print(getGuessedWord(secretWord, lettersGuessed))
