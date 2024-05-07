# Generated by Django 4.2.11 on 2024-05-07 12:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11)], default=1, verbose_name='Номер')),
                ('letter', models.CharField(default='', max_length=1, verbose_name='Буква')),
            ],
            options={
                'verbose_name': 'Класс',
                'verbose_name_plural': 'Классы',
            },
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('surname', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('middlename', models.CharField(blank=True, max_length=20, verbose_name='Отчество')),
                ('sex', models.CharField(choices=[('М', 'М'), ('Ж', 'Ж')], default='М', max_length=1, verbose_name='Пол')),
                ('photo', models.ImageField(blank=True, upload_to='pictures', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Родитель',
                'verbose_name_plural': 'Родители',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('surname', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('middlename', models.CharField(blank=True, max_length=20, verbose_name='Отчество')),
                ('date_of_birth', models.DateField(default=datetime.date(2024, 5, 7), verbose_name='Дата рождения')),
                ('sex', models.CharField(choices=[('М', 'М'), ('Ж', 'Ж')], default='М', max_length=1, verbose_name='Пол')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='pictures', verbose_name='Фотография')),
                ('subjects', models.ManyToManyField(to='core.subject', verbose_name='Преподаваемые предметы')),
            ],
            options={
                'verbose_name': 'Учитель',
                'verbose_name_plural': 'Учителя',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('surname', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('middlename', models.CharField(blank=True, max_length=20, verbose_name='Отчество')),
                ('date_of_birth', models.DateField(default=datetime.date(2024, 5, 7), verbose_name='Дата рождения')),
                ('sex', models.CharField(choices=[('М', 'М'), ('Ж', 'Ж')], default='М', max_length=1, verbose_name='Пол')),
                ('photo', models.ImageField(blank=True, upload_to='pictures', verbose_name='Фотография')),
                ('group', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='core.group', verbose_name='Класс')),
                ('parents', models.ManyToManyField(to='core.parent', verbose_name='Родители')),
            ],
            options={
                'verbose_name': 'Ученик',
                'verbose_name_plural': 'Ученики',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='subjects',
            field=models.ManyToManyField(to='core.subject', verbose_name='Изучаемые предметы'),
        ),
    ]
