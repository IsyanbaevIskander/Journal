from django.db import models
from datetime import date


class Film(models.Model):
    name = models.CharField('Название', max_length=50)
    release_date = models.DateField('Дата релиза')
    photo = models.ImageField(upload_to='photos', verbose_name='Фотография', blank=True, null=True)
    description = models.TextField('Описание')
    director = models.ForeignKey('Director', on_delete=models.CASCADE, verbose_name='Продюсер')
    actors = models.ManyToManyField('Actor', verbose_name='Актёры', related_name='actors')

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.name


class Director(models.Model):
    surname = models.CharField('Фамилия', max_length=50)
    name = models.CharField('Имя',  max_length=50)
    middlename = models.CharField('Отчество', max_length=50, blank=True)
    date_of_birth = models.DateField('Дата рождения', default=date.today(), blank=False)
    sex = models.CharField('Пол', choices=(('Мужчина', 'Мужчина'), ('Женщина', 'Женщина')),
                           max_length=7, default='Мужчина')
    photo = models.ImageField('Фотография', upload_to='photos', blank=True, null=True)

    class Meta:
        verbose_name = 'Продюсер'
        verbose_name_plural = 'Продюсеры'

    def __str__(self) -> str:
        return f'{self.name} {self.surname} {self.middlename}'


class Actor(models.Model):
    surname = models.CharField('Фамилия', max_length=50)
    name = models.CharField('Имя',  max_length=50)
    middlename = models.CharField('Отчество', max_length=50, blank=True)
    date_of_birth = models.DateField('Дата рождения', default=date.today(), blank=False)
    sex = models.CharField('Пол', choices=(('Мужчина', 'Мужчина'), ('Женщина', 'Женщина')),
                           max_length=7, default='Мужчина')
    photo = models.ImageField('Фотография', upload_to='photos', blank=True, null=True)

    class Meta:
        verbose_name = 'Актёр'
        verbose_name_plural = 'Актёры'

    def __str__(self) -> str:
        return f'{self.surname} {self.name} {self.middlename}'