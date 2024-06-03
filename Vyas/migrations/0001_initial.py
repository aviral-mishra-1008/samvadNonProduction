# Generated by Django 4.1.5 on 2023-03-11 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('email_id', models.CharField(default='', max_length=1000)),
                ('heading', models.CharField(default='An article', max_length=100)),
                ('estimated_time', models.IntegerField(default=0, null=True)),
                ('article', models.CharField(default='', max_length=1000000000000000000)),
                ('image', models.ImageField(default='', upload_to='static/')),
                ('branch', models.CharField(default='', max_length=100)),
                ('year', models.IntegerField(default=0, null=True)),
                ('slug', models.CharField(max_length=130)),
            ],
        ),
    ]
