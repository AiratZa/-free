from .models import Category, Shop


def category_context_proccessor(request):
    context = {}
    context ['categories'] = Category.objects.all()
    return context

def shop_context_proccessor(request):
    context = {}
    context ['shops'] = Shop.objects.all()
    return context

