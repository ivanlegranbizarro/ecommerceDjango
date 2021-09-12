from .models import Categoria


def menu_link(request):
    links = Categoria.objects.all()
    return dict(links=links)
