import graphene
from word.models import POS, Word, Meaning
from word.types import MeaningType, WordInput, MeaningInput, WordType


class CreateWord(graphene.Mutation):
    class Arguments:
        input = WordInput(required=True)

    word = graphene.Field(WordType)
    code = graphene.Int()

    @staticmethod
    def mutate(self, info, input=None):
        word = Word(
            name=input.name,
            base_word=input.base_word,
            pronounciation=input.pronounciation
        )

        word.save()
        return CreateWord(word=word, code=200)

class DeleteWord(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    message = graphene.String()
    code = graphene.Int()

    @staticmethod
    def mutate(self, info, id=None):
        word = Word.objects.get(id=id)
        if word:
            word.delete()
            return DeleteWord(message='Succcess', code=200)

        return DeleteWord(message='Word Not Found', code=404)


class CreateMeaning(graphene.Mutation):
    class Arguments:
        input = MeaningInput(required=True)

    meaning = graphene.Field(MeaningType)
    code = graphene.String()

    def find_and_add_pos(self, pos):
        pass

    @staticmethod
    def mutate(self, info, input=None):
        word = Word.objects.get(id=input.word)
        meaning = Meaning.objects.create(
            word=word,
            meaning=input.meaning
        )

        pos_id = []
        for pos in input.pos:
            pos_data, created = POS.objects.get_or_create(
                code=pos['code'].lower(),
                defaults={'verbose': pos['verbose'].lower(), 'description': pos['description'].lower()}
            )
            pos_id.append(pos_data.id)    
        meaning.pos.set(pos_id)

        return CreateMeaning(meaning=meaning, code=200)

class DeleteMeaning(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    message = graphene.String()
    code = graphene.Int()

    @staticmethod
    def mutate(self, info, id=None):
        meaning = Meaning.objects.get(id=id)
        if meaning:
            meaning.delete()
            return DeleteMeaning(message='Succcess', code=200)

        return DeleteMeaning(message='Meaning Not Found', code=404)
