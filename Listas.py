def excluir_numero(lista):
    n = float(input('digite o numero quee deseja remover:  '))
    if n in lista:
        lista.remove(n)
    else:
        print('este numero nao está na lista ')


def soma(lista):
    return sum(lista)


def media(lista):
    return sum(lista)/len(lista)

def pares(lista):
    lista1 = []
    for n in lista:
        if n % 2 == 0:
            lista1.append(n)
    return lista1

def ordenar_lista(lista):
    return sorted(lista)


def tam_lista(lista):
    return len(lista)


def popular_lista():
    lista = []
    while True:
        texto = input('Adcione quantos numeros quiser, e quando desejar para: digite "stop" .')
        if texto.lower() == 'stop':
            print('FIM!!!!!')
            break
        else:
            n = float(texto)
            lista.append(n)
    return lista


answer = input(f'--------------VAMOS MONTAR UMA LISTA COM NUMEROS DIVERSOS?-------sim/não----')
if answer.lower() == 'sim':
    lista = popular_lista()
    print(f'Lista ordenada :  {ordenar_lista(lista)}')
    print('############################################')
    print(f'lista completa {lista}')
    print('############################################')
    print(f'numeros :  {tam_lista(lista)}')
    print('############################################')
    print(f'soma : {soma(lista)}')
    print('############################################')
    print(f'numeros pares:  {pares(lista)}')
    print('############################################')
    print(f'media :  {media(lista)}')
else:
    print("######### NOS VEMOS NA PROXIMA #############")

answer2 = input('Deseja remover algum numero da lista?---------sim/não-----------')
if answer2 == 'sim' :
    excluir_numero(lista)
    print(f'REMOVIDO!!! ----->>>>>  {lista}')
else:
    print("######### NOS VEMOS NA PROXIMA #############")
