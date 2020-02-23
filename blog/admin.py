from django.contrib import admin


from .models import Category, Comment, Post, Tag
from pages.admin import ActionPublish

admin.site.register(Tag)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Комментарии блога"""
    list_display = ("id", "author",)
    list_display_links = ("author",)
    list_filter = ("post",)
    readonly_fields = ("text", "create_data", "post", "author",)


@admin.register(Category)
class CategoryAdmin(ActionPublish):
    """Категории блога"""
    actions = ['unpublish', 'publish']
    list_display = ("id", "name", "parent", "slug", "sort", "published", "paginated",)
    list_display_links = ("name",)
    list_filter = ("parent",)
    # fieldsets =
    # inlines =


class CommentsInline(admin.StackedInline):
    model = Comment
    extra = 1                                                                   # Вывод одного пустого поля комментариев


@admin.register(Post)
class PostAdmin(ActionPublish):
    """Посты блога"""
    actions = ['unpublish', 'publish']
    inlines = [CommentsInline]
    filter_horizontal = ("tags",)
    fieldsets = (
        ('Контент', {
            'fields': ('author', 'title', 'subtitle', 'slug'),
        }),
        ('Контент 2', {
            'fields': ('mini_text', 'text', 'image'),
        }),
        ('Даты', {
            'fields': ('edit_date', 'published_date'),
        }),
        ('Завязки', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('tags', 'category'),
        }),
        ('Настройки', {
            'classes': ('collapse',),                                           # Делает кнопку скрыть и показать
            'fields': ('template', 'published', 'status', 'sort', 'viewed'),
        }),
    )


admin.site.site_title = "Проект созданный на django 2.0"
admin.site.site_header = "Проект созданный на django 2.0"