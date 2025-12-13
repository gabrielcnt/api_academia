def validacoes(dado):
    erros = []
    if not dado:
        erros.append("dado não enviado")
        return erros
    
    if "id" not in dado:
        erros.append("O campo 'id' é obrigatório")

    if "nome" not in dado:
        erros.append("O campo 'nome' é obrigatório")

    if "grupo_muscular" not in dado:
        erros.append("O campo 'grupo_muscular' é obrigatório")

    if "series" not in dado:
        erros.append("O campo 'series' é obrigatório")

    if "repeticoes" not in dado:
        erros.append("O campo 'repeticoes' é obrigatório")
    
    return erros
