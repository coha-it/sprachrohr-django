# Generated by Django 3.0.8 on 2020-07-23 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_author_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.CharField(choices=[('A', 'Audio-Blogpost'), ('S', 'Text-Blogpost')], max_length=1),
        ),
    ]
