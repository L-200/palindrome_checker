while True:  
    print('Enter "stop" to end program')
    print('Write a word that is a palindrome(word that is the same even when read backwards)') 
    word = list(input())
    if word == ['s', 't', 'o', 'p']:
        break
    else:
        aux_word = word[:]
        reversed_word = []
        for i in range(len(word)):
            reversed_word.append(word[-1])
            del word[-1]
        if reversed_word == aux_word:
            print('That is a palindrome! Well done!')
        else:
            print('That is not a palindrome, sorry :(')