from owlready2 import *

# Criação a ontologia
onto = get_ontology(r"owl_files\biblioteca_ontologia.owl")

# Classes superiores
class Obra(Thing):
    namespace = onto

class Pessoa(Thing):
    namespace = onto

# Definindo classes
class Livro(Obra):
    namespace = onto

class Autor(Pessoa):
    namespace = onto

class Categoria(Thing):
    namespace = onto

# Definindo propriedades
class escritoPor(ObjectProperty):
    namespace = onto
    domain = [Livro]
    range = [Autor]

class pertenceA(ObjectProperty):
    namespace = onto
    domain = [Livro]
    range = [Categoria]

# Adicionando indivíduos
livro1 = Livro("livro1")
livro1.titulo = "Aventuras de Owlready"
livro1.escritoPor.append(Autor("Autor1"))
livro1.pertenceA.append(Categoria("Ficção"))

# Adicionando categoria de Computação
categoria_computacao = Categoria("Computação")

# Adicionando autores de livros de computação
autor_turing = Autor("Alan Turing")
autor_turing.nome = "Alan Turing"

autor_knuth = Autor("Donald Knuth")
autor_knuth.nome = "Donald Knuth"

# Adicionando livros de computação
livro_introducao = Livro("Introdução à Computação")
livro_introducao.titulo = "Introdução à Computação"
livro_introducao.escritoPor.append(autor_turing)
livro_introducao.pertenceA.append(categoria_computacao)

livro_art_of_programming = Livro("The Art of Computer Programming")
livro_art_of_programming.titulo = "The Art of Computer Programming"
livro_art_of_programming.escritoPor.append(autor_knuth)
livro_art_of_programming.pertenceA.append(categoria_computacao)

# Salvando a ontologia
onto.save(file=r"owl_files\biblioteca_ontologia.owl")
