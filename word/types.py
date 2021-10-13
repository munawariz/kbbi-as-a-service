import graphene
from word.models import Meaning, POS, Word
from graphene_django import DjangoObjectType

class POSType(DjangoObjectType):
    class Meta:
        model = POS
        fields = ('id', 'code', 'verbose', 'description')


class MeaningType(DjangoObjectType):
    pos = POSType()
    class Meta:
        model = Meaning
        fields = ('id', 'word', 'pos','meaning')

class WordType(DjangoObjectType):
    meaning = MeaningType()
    
    class Meta:
        model = Word
        fields = ('id', 'name', 'base_word', 'pronounciation', 'meaning')

class POSInput(graphene.InputObjectType):
    code = graphene.String()
    verbose = graphene.String()
    description = graphene.String()

class MeaningInput(graphene.InputObjectType):
    word = graphene.Int()
    pos = graphene.List(POSInput)
    meaning = graphene.String()

class WordInput(graphene.InputObjectType):
    name = graphene.String()
    base_word = graphene.String()
    pronounciation = graphene.String()
