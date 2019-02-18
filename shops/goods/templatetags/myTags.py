#coding utf-8
#mojun
from django import template
import time
register = template.Library()

@register.simple_tag()
def today(format):
    return time.strftime(format)

#括号可以传参数
@register.filter()
def cf(value,arg):
    print(value,arg)
    return value*arg


