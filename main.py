import random

point = random.randint(1, 100)
count = 0
print("Добро пожаловать в числовую угадайку, введите число от 1 до 100")
def is_valid(Scanner):
    if 1 <= Scanner <= 100:
        return True
    else:
        return False

def game(count):
    while True:
        Scanner = int(input())
        if not is_valid(Scanner):
            print("Нужно ввести число от 1 до 100")
            break
        if Scanner < point:
            print("Ваше число меньше загаданного, попробуйте еще разок")
        elif Scanner > point:
            print("Ваше число больше загаданного, попробуйте еще разок")
        elif Scanner == point:
            print("Вы угадали, поздравляем!")
            break
        count += 1
        print(f'Всего попыток {count}')

game(count)
