from marshmallow import Schema, fields
from marshmallow.validate import Range

class AlunoSchema(Schema):
    id = fields.Str(required=False)
    nome = fields.Str(required=True)
    idade = fields.Int(required=True, validate=Range(min=1))
    cpf = fields.Int(required=True, validate=Range(min=0))

class AlunoSchemaUpdate(Schema):
    id = fields.Str(required=False)
    nome = fields.Str(required=True)
    idade = fields.Int(required=True, validate=Range(min=1))
    cpf = fields.Int(required=True, validate=Range(min=0))