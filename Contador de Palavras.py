"""
contar quantas palavras tem em cada documento
"""


livro_1 = open('livro.txt', 'r', encoding='utf_8')
salvar_palavras = open('salvar_palavras.txt', 'w', encoding='utf8')
conteudo = livro_1.readlines()


def retira_pontos(word):
    """ salva as palavras"""
    pontos = [',', '.', ':', ';']
    word = ''.join([i for i in word if i not in pontos]).lower()
    return word


list_temp1 = []
for palavras_k in conteudo:
    palavra_v = palavras_k.split(' ')
    for LETRAS_K in palavra_v:
        LETRAS_K = LETRAS_K.rstrip('\n')
        if LETRAS_K == '':
            del LETRAS_K
        else:
            list_temp1.append(retira_pontos(LETRAS_K))

list_temp2 = list(set((x for x in list_temp1)))

list_final = []
for k in list_temp2:
    list_final.append([k, list_temp1.count(k)])

list_temp1.clear()
list_temp2.clear()

list_final.sort(lambda ordena: ordena[1], reverse=True)

for palavra, vezes in list_final:
    livro_1.write(f'"{palavra}" aparece {vezes} vezes\n')

print('ok')

livro_1.close()
salvar_palavras.close()
