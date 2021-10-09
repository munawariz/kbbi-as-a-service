import graphene
import word.schema as word_schema


class Query(word_schema.Query, graphene.ObjectType):
    pass

class Mutation(word_schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)