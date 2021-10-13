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


class POS(models.Model):
    code = models.CharField(max_length=5)
    verbose = models.CharField(max_length=64, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.verbose


class Meaning(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='meaning')
    pos = models.ManyToManyField(POS, related_name='meaning', blank=True)
    meaning = models.CharField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return f'{self.word.name} ({self.id})'
