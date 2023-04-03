from forml.io import dsl


class Dummy(dsl.Schema):
    """Dummy dataset schema."""

    Title = dsl.Field(dsl.String())
    Key = dsl.Field(dsl.Integer())
    Target = dsl.Field(dsl.Float())
    Timestamp = dsl.Field(dsl.Timestamp())
