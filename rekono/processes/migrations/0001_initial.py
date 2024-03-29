# Generated by Django 3.2.12 on 2022-03-20 11:45

from django.db import migrations, models
import security.input_validation


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100, unique=True, validators=[security.input_validation.validate_name])),
                ('description', models.TextField(max_length=300, validators=[security.input_validation.validate_text])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.IntegerField(default=1, validators=[security.input_validation.validate_number])),
            ],
        ),
    ]
