# Generated by Django 5.0.1 on 2024-04-07 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vyas', '0003_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
