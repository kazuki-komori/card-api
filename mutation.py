from graphene import ObjectType, String, Schema
from graphene_file_upload.scalars import Upload
import graphene


class UploadMutation(graphene.Mutation):
    class Arguments:
        file = Upload(required=True)
    success = graphene.Boolean()

    def mutate(self, info, file):
        return 'hogehoge'


class Query(ObjectType):
    hello = String(name=String(default_value="hoge"))

    def resolve_hello(self, info, name):
        return f'こんにちは {name}さん'


schema = Schema(query=Query)
data = '{hello(name:"jajaja")}'
res = schema.execute(data)
print(res.data)
