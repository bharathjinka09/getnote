# Generated by Django 3.0.5 on 2020-05-01 14:56

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='text',
            field=django_cryptography.fields.encrypt(models.TextField(blank=True, null=True)),
        ),
    ]
