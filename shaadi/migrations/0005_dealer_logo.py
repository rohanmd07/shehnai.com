# Generated by Django 2.1.5 on 2019-03-10 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shaadi', '0004_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='dealer',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
