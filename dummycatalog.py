"""
This is a FooBarBaz schema catalog used throughout this tutorial.
"""
from forml.io import dsl


class Foo(dsl.Schema):
    """Foo dataset schema."""

    Timestamp = dsl.Field(dsl.Timestamp())
    Label = dsl.Field(dsl.Integer())
    Level = dsl.Field(dsl.String())
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
          not resolved by any of the feeds configured within this tutorial
          platform.
    """

    Key = dsl.Field(dsl.Integer())
    Name = dsl.Field(dsl.String())
    Dob = dsl.Field(dsl.Date())
