from django.db import models
from datetime import date


class Subject(models.Model):
    name = models.CharField('Название', max_length=30)

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self) -> str:
        return f'{self.name}'


class Teacher(models.Model):
    name = models.CharField('Имя', max_length=20)
    surname = models.CharField('Фамилия', max_length=20)
    middlename = models.CharField('Отчество', max_length=20, blank=True)
    date_of_birth = models.DateField('Дата рождения', default=date.today())
    sex = models.CharField('Пол', max_length=1, choices=(('М', 'М'), ('Ж', 'Ж')), default='М')
    photo = models.ImageField('Фотография', upload_to='pictures', null=True, blank=True)
    subjects = models.ManyToManyField(Subject, verbose_name='Преподаваемые предметы')

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

    def __str__(self) -> str:
        return f'{self.surname} {self.name} {self.middlename}'


class Parent(models.Model):
    name = models.CharField('Имя', max_length=20)
    surname = models.CharField('Фамилия', max_length=20)
    middlename = models.CharField('Отчество', max_length=20, blank=True)
    sex = models.CharField('Пол', max_length=1, choices=(('М', 'М'), ('Ж', 'Ж')), default='М')
    photo = models.ImageField('Фотография',upload_to='pictures', blank=True)

    class Meta:
        verbose_name = 'Родитель'
        verbose_name_plural = 'Родители'

    def __str__(self):
        return f'{self.surname} {self.name} {self.middlename}'


class Group(models.Model):
    number = models.PositiveIntegerField('Номер', choices=tuple((i, i) for i in range(1, 12)), default=1)
    letter = models.CharField('Буква', max_length=1, default='')
    subjects = models.ManyToManyField(Subject, verbose_name='Изучаемые предметы')

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'

    def __str__(self):
        return f'{self.number} {self.letter} класс'


class Student(models.Model):
    name = models.CharField('Имя',  max_length=20)
    surname = models.CharField('Фамилия', max_length=20)
    middlename = models.CharField('Отчество', max_length=20, blank=True)
    date_of_birth = models.DateField('Дата рождения', default=date.today(), blank=False)
    sex = models.CharField('Пол', max_length=1, choices=(('М', 'М'), ('Ж', 'Ж')), default='М')
    parents = models.ManyToManyField(Parent, verbose_name='Родители')
    photo = models.ImageField('Фотография', upload_to='pictures', blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, default='', verbose_name='Класс')

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

    def __str__(self) -> str:
        return f'{self.name} {self.surname}'