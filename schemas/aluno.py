from marshmallow import Schema, fields
from marshmallow.validate import Range

from schemas.plain import PlainAlunoSchema, PlainExercicioSchema

class AlunoSchema(PlainAlunoSchema):
    exercicio = fields.List(fields.Nested(PlainExercicioSchema()),
                            dump_only=True)

class AlunoSchemaUpdate(Schema):
    nome = fields.Str(required=True)
    idade = fields.Int(required=True, validate=Range(min=1))
    cpf = fields.Int(required=True, validate=Range(min=0))