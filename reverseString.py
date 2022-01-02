def reverseWord(s):
    #your code here
    newString = ''
    for i in range(len(s)):
        newString += s[len(s)-1-i]
    
    return newString
