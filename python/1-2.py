# факториал числа
def one(n):
    if n == 0:
        return 1
    else:
        return n * one(n-1)

# числа Фибоначчи
def two(n):
    if n <= 2:
        return 1
    else:
        return two(n-1)+two(n-2)
    
# уникальные элементы
def three(massive):
    return set(massive)

# возвращение словаря
def four(string):
    words = dict()

    for i in string:
        if i not in words.keys():
            words[i]=1
            continue
        words[i]+=1

    return words

# переворот строки
def five(string):
    ret_string = ''
    for i in range(len(string)):
        ret_string += string[len(string)-1-i]

    return ret_string

# проверка на палиндром
def six(string):
    count = 0

    for i in range(len(string)//2):
        if string[i] == string[len(string)-i-1]:
            count += 1
        else:
            return False
    if count != len(string)//2:
        return False
    else:
        return True
    
# сортировка списка
def seven(massive):
    if len(massive) < 2:
        return massive
    else:
        n = massive[0]
        less = [i for i in massive if i < n]
        greater = [i for i in massive if i > n]

        return seven(less) + [n] + seven(greater)

# сумма чисел в строке
def eight(string):
    summa = 0
    for i in string:
        summa += int(i)
    return summa

# словарь со списком значений
def nine(lisst):
    spisok = dict()

    for i in lisst:
        if i not in spisok:
            spisok[i] = 1
            continue
        spisok[i] += 1

    return spisok

# решето Эратосфена
def ten(n):

    primes = [i for i in range(n+1)]
    primes[1]=0

    i=2
    while i <= n:
        if primes[i] != 0:
            j = i+i

            while j <= n:
                primes[j] = 0
                j += i
        i += 1
    
    primes = [i for i in primes if i != 0]

    return primes

# генерация паролей
def eleven():
    import hashlib

    sha = hashlib.sha1(b'Hello Python').hexdigest()

    return sha

# сумма квадратов
def twelve(massive):
    import math
    squares = set()

    n = max(massive)

    simple = [i for i in range(1, n)]

    for e in massive:
        if math.sqrt(e) in simple:
            print(e)
            squares.add(e)
    
    summa = sum(squares)

    return summa

# объедиинение списков
def thirteen(lst1, lst2):
    st1 = set(lst1)
    st2 = set(lst2)

    return st1.union(st2)

# поиск уникальных слов
def fourteen(string):
    unic = dict()
    ret_unic = set()

    words = string.split(' ')
    
    for word in words:
        if word not in unic:
            unic[word] = 1
            continue
        unic[word] += 1

    for key, value in unic.items():
        if value == 1:
            ret_unic.add(key)
    
    return ret_unic

# поиск анаграм
def fifteen(word, massive):
    anagrams = set()

    word1 = list(word)
    word1.sort()

    for e in massive:
        word2 = list(e)
        word2.sort()

        if word1 == word2:
            anagrams.add(e)

    return f'{word} - {anagrams}'
