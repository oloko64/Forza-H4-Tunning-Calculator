import os


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


# Global variable for the % of weight distribution of the car
weight_distr = 0


def weight_distribution():
    global weight_distr
    weight_distr = 0
    print(f'>>>> Weight Distribution <<<<')
    print('')
    weight_distr = input("Type the % of weight distribution: ")
    if (weight_distr == ''):
        weight_distr = 0
    return weight_distr


def inputs():
    global weight_distr
    maxi = input("Type the max value: ")
    mini = input("Type the min value: ")
    if (maxi == '' or mini == ''):
        maxi = 0
        mini = 0
    print('')
    return weight_distr, maxi, mini


def calculos():
    aux = inputs()
    resul_front = (float(aux[1]) - float(aux[2])) * \
        (float(aux[0]) / 100) + float(aux[2])
    resul_back = (float(aux[1]) - float(aux[2])) * \
        ((100 - float(aux[0])) / 100) + float(aux[2])
    return (round(resul_front, 2)), (round(resul_back, 2))


def damping(valor):
    print(f'>>>> Damping Results <<<<')
    print('')
    print(f'Rebound Stiffness Front ==> {valor[0]}')
    print(f'Rebound Stiffness Rear ==> {valor[1]}')
    print('')
    print(f'Bump Stiffness Front ==> {round((valor[0] * 60) / 100, 2)}')
    print(f'Bump Stiffness Rear ==> {round((valor[1] * 60) / 100, 2)}')


def springs(valor):
    print(f'>>>> Springs Results <<<<')
    print('')
    print(f'Springs Front ==> {valor[0]}')
    print(f'Springs Rear ==> {valor[1]}')


def anti_roll(valor):
    print(f'>>>> Antirolls Bars Results <<<<')
    print('')
    print(f'Antiroll Bars Front ==> {valor[0]}')
    print(f'Antiroll Bars Rear ==> {valor[1]}')


def run_weight():
    weight_distribution()
    clearConsole()


def run_damping():
    print('>>>> Damping Input <<<<')
    print('')
    damping(calculos())
    print('')
    input('Press ENTER for the next menu...')
    clearConsole()


def run_springs():
    print('>>>> Springs Input <<<<')
    print('')
    springs(calculos())
    print('')
    input('Press ENTER for the next menu...')
    clearConsole()


def run_antiroll():
    print('>>>> Antiroll Bars Input <<<<')
    print('')
    anti_roll(calculos())
    print('')
    input('Press ENTER to exit...')
    clearConsole()


def run():
    try:
        run_weight()
        run_damping()
        run_springs()
        run_antiroll()
    except (ValueError):
        clearConsole()
        print('Only numbers are allowed...')
        print('')
        run()
    except:
        clearConsole()
        print('Exiting...')


if __name__ == "__main__":
    run()
