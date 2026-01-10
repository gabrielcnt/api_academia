from marshmallow import Schema, fields
from marshmallow.validate import Range


class ExercicioSchema(Schema):
    id = fields.Str(required=False)
    nome = fields.Str(required=True)
    grupo_muscular = fields.Str(required=True)
    repeticoes = fields.Int(required=True, validate=Range(min=1))
    series = fields.Int(required=True, validate=Range(min=1))

class ExercicioSchemaUpdate(Schema):
    id = fields.Str(required=False)
    nome = fields.Str(required=True)
    grupo_muscular = fields.Str(required=True)
    repeticoes = fields.Int(required=True, validate=Range(min=1))
    series = fields.Int(required=True, validate=Range(min=1))