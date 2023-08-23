from django.db import models
from . import catalog as ct, GR, EN

class Category(models.Model):
  choices = ct.get_pr_choices()

  name = models.CharField('Name', max_length=32, choices=choices, unique=True, primary_key=True)
  name_gr_s = models.CharField('Greek singular', max_length=32, blank=True)
  name_gr_pl = models.CharField('Greek plural', max_length=32, blank=True)
  name_en_s = models.CharField('English singular', max_length=32, blank=True)
  name_en_pl = models.CharField('English plural', max_length=32, blank=True)

  def __str__(self):
      return self.name_en_s

  def save(self, *args, **kwargs):
      self.name_gr_s = ct.get_pr_trans(self.name, GR, False)
      self.name_gr_pl = ct.get_pr_trans(self.name, GR, True)
      self.name_en_s = ct.get_pr_trans(self.name, EN, False)
      self.name_en_pl = ct.get_pr_trans(self.name, EN, True)
      super().save(*args, **kwargs)

  class Meta:
      verbose_name = 'category'
      verbose_name_plural = 'categories'