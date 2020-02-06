bool = True

while bool:
    s = input()
    if s != 'End':
        print('Processing "' + s + '" command...')
    else:
        bool = False
        print('Good bye!')
