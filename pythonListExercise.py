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
            n = int(texto)
            lista.append(n)
    return lista

answer = input(f'--------------VAMOS MONTAR UMA LISTA COM NUMEROS DIVERSOS?-------sim/não----')
if answer.lower() == 'sim':
    lista = popular_lista()
    print(f'lista completa {lista}')
    print(f'tamanho da lista {tam_lista(lista)}')
    print(f'Lista ordenada :  {ordenar_lista(lista)}')
else:
    print("######### NOS VEMOS NA PROXIMA #############")



