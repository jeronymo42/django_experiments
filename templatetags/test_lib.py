from django import template

register = template.Library()


@register.filter(name="splitl")
# Из Hello_World получаем Hello World
def splitl_func(value: str):
    return value.replace("_", " ")
