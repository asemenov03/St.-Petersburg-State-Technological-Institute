def f(n):
    if len(n) <= 1:
        return n
    opora = sum(n) // len(n)
    spisok_sleva = [i for i in n if i < opora]
    center = [i for i in n if i == opora]
    spisok_sprava = [i for i in n if i > opora]
    return f(spisok_sleva) + center + f(spisok_sprava)


def greben(n):
    dlina = int(len(n) / 1.3)
    while dlina >= 1:
        try:
            for i in range(len(n)):
                if n[i] > n[i + dlina]:
                    n[i], n[i + dlina] = n[i + dlina], n[i]
        except IndexError:
            dlina = int(dlina / 1.3)
    return n

