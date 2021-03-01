name = input('Вкажіть своє ім\'я:')
surname = input('Вкажіть своє прізвище:')
print("Привіт, %s %s!" % (name, surname))
age = int(input('Скільки тобі років?:'))
if age <= 25:
    print('У тебе все життя попереду.')
elif age <= 40 and age >=26:
    print('Ти старший(а) мене.')
elif age <= 60 and age >= 41:
    print('ого!')
else:
    print('СКІЛЬКИ!!!')
Як_справи = input('А як у тебе справи? (добре, погано, так собі):')
if Як_справи == 'добре':
    print('О, в мене теж!')
elif Як_справи == 'погано':
    print(input('Ой, що стлось?:'))
    print('''Ох.
    Вище носа!''')
elif Як_справи == 'так собі'
    print(input('Чому?:')
    print('Оу')
print(input('Ну, що ж пока? :'))