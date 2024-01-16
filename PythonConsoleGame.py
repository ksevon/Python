from random import randrange

print("Ваша задача угадать число")

def CreateRandomNumber(): # Создание случаного числа
    return randrange(0, 101)

CurrentValue = CreateRandomNumber() # "Запекание" случайного числа

while True:
    UserValueInput = int(input("--->")) # Получение числа от пользователя
    
    if UserValueInput == CurrentValue: # Проверка на совпадение
        print(f"Верно вы угадали! {CurrentValue}")
        CurrentValue = CreateRandomNumber()

    elif UserValueInput < CurrentValue:
        if UserValueInput > (CurrentValue - 15):
            print("Ваше число близко но меньше загаданного")
        else:
            print("Ваше число меньше загаданного")

    elif UserValueInput > CurrentValue:
        if UserValueInput < (CurrentValue + 15):
            print("Ваше число близко но больше загаданного")
        else:
            print("Ваше число больше загаданного")
