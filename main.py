import logging
import random

logging.basicConfig(filename="ex.log", level=logging.INFO)


def play_game(N, k):
    # загадываем случайное число от 1 до N
    number = random.randint(1, N)
    logging.info(f"the computer chose a number {number}")

    for i in range(k):
        # получаем попытку от пользователя
        guess = int(input("Введите число от 1 до {}: ".format(N)))

        # проверяем, правильно ли отгадано число
        if guess == number:
            logging.info("Player win!")
            print("Вы угадали!")
            return
        elif guess < number:
            print("Загаданное число больше")
            logging.info("Player called number {} The hidden number is greater".format(guess))
        else:
            print("Загаданное число меньше")
            logging.info("Player called number {} The hidden number is less".format(guess))

    # если у пользователя закончились попытки
    print("Вы не угадали :(")
    logging.info("Attempts ended.")


# запрашиваем у пользователя N и k
N = int(input("Введите число, до которого загадывать: "))
k = int(input("Введите количество попыток: "))

# запускаем игру
play_game(N, k)
