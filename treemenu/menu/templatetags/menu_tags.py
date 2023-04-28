from django import template
from django.urls import reverse
from ..models import MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    menu_items = MenuItem.objects.filter(parent__isnull=True).order_by('order')
    active_url = request.path
    active_item = None
    menu_html = ''
    
    for item in menu_items:
        if item.name != menu_name:
            continue
        menu_html += '<li class="menu-item'
        if active_url.startswith(item.url):
            menu_html += ' active'
            active_item = item
        menu_html += '">'
        if item.url:
            menu_html += '<a href="%s">%s</a>' % (item.url, item.name)
        else:
            menu_html += item.name
        children = item.children.order_by('order')
        if children:
            menu_html += '<ul class="sub-menu">'
            for child in children:
                menu_html += '<li class="menu-item'
                if active_url.startswith(child.url):
                    menu_html += ' active'
                    active_item = child
                menu_html += '"><a href="%s">%s</a></li>' % (child.url, child.name)
            menu_html += '</ul>'
        menu_html += '</li>'
    context['active_item'] = active_item
    return menu_html
