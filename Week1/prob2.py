b = 'bob'
l = len(b)
count = 0
for i in range(len(s)-len(b)+1):
    if(s[i:i+len(b)]==b):
        count+=1
print(("Number of times bob occurs is:"),count)
