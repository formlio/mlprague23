"""
This is a FooBarBaz schema catalog used throughout the ForML tutorial.
"""
from forml.io import dsl


class Foo(dsl.Schema):
    """Foo dataset schema."""

    Timestamp = dsl.Field(dsl.Timestamp())
    Label = dsl.Field(dsl.Integer())
    Code = dsl.Field(dsl.String())
    Value = dsl.Field(dsl.Float())
    Bar = dsl.Field(dsl.Integer())


class Bar(dsl.Schema):
    """Bar dataset schema."""

    Key = dsl.Field(dsl.Integer())
    Length = dsl.Field(dsl.Float())
    Color = dsl.Field(dsl.String())


class Baz(dsl.Schema):
    """Baz dataset schema.

    Note: To demonstrate an unavailable dataset, this schema is deliberately
          not resolved by any of the feeds configured in this tutorial
          environment.
    """

    Key = dsl.Field(dsl.Integer())
    Name = dsl.Field(dsl.String())
    Dob = dsl.Field(dsl.Date())
