from django import template

from ..models import MenuItems

register = template.Library()


def get_menu_item(menu):
    """QuerySet menu item"""
    return MenuItems.objects.filter(
            menu__name=menu,
            menu__published=True,
            published=True,
        )


@register.inclusion_tag('base/tags/base_tag.html', takes_context=True)
def menu_item(context, menu, template='base/menu/menu-item-tag.html'):
    """Вывод меню в шаблон"""
    return {
        "template": template,
        "items": get_menu_item(menu)
    }


@register.simple_tag(takes_context=True)
def for_menu_item(context, menu):
    """Вывод меню без шаблона"""
    return get_menu_item(menu)
