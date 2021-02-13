from django.db import models
from django.utils.translation import gettext as _

from acquarist.core.models import BaseModel, NULL_OPTION


class Aquariums(BaseModel):
    VOLUME_TYPE_CHOICES = (
        ('liter', _('Liter')),
        ('gallon', _('Gallon')),
    )
    AQUARIUM_TYPE_CHOICES = (
        ('freshwater', _('Freshwater')),
        ('saltwater', _('Saltwater')),
        ('brackish_water', _('Brackish Water')),
    )
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    owner = models.ForeignKey("users.User", verbose_name=_('Owner'), related_name='aquariums', on_delete=models.CASCADE)
    goal = models.ForeignKey("aquariums.Goals", verbose_name=_('Goal'), on_delete=models.CASCADE, **NULL_OPTION)
    volume_type = models.CharField(max_length=255, choices=VOLUME_TYPE_CHOICES, verbose_name=_('Volume Type'))
    aquarium_type = models.CharField(max_length=255, choices=AQUARIUM_TYPE_CHOICES, verbose_name=_('Aquarium Type'))
    length = models.DecimalField(max_digits=5, decimal_places=1, verbose_name=_('Length'))
    height = models.DecimalField(max_digits=5, decimal_places=1, verbose_name=_('Height'))
    width = models.DecimalField(max_digits=5, decimal_places=1, verbose_name=_('Width'))
    tank_volume = models.DecimalField(max_digits=5, decimal_places=1, verbose_name=_('Tank Volume'))
    tank_volume_real = models.DecimalField(max_digits=5, decimal_places=1,
                                           verbose_name=_('Tank Volume Real'), **NULL_OPTION)
    visibility = models.BooleanField(default=True, verbose_name=_('Visibility'))
    start = models.DateField(verbose_name=_('Start'))
    end = models.DateField(verbose_name=_('End'), **NULL_OPTION)

    def __str__(self):
        return _(self.name)


class Goals(BaseModel):
    test_type = models.ForeignKey("aquariums.TestTypes", verbose_name=_('Test Type'), on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=_('Amount'))

    def __str__(self):
        return _(f'{self.test_type.name} ({self.amount} {self.test_type.unit})')


class Tests(BaseModel):
    aquarium = models.ForeignKey("aquariums.Aquariums", verbose_name=_('Aquarium'), on_delete=models.CASCADE)
    test_type = models.ForeignKey("aquariums.TestTypes", verbose_name=_('Test Type'), on_delete=models.PROTECT)
    brand = models.CharField(max_length=250, verbose_name=_('Brand'))
    amount = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=_('Amount'))
    date_execution = models.DateTimeField(verbose_name=_('Date Execution'))

    def __str__(self):
        return _(f'{self.test_type.name} ({self.amount} {self.test_type.unit})')


class Equipament(BaseModel):
    aquarium = models.ForeignKey("aquariums.Aquariums", verbose_name=_('Aquarium'), on_delete=models.CASCADE)
    equipament_type = models.ForeignKey("aquariums.EquipamentTypes",
                                        verbose_name=_('Equipament Type'), on_delete=models.PROTECT)
    brand = models.CharField(max_length=250, verbose_name=_('Brand'))
    amount = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=_('Amount'))
    value_payed = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=_('Value Payed'), **NULL_OPTION)

    def __str__(self):
        return _(f'{self.amount} - {self.equipament_type.name} ({self.brand})')


class EvolutionPhotos(BaseModel):
    aquarium = models.ForeignKey("aquariums.Aquariums", verbose_name=_('Aquarium'), on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name=_('Photo'))
    date_execution = models.DateField(verbose_name=_('Date Execution'))

    def __str__(self):
        return self.date_execution


class TestTypes(BaseModel):
    name = models.CharField(max_length=150, verbose_name=_('Name'))
    unit = models.CharField(max_length=5, verbose_name=_('Unit'))

    def __str__(self):
        return _(f'{self.name}/{self.unit}')


class EquipamentTypes(BaseModel):
    name = models.CharField(max_length=150, verbose_name=_('Name'))

    def __str__(self):
        return _(self.name)
