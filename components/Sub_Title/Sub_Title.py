from django_components import component
from Bun_Store.models import *

@component.register("sub_title")
class Sub_tile(component.Component):
    template_name = "Sub_Tile/template.html"
    class Media:
        css = 'Sub_Title/style.css'
        js = 'Sub_Ttile'