from django import template

register = template.Library()


# 使用说明 {% load my_tags %}

@register.filter()
def to_int(value):
    return int(value)


@register.simple_tag
def hello(*args):
    return "hello " + " ".join(str(args))
