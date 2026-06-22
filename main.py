import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import (Genre, Actor)


def main() -> QuerySet:
    genre = Genre.objects.all()
    actor = Actor.objects.all()
    for genres in genre:
        genre = Genre.objects.create(name={genres.name})

    for actors in actor:
        actor = Actor.objects.create(
            first_name={actors.first_name}, last_name={actors.last_name}
        )

    genre = Genre.objects.get(name="Dramma")
    genre.name = "Drama"
    genre.save()

    actor = Actor.objects.get(last_name="Klooney")
    actor.last_name = "Clooney"
    actor.save()

    actor = Actor.objects.get(first_name="Kianu", last_name="Reaves")
    actor.first_name = "Keanu"
    actor.last_name = "Reeves"
    actor.save()

    genre = Genre.objects.get(name="Action")
    genre.delete()

    actor = Actor.objects.filter(first_name="Scarlett")
    actor.delete()

    for actors in actor:
        return Actor.objects.filter(last_name="Smith").order_by("first_name")
