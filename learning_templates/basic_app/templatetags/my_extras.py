from django import template

register=template.Library()
&register.filter(name='cut')
def cut(value,arg):
    """
    This cuts.
    """

    return value.replace(arg,'')

register.filter('cut',cut)