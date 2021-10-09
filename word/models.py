from django.db import models

class Word(models.Model):
    name = models.CharField(max_length=255)
    base_word = models.CharField(max_length=255, null=True, blank=True)
    pronounciation = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        self.base_word = self.base_word.lower() if self.base_word else self.base_word
        self.pronounciation = self.pronounciation.lower() if self.pronounciation else self.pronounciation
        return super(Word, self).save(*args, **kwargs)


class Meaning(models.Model):
    # Short for part of speech
    POS = [
        ('noun', 'Kata Benda'),
        ('pronoun', 'Kata Ganti'),
        ('verb', 'Kata Kerja'),
        ('adjective', 'Kata Sifat'),
        ('adverb', 'Kata Keterangan'),
        ('preposition', 'Kata Depan'),
        ('conjunction', 'Kata Hubung'),
        ('interjection', 'Kata Seru')
    ]

    word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='meaning')
    pos = models.CharField(max_length=20, choices=POS, null=True, blank=True)
    pos_verbose = models.CharField(max_length=64, null=True, blank=True)
    meaning = models.CharField(max_length=1024)

    def __str__(self):
        return f'{self.word.name} ({self.pos})'

    def save(self, *args, **kwargs):
        self.pos_verbose = self.get_pos_display()
        return super(Meaning, self).save(*args, **kwargs)
