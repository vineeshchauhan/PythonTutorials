try:
    age = int(input('Age : '))
    print(100/age)
except ValueError:
    print('Invalid value')
except ZeroDivisionError:
    print('Age can not be zero')

