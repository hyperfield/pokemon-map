# Generated by Django 3.1.4 on 2020-12-29 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0005_pokemonentity_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='Date',
            new_name='appeared_at',
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(default=None),
        ),
    ]
