import init_django_orm  # noqa: F401

from django.db.models import QuerySet


def main() -> QuerySet:
    western = Genre.objects.create(name="Western")
    action = Genre.objects.create(name="Action")
    dramma = Genre.objects.create(name="Dramma")
    george_klooney = Actor.objects.create(first_name="George", last_name="Klooney")
    kianu_reeves = Actor.objects.create(first_name="Kianu", last_name="Reeves")
    scarlet_keegan = Actor.objects.create(first_name="Scarlet", last_name="Keegan")
    will_smith = Actor.objects.create(first_name="Will", last_name="Smith")
    jaden_smith = Actor.objects.create(first_name="Jaden", last_name="Smith")
    scarlett_johansson = Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    genre = Genre.objects.get(name="Dramma")
    genre.name = "Drama"
    genre.save()
    actor = Genre.objects.get(last_name="Klooney")
    actor.last_name = "Clooney"
    actor.save()
    actor = Genre.objects.get(first_name="Kianu")
    actor.first_name = "Keanu"
    actor.save
    actor = Genre.objects.get(last_name="Reeves")
    actor.last_name = "Reaves"
    actor.save()

    Genre.objects.get(name="Action").delete()
    Actor.objects.get(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")