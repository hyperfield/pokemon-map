from django.db import models


class Pokemon(models.Model):
    """Покемон"""
    title = models.CharField(max_length=20, verbose_name="Название по-русски")
    title_en = models.CharField(max_length=20,
                                verbose_name="Название по-английски",
                                blank=True)
    title_jp = models.CharField(max_length=20,
                                verbose_name="Название по-японски",
                                blank=True)
    photo = models.ImageField(upload_to='pokemons', verbose_name="Картинка",
                              null=True)
    description = models.TextField(null=True, verbose_name="Описание")
    evolves_from = "Из кого эволюционирует"
    previous_evolution = models.ForeignKey("self", verbose_name=evolves_from,
                                           on_delete=models.SET_NULL,
                                           related_name='next_evolutions',
                                           null=True, blank=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    """Сущность покемона"""
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE,
                                default=None, verbose_name="Покемон")
    lat = models.FloatField(max_length=7, verbose_name="Широта")
    lon = models.FloatField(max_length=7, verbose_name="Долгота")
    appeared_at = models.DateTimeField(default=None, null=True,
                                       verbose_name="Когда появился")
    disappeared_at = models.DateTimeField(default=None, null=True,
                                          verbose_name="Когда исчезает")
    level = models.IntegerField(default=1, verbose_name="Уровень")
    health = models.IntegerField(default=100, verbose_name="Здоровье")
    strength = models.IntegerField(default=20, verbose_name="Сила")
    defense = models.IntegerField(default=20, verbose_name="Щит")
    stamina = models.IntegerField(default=20, verbose_name="Выносливость")

    def __str__(self):
        return f"{self.pokemon.title} {self.id}"
