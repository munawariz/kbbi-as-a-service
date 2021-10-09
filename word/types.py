import graphene
from word.models import Meaning, Word
from graphene_django import DjangoObjectType

class MeaningType(DjangoObjectType):
    class Meta:
        model = Meaning
        fields = ('id', 'word', 'pos', 'meaning', 'pos_verbose')

class WordType(DjangoObjectType):
    meaning = MeaningType()
    
    class Meta:
        model = Word
        fields = ('id', 'name', 'base_word', 'pronounciation', 'meaning')

class MeaningInput(graphene.InputObjectType):
    word = graphene.Int()
    pos = graphene.String()
    meaning = graphene.String()

class WordInput(graphene.InputObjectType):
    name = graphene.String()
    base_word = graphene.String()
    pronounciation = graphene.String()
