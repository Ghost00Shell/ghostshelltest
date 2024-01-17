# Generated by Django 3.2.13 on 2022-04-23 11:29

from django.db import migrations, models
import security.input_validation


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100, unique=True, validators=[security.input_validation.validate_name])),
                ('description', models.TextField(max_length=300, validators=[security.input_validation.validate_text])),
                ('defectdojo_product_id', models.IntegerField(blank=True, null=True, validators=[security.input_validation.validate_number])),
                ('defectdojo_engagement_id', models.IntegerField(blank=True, null=True, validators=[security.input_validation.validate_number])),
                ('defectdojo_engagement_by_target', models.BooleanField(default=False)),
                ('defectdojo_synchronization', models.BooleanField(default=False)),
            ],
        ),
    ]