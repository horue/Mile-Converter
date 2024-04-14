


def converter(milhas):
    final= milhas * 1.6
    print(final)




def pergunta():
    milhas=int(input('Qual valor você gostaria de converter para quilômetros? '))
    return milhas


def outro():
    res=input('Deseja converter outro valor? ')
    if res == 's' or "S":
        return
    else:
        SystemExit


while True:
    milhas = pergunta()
    converter(milhas)
    outro()