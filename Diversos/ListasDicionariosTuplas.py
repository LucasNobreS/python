#TEMAS: listas (list), tuplas (tuple), dicionários (dict), conjuntos (set)

#LISTAS(list): 
primeira_lista = ["LISTAS", 3, 3.2, True]

lista = ["primeiro elemento"]
lista.append("segundo elemento")#comando de incluir elemento, para deletar é possivel usar o del
#print(lista)

lista.remove("segundo elemento")#tambem remove pode usar tanto posição quanto nome
#print(lista)

lista[0] = "novo elemento" #atribui novo valor
#print(lista)

#print(len(primeira_lista))

#strings tambem sao consideradass listas, entao os comandos acima tambem funcionam em strings
texto = "FLAMENGO"
#print(texto[4])


#TUPLA(tuple):

#mesmas caracteristicas de lista mas é imutavel
primeira_tupla = ("Tuplas", 3, 4.5, False)#() opcionais
#modo de acesso é igual mas para acessar a posicao é com []

#CONJUNTO(set):
#nao tem ordem definida e nao pode ter elementos repetidos
primeiro_conjunto = {"Conjunto", 3, 4.6, True}
segundo_conjunto = {1,1,1,3,3,3,True,"conjunto", "conjunto", "data"}#elimina repetição sem dar erro e nao possui ordem
segundo_conjunto.add("+1 elemento")# mesmo do append
conjunto = segundo_conjunto.pop() #exibe elemento mas remove do conjunnto, se converter pra lista nao remove


#DICIONARIOS(dict):
#lembrar do dicionario de verdade, pois no python é uma chave que remete a um valor

dicionario = {"piton":"Serpente da Ásia e da África, não venenosa, que constringe as presas com seus anéis. (O píton reticulado, ou molura, da península da Malásia, mede de 7 a 10 m e atinge o peso de 100 kg; é a maior serpente que existe atualmente.)."}
dicio = { "nome": "Alberto", "idade": "43", "altura": "1,84"}
#metodos mais importantes de dicionarios sao keys(), values(), items()
#print(dicio.keys()) nesse caso, nome idade e altura
#print(dicio.values()) nesse caso, Alberto, 43 e 1,84
#print(dicio.items())# nesse caso, nome: Alberto, idade: 43 e altura: 1,84
#del dicio["altura"] remove itens, porem, necessario especificar as chaves
#dicio["nome"] = "Lucas" alterar itens tambem parecido com a lista


#CONVERSÕES:
#(o dict nao tem como converter pois precisa dos pares chave valor)

#raul_seixas = ["eu prefiro seeeer", "essa metamorfose ambulante"]
#raul_seixas = tuple(raul_seixas) estrutura para converter
#raul_seixas = set(raul_seixas)
#print(type(raul_seixas))

#listapdict = ["Destrito federal", "DF", "GO", "Goias"]
#listapdict = dict([("Destrito federal", "DF"),( "GO", "Goias")]) conversao deve ser nesse modelo exato

