from django_components import component
from Bun_Store.models import *

@component.register('title')
class Title(component.Component):
    template_name = 'Title/template.html'
    
    class Media:
        css = 'Title/style.css'
        js = 'Title/script.js'
