# models.py

# -*- coding: utf-8 -*-
# Defines the database models for the French learning application.

from django.db import models

class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    name_english = models.CharField(max_length=100, verbose_name="English Name")
    name_hebrew = models.CharField(max_length=100, verbose_name="שם בעברית")
    name_french = models.CharField(max_length=100, verbose_name="French Name")

    # String representation of the model, using English name for display
    def __str__(self):
        return self.name_english

    # Metadata options for the Lesson model
    class Meta:
        verbose_name = "Lesson" # Singular name for an instance of this model
        verbose_name_plural = "Lessons" # Plural name for instances of this model


class Word(models.Model):
    id = models.AutoField(primary_key=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='words')
    # Searchable key associated with the word (used for image searches, etc.)
    word_key = models.CharField(max_length=50, verbose_name="word to search")
    word_english = models.CharField(max_length=50, verbose_name="English Word")
    word_hebrew = models.CharField(max_length=50, verbose_name="מילה בעברית")
    word_french = models.CharField(max_length=50, verbose_name="French Word")

    # String representation of the model, using English word for display
    def __str__(self):
        return self.word_english

    class Meta:
        verbose_name = "Word" # Singular name for an instance of this model
        verbose_name_plural = "Words" # Plural name for instances of this model
