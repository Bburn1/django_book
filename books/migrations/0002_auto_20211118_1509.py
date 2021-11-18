# Generated by Django 3.2.9 on 2021-11-18 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ratingstar',
            options={'ordering': ['-value'], 'verbose_name': 'Звезда рейтинга', 'verbose_name_plural': 'Звёзды рейтинга'},
        ),
        migrations.AddField(
            model_name='book',
            name='ebook',
            field=models.FileField(blank=True, upload_to='ebooks/', verbose_name='Електронная книга'),
        ),
    ]