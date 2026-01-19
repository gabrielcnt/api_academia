from marshmallow import Schema, fields

class PlainAlunoSchema(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True)
    idade = fields.Int(required=True)
    cpf = fields.Int(required=True)

class PlainExercicioSchema(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True)
    grupo_muscular = fields.Str(required=True)
    series = fields.Int(required=True)
    repeticoes = fields.Int(required=True)