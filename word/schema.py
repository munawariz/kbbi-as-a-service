import graphene
from word.types import MeaningType, WordType
from word.models import Word
from word.mutation import CreateMeaning, CreateWord, DeleteMeaning, DeleteWord


class Query(graphene.ObjectType):
    words = graphene.List(WordType)
    word = graphene.Field(WordType, name=graphene.String(required=True))

    def resolve_words(self, info):
        return Word.objects.prefetch_related('meaning').all()

    def resolve_word(self, info, name):
        try:
            return Word.objects.get(name=name)
        except Word.DoesNotExist:
            return None


class Mutation(graphene.ObjectType):
    create_word = CreateWord.Field()
    create_meaning = CreateMeaning.Field()
    delete_word = DeleteWord.Field()
    delete_meaning = DeleteMeaning.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)