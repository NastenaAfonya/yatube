from django.contrib import admin
# из файла models импортируем модель Post
from .models import Post


class PostAdmin(admin.ModelAdmin):
    # перечисляем поля, которые должны отображатся в админке
    list_display = ("pk", "text","pub_date", "author")
    #добавляем интрефейс для поиска по тексту постов
    search_fields = ("text",)
    # добавляем возможность фильтрации по дате
    list_filter = ("pub_date",)
    empty_value_display = "-пусто-" #это свойство сработает для всех колонок: где пусто - там будет эта строка
    
    
# при регистрации модели Post источником конфигурации для неё назначаем класс PostAdmin
admin.site.register(Post,PostAdmin)

