import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Actor, Genre


def main() -> QuerySet:
    for name in ["Western", "Action", "Dramma"]:
        Genre.objects.create(name=name)

    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlet", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    for first_name, last_name in actors:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    genre = Genre.objects.get(name="Dramma")
    genre.name = "Drama"
    genre.save()
    actor = Actor.objects.get(last_name="Klooney")
    actor.last_name = "Clooney"
    actor.save()
    actor = Actor.objects.get(first_name="Kianu")
    actor.first_name = "Keanu"
    actor.save()
    actor = Actor.objects.get(last_name="Reaves")
    actor.last_name = "Reeves"
    actor.save()

    Genre.objects.get(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
