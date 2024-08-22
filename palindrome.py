print('Write a word that is a palindrome(word that is the same even when read backwards)') 
word = list(input())
def check(x):
    for i in range(len(x)):
            length = len(word)
            if length == 1 or length == 0:
                return True
            if length > 1 and x[0] != x[-1]:
                return False
            else:
                del x[0]
                del x[-1]
if check(word) == True:
    print('Congratulations, that is a palindrome :)')
else:
    print('That is not a palindrome, sorry :(')