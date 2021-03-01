what = input('Що робим? (-, +, *, /, %, **):')
a = float(input('Яке перше число?:'))
b = float(input('Яке друге число?:'))
if what == '-':
    c = a - b
    print(c)
elif what == '+':
    c = a + b
    print(c)
elif what == '*':
    c = a * b
    print(c)
elif what == '/':
    c = a / b
    print(c)
elif what == '%':
    c = a % b
    print(c)
elif what == '**':
    c = a ** b
    print(c)
else:
    print('Введина не правильна операція.')