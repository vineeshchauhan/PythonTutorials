weight = input('Enter your weight ')
convertTo = input('Convert to Kg(k) or Lb(l) ')

if convertTo.lower() == 'k':
    converted = int(weight) * 2.20462
    print(f'Your weight in KG is {converted}')
elif convertTo.lower() == 'l':
    converted = int(weight) // 2.20462
    print(f'Your weight in lb is {converted}')
else:
    print('Invalid input')