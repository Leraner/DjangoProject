from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Page


class ActionPublish(admin.ModelAdmin):
    """Action для публикации и снятия с публикации"""

    def unpublish(self, request, queryset):
        """Снять с публикации"""
        rows_updated = queryset.update(published=False)
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)

    unpublish.short_description = "Снять с публикации"
    unpublish.allowed_permissions = ('change',)     # При каких правах это можно делать

    def publish(self, request, queryset):
        """Опубликовать"""
        rows_updated = queryset.update(published=True)
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)

    publish.short_description = "Опубликовать"
    publish.allowed_permissions = ('change',)


class PagesAdminForm(forms.ModelForm):
    """Виджет редактора ckeditor"""
    text = forms.CharField(required=False, label="Контент страницы", widget=CKEditorUploadingWidget())

    class Meta:
        model = Page
        fields = '__all__'


@admin.register(Page)
class PagesAdmin(ActionPublish):
    """Статичные страницы"""
    list_display = ("title", "published", "id")
    list_editable = ("published", )
    list_filter = ("published", "template")
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title", )}     # Автоматом заполняет поле slug на основе title
    form = PagesAdminForm
    actions = ['unpublish', 'publish']              # После регистрации здесь action's будут срабатывать!
    save_on_top = True                              # Сохранение страницы было сверху
    # readonly_fields = ("slug",)                   # readonly_fields - говорит о том, что это поле только для чтения

