from django.db import models

class Mineral(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='collection/media')

    class Meta:
        verbose_name = 'mineral'
        verbose_name_plural = 'minerals'

    def __str__(self):
        return self.name
