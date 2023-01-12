t = {'plus' : ['더하기', '장점'], 'minus' : ['빼기', '적자'], 'multiply' : ['곱하게', '다양하게'], 'division' : ['나누기', '분열'], 'square' : '제곱'}
d = input("단어: ")
del t[d]
print(t.items())