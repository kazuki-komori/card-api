from ariadne import gql, make_executable_schema, upload_scalar

type_defs = """
    type Mutation {
        uploadUserImage(image: Upload!): Boolean!
    }
"""

schema = make_executable_schema(type_defs, [..., upload_scalar])


def resolve_image(*_):
    return "Hello///"
