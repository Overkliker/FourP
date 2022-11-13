import random

alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ch = '1234567890'


def gen():
    t_or_f = random.randint(0, 1)

    if t_or_f == 0:
        return f'{random.choice(ch)}{random.choice(ch)}{random.choice(ch)}{random.choice(ch)}' \
               f'{random.choice(alp)}{random.choice(alp)}{random.choice(alp)}'

    else:
        return f'{random.choice(alp)}{random.choice(alp)}{random.choice(ch)}{random.choice(ch)}{random.choice(ch)}' \
               f'{random.choice(alp)}'

print(gen())