from django_components import component

@component.register('add_to_cart')
class Add_to_cart(component.Component):
    template_name = 'Add_to_cart/template.html'

