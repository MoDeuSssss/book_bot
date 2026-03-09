from functools import lru_cache

print('Это файл прямиком с GitHub')

print('АААААвыаываыафы')

def f(a: int|float, s: str) -> str:
    return a * s

def f2(lst: list[int|float], tpl: tuple[str, list], sep: str='') -> str:
    return 'ds'

def f3(dct: dict[int, str|float]) -> dict:
    return {3: 'd'}


@lru_cache(None)
def rcs1(x):
    print(f'down: x = {x}')
    rcs2(x - 1)
    print(f'up: x = {x}')

def rcs2(x):
    print(f'down: x = {x}')
    rcs3(x - 1)
    print(f'up: x = {x}')

def rcs3(x):
    print(f'down: x = {x}')
    print(f'up: x = {x}')

def rcs(x):
    print(f'down: x = {x}')
    if x > 1:
        rcs(x-1)    # Каждый вызов функции, а также параметр х, не зависит друг от друга
    print(f'up: x = {x}')


print('Одна рекурсивная функция')
rcs(3)
print()
print('Несколько обычных функций')
rcs1(3)


def set_zeros(p, i, j, sz):
    if p[i][j] != '*':
        return
    p[i][j] = '@'

    if i-1 >= 0 and p[i-1][j] == '*':
        set_zeros(p, i-1, j, sz)
    if i+1 < sz and p[i+1][j] == '*':
        set_zeros(p, i+1, j, sz)
    if j-1 >= 0 and p[i][j-1] == '*':
        set_zeros(p, i, j-1, sz)
    if j+1 < sz and p[i][j+1] == '*':
        set_zeros(p, i, j+1, sz)


pole = [['#', '*', '*', '*', '#'],
        ['#', '#', '#', '#', '#'],
        ['*', '*', '*', '*', '#'],
        ['#', '#', '*', '*', '*'],
        ['#', '#', '*', '#', '#']]

N = len(pole)

set_zeros(pole, 2, 2, N)

print(*pole, sep='\n')