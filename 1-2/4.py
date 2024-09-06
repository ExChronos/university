def find(element, massive):
    for e in massive:
        if e == element:
            return True
    return 'Не смог найти'
        
print(find(4, [2,0,1,4,2,8,0,2]))