from django import template

register = template.Library()
@register.filter(name = 'cutValue')
def cutVal(value,arg):
    """
        this cuts all values of 'arg' from string
    """
    return value.replace(arg,'')

#register.filter('cutValue',cutVal)
