arquivo = open("arquivo.txt", "w") #cria o arquivo

arquivo.write("Curso de Python\n")
arquivo.write("Aula Prática\n")
arquivo.close()

#ler arquivos

leitura = open("arquivo.txt", "r")
print(leitura.read())
leitura.close()