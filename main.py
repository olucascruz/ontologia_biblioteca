from owlready2 import *
from ontologia_biblioteca import *



if __name__ == "__main__":

    
    # Carregando a ontologia
    onto = get_ontology(r"biblioteca_ontologia.owl").load()
    print(f"Título do livro1: {livro1.titulo}")
    print(f"Autor do livro1: {livro1.escritoPor.name}")
    print(f"Categoria do livro1: {livro1.pertenceA.name}")


    # Consulta dinâmica
    novo_livro = Livro("livro2")
    novo_livro.titulo = "Owlready para Iniciantes"
    novo_livro.escritoPor = Autor("Autor2")
    novo_livro.pertenceA = Categoria("Educação")

    # Verificando se as alterações foram refletidas corretamente
    print(f"Título do novo livro: {novo_livro.titulo}")
    print(f"Autor do novo livro: {novo_livro.escritoPor.name}")
    print(f"Categoria do novo livro: {novo_livro.pertenceA.name}")