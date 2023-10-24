import random

def dice_roll():
    roll = random.randint(1, 6)
    print("Кубик выпал на:", roll)

    if roll in [5, 6]:
        print("Вы выиграли!")
    elif roll in [3, 4]:
        dice_roll()
    else:
        print("Попробуйте еще раз…")

dice_roll()