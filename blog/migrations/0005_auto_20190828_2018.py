# Generated by Django 2.2.3 on 2019-08-28 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190828_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entertainmentmodel',
            name='author',
            field=models.TextField(default='Sanchit Gupta', max_length=100),
        ),
    ]
