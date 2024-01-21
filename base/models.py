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
