from django.db import models

import uuid
from stdimage import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    created = models.DateField('Created', auto_now_add=True)
    modified = models.DateField('Last Modified', auto_now=True)
    active = models.BooleanField('Is Active?', default=True)

    class Meta:
        abstract = True


class Service(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Gear'),
        ('lni-stats-up', 'Graphic'),
        ('lni-users', 'Users'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Rocket'),
    )
    service = models.CharField('Service', max_length=100)
    description = models.TextField('Description', max_length=200)
    icon = models.CharField('Icon', max_length=12, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.service


class Role(Base):
    role = models.CharField('Role', max_length=100)

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.role


class Employee(Base):
    name = models.CharField('Name', max_length=100)
    role = models.ForeignKey('core.Role', verbose_name='Role', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    image = StdImageField('Image', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return self.name


class Feature(Base):
    ICON_CHOICES = (
        ('lni-cog', 'Gear'),
        ('lni-layers', 'Design'),
        ('lni-leaf', 'Leaf'),
        ('lni-laptop-phone', 'Device'),
        ('lni-rocket', 'Rocket'),
    )

    feature = models.CharField('Feature', max_length=100)
    description = models.TextField('Description', max_length=200)
    icon = models.CharField('Icon', max_length=20, choices=ICON_CHOICES)
    side = models.CharField('Side', max_length=5, default='left')

    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'

    def __str__(self):
        return self.feature