temp = s[0]
answer = s[0]


for i in range(len(s) - 1):
    if s[i] <= s[i+1]:
        temp += s[i + 1]
        if len(temp) > len(answer):
            answer = temp
    else:
        temp = s[i+1]

print('Longest substring in alphabetical order is: ' + answer)
