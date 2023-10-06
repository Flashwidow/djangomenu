from django import template
from menuapp.models import Menu,MenuItem

register = template.Library()

@register.simple_tag  
def draw_menu(name):
    menu = Menu.objects.get(name=name)
    items = menu.menuitem_set.filter(parent=None)
    
    html = "<ul>"
    
    for item in items:
        html += "<li>"
        html += f'<a href="{item.url}">{item.title}</a>'
        
        children = item.menuitem_set.all()
        if children:
            html += "<ul>"
            for child in children:
                html += "<li>"    
                html += f'<a href="{child.url}">{child.title}</a>'
                html += "</li>"
            html += "</ul>"
                
        html += "</li>"
        
    html += "</ul>"
    
    return html