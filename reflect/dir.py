for x in dir():
    x_ = globals()[x]
    
    print(f'{x:<30} - {type(x_)}')

    for y in dir(x_):
        print(f'  {y}')
