from django_components import component
from Bun_Store.models import *


@component.register("small")
class Small(component.Component):
    template_name = "small-card/template.html"

    def get_context_data(self, model_instance):

        model_instance = Product.objects.all().filter(offer__gte=90)[:2]

        context = {"model_data": model_instance}

        return context

    class Media:
        css = "small-card/style.css"
        js = "small-card/script.js"
