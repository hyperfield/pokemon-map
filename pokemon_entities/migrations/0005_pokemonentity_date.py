# Generated by Django 3.1.4 on 2020-12-29 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0004_pokemonentity_pokemon'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonentity',
            name='Date',
            field=models.DateTimeField(default=None),
        ),
    ]
