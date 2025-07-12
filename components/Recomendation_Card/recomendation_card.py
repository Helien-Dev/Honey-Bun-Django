from django_components import component
from Bun_Store.models import *

@component.register("recomendation_card")
class Recomendation_Card(component.Component):
    template_name = "Recomendation_Card/template.html"

    def get_context_data(self, model_instance):

        model_instance = Product.objects.all().order_by("?")[:3]

        context = {"model_data": model_instance}

        return context

    class Media:
        css = "Recomendation_Card/style.css"
        js = "Recomendation_Card/script.js"


