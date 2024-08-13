print('Write a word that is a palindrome(word that is the same even when read backwards)') 
word = list(input())
def check(x):
    for i in range(len(x)):
            if len(word) > 1 and x[0] != x[-1]:
                return False
            elif i ==(len(x)/2):
                return True
            else:
                return True
if check(word) == True:
    print('Congratulations, that is a palindrome :)')
else:
    print('That is not a palindrome, sorry :(')