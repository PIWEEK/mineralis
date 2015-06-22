from django.db import models

KINDS = (
    ('ELEMENTS', 'Elements'),
    ('SULFIDES', 'Sulfides and sulfosalts'),
    ('HALIDES', 'Halides'),
    ('OXIDES', 'Oxides, hydroxides and arsenites'),
    ('CARBONATES', 'Carbonates and nitrates'),
    ('BORATES', 'Borates'),
    ('SULFATES', 'Sulfates, chromates, molybdates and tungstates'),
    ('PHOSPHATES', 'Phosphates, arsenates and vanadates'),
    ('SILICATES', 'Silicates'),
    ('ORGANIC', 'Organic compounds')
)

class Mineral(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    chemical_composition = models.TextField(blank=True, null=True)
    strength = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='collection/media')
    kind = models.CharField(max_length=255, blank=True, null=True, choices=KINDS)

    class Meta:
        verbose_name = 'mineral'
        verbose_name_plural = 'minerals'

    def __str__(self):
        return self.name
