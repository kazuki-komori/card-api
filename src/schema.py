from graphene_file_upload.scalars import Upload
import graphene
from graphene import Schema, ObjectType, String


class UploadMutation(graphene.Mutation):
    class Arguments:
        file = Upload(required=True)
    success = graphene.Boolean()

    def mutate(self, info, file):
        return 'hogehoge'


# class Query(ObjectType):
#     hello = String(name=String(default_value="hoge"))
#
#     def resolve_hello(self, info, name):
#         return f'こんにちは {name}さん'

schema = Schema(mutation=UploadMutation)
