from django.shortcuts import render
from .models import Comentario
from django.db.models import Avg

# Create your views here.


def Blog(request):
    comentarios = Comentario.objects.all()
    avg_rating = comentarios.aggregate(Avg("rating"))["rating__avg"]

    return render(
        request,
        "blog/blog.html",
        {
            "comentarios": comentarios,
            "avg_rating": avg_rating,
        },
    )
