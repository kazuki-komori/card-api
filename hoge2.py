from graphene_file_upload.scalars import Upload
import graphene


class UploadMutation(graphene.Mutation):
    class Arguments:
        file = Upload(required=True)
    success = graphene.Boolean()

    def mutate(self, info, file):
        return UploadMutation(success=True)


# class Query(graphene.ObjectType):
#     data = UploadMutation.Field()
