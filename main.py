import sys


def converter(milhas):
    try:
        final= milhas * 1.6
        print(final)
    except TypeError:
        print('Erro. O valor deve ser um número.')





def pergunta():
    try:
        milhas=int(input('Qual valor você gostaria de converter para quilômetros? '))
        return milhas
    except ValueError:
        print('Erro. O valor deve ser um número.')
        return()



def outro():
    res=input('Deseja converter outro valor? ')
    if res in ['s','S']:
        return
    elif res in ['n', 'N']:
        sys.exit

def main():
    milhas = pergunta()
    converter(milhas)
    outro()