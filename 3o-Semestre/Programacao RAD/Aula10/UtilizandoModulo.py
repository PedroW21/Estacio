import ModuloTransporte
# Poderiamos importar partes do modulo como: from ModuloTransporte import calcula_imposto e etc...

ladroagem = ModuloTransporte.calcula_imposto()

# Saber oque tem no modulo

print(dir(ModuloTransporte))

# Pacote é uma espécie de coleção de módulos.
# A grande diferença física fundamental entre ambos é simples: os módulos são organizados em arquivos, e os pacotes, em pastas.
# Além disso, nos pacotes, temos de incluir um arquivo especial (__init__.py), o qual faz o interpretador Python identificar os pacotes que estão sendo usados. 
# Quando o interpretador Python encontra um arquivo desses em uma pasta, ela passa a ser um pacote.

