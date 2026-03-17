from django import template

register = template.Library()


@register.filter
def timer_mm(seconds):
    return f"{int(seconds) // 60:02d}"


@register.filter
def timer_ss(seconds):
    return f"{int(seconds) % 60:02d}"
