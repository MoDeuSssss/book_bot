print('Это файл прямиком с GitHub')

print('АААААвыаываыафы')

def f(a: int|float, s: str) -> str:
    return a * s

def f2(lst: list[int|float], tpl: tuple[str, list], sep: str='') -> str:
    return 'ds'

def f3(dct: dict[int, str|float]) -> dict:
    return {3: 'd'}
