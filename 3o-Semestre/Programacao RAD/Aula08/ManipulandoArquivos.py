ajaxEx = open("C:\\Users\\Pedro Verner\\Desktop\\Estacio\\3o-Semestre\\Programacao RAD\\Aula08\\AJAX-Example.txt", "r+")

# Formas de mostrar o conteudo do arquivo

# Linha a linha (todas as linhas)
for line in ajaxEx:
    print(line)

# Numa paulada só
print(ajaxEx.read())

# Numa paulada só no modo lista

print(ajaxEx.readlines())

# Linha a linha (literalmente)

print("Primeira linha:", ajaxEx.readline())
print("Segunda linha:", ajaxEx.readline())

# Criando um arquivo vazio

newArchive = open("C:\\Users\\Pedro Verner\\Desktop\\Estacio\\3o-Semestre\\Programacao RAD\\Aula08\\ImNew.txt", "w")
newArchive.write("Hello! I was writed by python ;p")

