#input is an integer
#output is a palindrome which reads same backward or forward

s = 515


lst = list()


def isPalindrome(x):
    x = str(x)
    for i in x:
        lst.append(i)
        if lst[0] == lst[-1]:
            print(True)
        elif lst[0] == '-':
            print(False)
isPalindrome(121)