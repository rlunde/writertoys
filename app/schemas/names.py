from .. import ma
from ..models.names import Names


class NamesSchema(ma.ModelSchema):

    class Meta:
        model = Names


names_schema = NamesSchema()
names_schema = NamesSchema(many=True)
