from django_components import component

@component.register('see_product')
class See_Product(component.Component):
    template_name = 'See_product/template.html'