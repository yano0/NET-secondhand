# Generated by Django 3.2 on 2022-09-12 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0006_alter_contents_book_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contents',
            name='book_id',
            field=models.IntegerField(unique=True),
        ),
    ]