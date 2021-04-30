import Car
import os

# Code made by OLoKo64
# Copied code ready to use for clear the console in Unix and Windows machines


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def run():
    try:
        print('>>>>>>>>>>>>>>> Forza Horizon 4 Tunning Calculator <<<<<<<<<<<<<<<\n\n')

        carro.peso = float(input('Weight (Kg): '))
        carro.distr_peso = int(input('Weight distribuition (%): '))
        if (carro.distr_peso < 0 or carro.distr_peso > 100):
            raise Exception('Outside of parameters')
        carro.rig_mola = int(input('Spring stiffness [Default: 20]: ') or 20)
        carro.barra_20 = int(input('Total damping bar [Default: 20]: ') or 20)

        print('\n')

        print(f'Suspension Front: {carro.suspencaoFront()}')
        print(f'Suspension Rear: {carro.suspencaoRear()}')
        print('')
        print(f'Damping Front: {carro.reboundFront()}')
        print(f'Damping Rear: {carro.reboundRear()}')
        print('')
        print(f'Rebound Front: {carro.bumpFront()}')
        print(f'Rebound Rear: {carro.bumpRear()}')
        print('\n')
        input('Press ENTER to exit...')
    except(ValueError):
        clearConsole()
        print('Only numbers are valid...\n')
        run()
    except(KeyboardInterrupt):
        clearConsole()
        print('Exiting...\n')
    except(Exception):
        clearConsole()
        print('Percentage error... [Only 0 to 100 is accepted]\n')
        run()


carro = Car.Carro(0, 0, 0, 0)
clearConsole()
run()
