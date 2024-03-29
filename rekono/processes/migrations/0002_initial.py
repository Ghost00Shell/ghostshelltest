# Generated by Django 3.2.12 on 2022-03-20 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tools', '0001_initial'),
        ('processes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='configuration',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tools.configuration'),
        ),
        migrations.AddField(
            model_name='step',
            name='process',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='processes.process'),
        ),
        migrations.AddField(
            model_name='step',
            name='tool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.tool'),
        ),
    ]
