# Generated by Django 3.2.8 on 2021-11-05 10:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avtor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('age', models.DateField(blank=True, default=datetime.date.today, help_text='Дата', verbose_name='Дата рождения')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(blank=True, upload_to='avtors/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы ',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Назва')),
                ('description', models.TextField(verbose_name='Опис')),
                ('poster', models.ImageField(blank=True, upload_to='books/', verbose_name='Обложка')),
                ('year', models.PositiveSmallIntegerField(blank=True, default=2021, verbose_name='Год написания')),
                ('isbn', models.CharField(blank=True, help_text='Международный стандартный книжный номер', max_length=150, verbose_name='ISBN')),
                ('pages', models.PositiveIntegerField(blank=True, default=0, verbose_name='Страницы')),
                ('language', models.CharField(blank=True, max_length=150, verbose_name='Язык')),
                ('world_publishing', models.CharField(blank=True, max_length=50, verbose_name='Дата издания кнгиги')),
                ('url', models.SlugField(max_length=150, unique=True)),
                ('draft', models.BooleanField(default=False, verbose_name='Черновик')),
                ('avtors', models.ManyToManyField(related_name='book_avtor', to='books.Avtor', verbose_name='Авторы')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Категория')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('url', models.SlugField(max_length=150)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Страна')),
                ('image', models.ImageField(blank=True, upload_to='country/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('url', models.SlugField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Publishing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, upload_to='publishing/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Издательство',
                'verbose_name_plural': 'Издательства',
            },
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveSmallIntegerField(default=0, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Звезда рейтинга',
                'verbose_name_plural': 'Звёзды рейтинга',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=150, verbose_name='Мся')),
                ('text', models.TextField(max_length=3000, verbose_name='Сообщение')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book', verbose_name='Кнгиа')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.reviews', verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'отзыв',
                'verbose_name_plural': 'отзывы',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=25, verbose_name='IP')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book', verbose_name='Книга')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.ratingstar', verbose_name='Звезда')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинги',
            },
        ),
        migrations.CreateModel(
            name='BookShots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='book_shots/', verbose_name='Изображение')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book', verbose_name='Книга')),
            ],
            options={
                'verbose_name': 'Страница книги',
                'verbose_name_plural': 'Страницы книги',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.category', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='book',
            name='countrys',
            field=models.ManyToManyField(blank=True, max_length=50, related_name='book_country', to='books.Country', verbose_name='Страна'),
        ),
        migrations.AddField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(to='books.Genre', verbose_name='Жанры'),
        ),
        migrations.AddField(
            model_name='book',
            name='publishings',
            field=models.ManyToManyField(blank=True, related_name='book_publishing', to='books.Publishing', verbose_name='Издательства'),
        ),
    ]
