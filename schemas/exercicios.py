from marshmallow import Schema, fields
from marshmallow.validate import Range
from schemas.plain import PlainExercicioSchema

class ExercicioSchema(PlainExercicioSchema):
    aluno_id = fields.Int(required=True)

class ExercicioSchemaUpdate(Schema):
    nome = fields.Str(required=True)
    grupo_muscular = fields.Str(required=True)
    repeticoes = fields.Int(required=True, validate=Range(min=1))
    series = fields.Int(required=True, validate=Range(min=1))
    aluno_id = fields.Int(required=False)