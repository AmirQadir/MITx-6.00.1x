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


print(getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's']))
