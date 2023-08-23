from django.db import models
from . import save_langs

class Technology(models.Model):
    name_gr = models.CharField('Name (gr)', max_length=32, blank=True)
    name_en = models.CharField('Name (en)', max_length=32, unique=True)
    image = models.ImageField('Photo', upload_to='images')
    desc_gr = models.TextField('Desc (gr)')
    desc_en = models.TextField('Desc (en)')
    
    def get_absolute_url(self):
        return '/media/images/' + self.image.name.split('/')[-1]

    def save(self, *args, **kwargs):
        self.name_gr, self.name_en = save_langs(self.name_gr, self.name_en)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'technology {self.name_en}'

    class Meta:
        verbose_name = 'technology'
        verbose_name_plural = 'technologies'

class LayerMattress(models.Model):
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    product = models.ForeignKey('Mattress', on_delete=models.CASCADE)

    def __str__(self):
        return f'mattres layer {self.product} with technology {self.technology}'

class LayerPillow(models.Model):
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    product = models.ForeignKey('Pillow', on_delete=models.CASCADE)

    def __str__(self):
        return f'pillow layer {self.product} with technology {self.technology}'

class LayerMattressPad(models.Model):
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    product = models.ForeignKey('MattressPad', on_delete=models.CASCADE)

    def __str__(self):
        return f'matresspad layer {self.product} with technology {self.technology}'