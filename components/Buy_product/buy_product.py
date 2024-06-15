from django_components import component

@component.register('buy_product')
class Buy_Product(component.Component):
    template_name = 'Buy_product/template.html'