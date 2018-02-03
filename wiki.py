import wikipedia
import sys

wikipedia.set_lang('PT')

def print_option(lista):
    print('Sua busca pode se referir à:')
    for option in lista:
        print(str(lista.index(option)+1)+" "+option)
    index=input('A qual dessas opçoes vc se refere?')
    #print(lista[int(index)-1])
    return search(lista[int(index)-1])

def search(querry):
    try:
        resultado=wikipedia.summary(querry)
    except wikipedia.exceptions.DisambiguationError as e:
        return print_option(e.options)

    except:
        return
    # except Exception as e:
    #     if e==wikipedia.exceptions.DisambiguationError:
    #         print('entrou')
    #         print_option(e)
    #
    #     else:
    #         print('me desculpe,aconteceu algo inesperado:',e)
    #         return

    if resultado:
        return resultado
    else:
        sugestao=wikipedia.suggest(querry)
        op=input('vc quis dizer '+sugestao+"?(Y/n)")
        if(op=='y' or op=='Y'):
            return search(sugestao)
        else:
            new_querry=('refaça sua busca:')
            search(new_querry)
#testes
# querry=input('oq está buscando:')
# print(search(querry=querry))

def main():
    print(search(sys.argv[1]))

if __name__=='__main__':
    main()
