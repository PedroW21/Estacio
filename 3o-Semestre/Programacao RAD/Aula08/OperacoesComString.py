second_king = "Pedro de Alcântara João Carlos Leopoldo Salvador Bibiano Francisco Xavier de Paula Leocádio Miguel Gabriel Rafael Gonzaga de Bragança e Bourbon"

#for names in second_king:
#    print(names)
print(f"Dom Pedro 2º tem {len(second_king)} caracteres no nome")
print(second_king[:18])
print(second_king[19:30])
print(second_king[107:])
print(second_king[:18].upper())


# Verificar se a string contém caracteres não alfabéticos
#second_king.isalpha()

# Retirar espaços em branco no início e no fim da string
# second_king.strip()

# Juntar cada item da string por meio de um delimitador especificado
# "-".join(second_king)

# O método center() centraliza strings em uma sequência de determinada largura
print("\n")

ex = "Hello World!!"

print(ex.center(19, "*"))