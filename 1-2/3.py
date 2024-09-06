def table():
    for i in range(1, 11):
        for j in range(1,11): 
            print(f'{i*j}'.ljust(3), end='')
        print('\n')

table()