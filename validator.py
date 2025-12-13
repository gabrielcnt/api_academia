
class Validator:

    @staticmethod
    def validar_post(dado):
        erros = []
        
        if not dado:
            return "dado não enviado"
        
        campos = [
            "id",
            "nome",
            "grupo_muscular",
            "series",
            "repeticoes"
        ]
        for campo in campos:
            if campo not in dado:
                erros.append(f"O campo {campo} é obrigatorio")
        return erros
        
    
    @staticmethod
    def validar_put_del(dado):
        erros = []

        if not dado:
            return "dado não enviado"
        
        campos = [
            "nome",
            "grupo_muscular",
            "series",
            "repeticoes"
        ]

        for campo in campos:
            if campo not in dado:
                erros.append(f"O campo {campo} é obrigatorio")
        
        return erros

