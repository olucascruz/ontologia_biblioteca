from owlready2 import *

# Criação a ontologia
onto_path.append(r"ontologia_biblioteca\owl_files")
onto = get_ontology(r"biblioteca_ontologia.owl")

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
    domain = [Livro]
    range = [Autor]

class pertenceA(ObjectProperty):
    domain = [Livro]
    range = [Categoria]

# Adicionando indivíduos
livro1 = Livro("livro1")
livro1.titulo = "Aventuras de Owlready"
livro1.escritoPor = Autor("Autor1")
livro1.pertenceA = Categoria("Ficção")

# Salvando a ontologia
onto.save(file="biblioteca_ontologia.owl", format="rdfxml")
