from api import ma
from marshmallow import fields

class CarSchema(ma.Schema):
    class Meta:
        fields = ('_id', 'model', 'specifications', 'year')

    _id = fields.Str()
    model = fields.Str(required=True)
    specifications = fields.Dict(required=True)
    year = fields.Int(required=True)
