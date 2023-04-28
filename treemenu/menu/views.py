from django.shortcuts import render
from django.views import View
from .templatetags.menu_tags import draw_menu
from .models import MenuItem
# Create your views here.

class MenuView(View):
    def get(self, request):
        context = {
            'menu_html': draw_menu({'request': request}, 'main_menu')
        }
        return render(request, 'index.html', context)

    

class MenuTestView(View):
    def get(self, request):
        c = MenuItem.objects.all()
        context = {
            'menu': c
        }
        return render(request, 'test.html', context)
   