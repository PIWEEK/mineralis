from django.db import models

KINDS = (
    ('ELEMENTS', 'Elementos nativos'),
    ('SULFIDES', 'Sulfuros y sulfosales'),
    ('HALIDES', 'Halogenuros'),
    ('OXIDES', 'Óxidos e hidroxidos'),
    ('CARBONATES', 'Carbonatos y nitratos'),
    ('BORATES', 'Boratos'),
    ('SULFATES', 'Sulfatos, cromatos, molibdatos y wolframatos'),
    ('PHOSPHATES', 'Fosfatos, arseniatos y vanadatos'),
    ('SILICATES', 'Silicatos'),
    ('ORGANIC', 'Sustancias orgánicas')
)

class Mineral(models.Model):
    name = models.CharField(max_length=255)
    crystalization_system = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    mineral_deposit = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    chemical_composition = models.CharField(blank=True, null=True, max_length=255)
    strength = models.CharField(max_length=255, blank=True, null=True)
    kind = models.CharField(max_length=255, blank=True, null=True, choices=KINDS)
    thumbnail = models.ImageField(blank=True, null=True, upload_to='collection/media')

    class Meta:
        verbose_name = 'mineral'
        verbose_name_plural = 'minerals'

    def __str__(self):
        return self.name

class Image(models.Model):
    mineral = models.ForeignKey('Mineral', related_name='images')
    image = models.ImageField(blank=True, null=True, upload_to='collection/media')

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'

    def __str__(self):
        return self.image.name
