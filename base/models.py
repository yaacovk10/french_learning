# models.py

# -*- coding: utf-8 -*-

from django.db import models

class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    name_english = models.CharField(max_length=100, verbose_name="English Name")
    name_hebrew = models.CharField(max_length=100, verbose_name="שם בעברית")
    name_french = models.CharField(max_length=100, verbose_name="French Name")

    def __str__(self):
        return self.name_english

    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"

class Word(models.Model):
    id = models.AutoField(primary_key=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='words')
    word_key = models.CharField(max_length=50, verbose_name="word to search")
    word_english = models.CharField(max_length=50, verbose_name="English Word")
    word_hebrew = models.CharField(max_length=50, verbose_name="מילה בעברית")
    word_french = models.CharField(max_length=50, verbose_name="French Word")

    def __str__(self):
        return self.word_english

    class Meta:
        verbose_name = "Word"
        verbose_name_plural = "Words"
