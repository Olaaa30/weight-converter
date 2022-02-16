run = True
user_weight = float(input('>weight:'))
while run:
    selection = input('pounds(l) or kilos(k)? ')

    if selection.lower() == 'k': 
        weight = user_weight * 2.20462
        print(f'your weight in pounds is {weight}')
        run = False

    elif selection.lower() == 'l':
        weight = user_weight * 0.4535
        print(f'your weight in kilos is {weight}')
        run = False

    else:
        print('wrong input!!! Please input l or k')

