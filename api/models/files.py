from django.db import models

class Image(models.Model):
    folder = 'products'
    image = models.ImageField('Photo', upload_to=folder)

    def __str__(self):
        name = self.get_name()
        if self.is_shortcut():
            name = name.replace('_', ' ')
            name += ' shortcut'
        else:
            name = name.replace('_', ' ')
            name = ' '.join(name.split(' ')[:-1]) + ' № ' + name.split(' ')[-1]

        return name

    def is_shortcut(self):
        return not self.get_name().split('_')[-1].isdigit()
    
    def get_absolute_url(self):
        return f'/media/{self.folder}/{self.get_name()}.jpg'

    def get_name(self):
        return self.image.name.split('/')[-1].split('.')[0] #products/[name].jpg -> [name]

    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photos'
