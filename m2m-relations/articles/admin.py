from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from articles.models import Article, Section, ArticleSection


class ArticleSectionInlineFormset(BaseInlineFormSet):
    def clean(self):
        k = 0
        for form in self.forms:
            if form.cleaned_data:
                if form.cleaned_data['is_main']:
                    k += 1
        if k == 0:
            raise ValidationError('Укажите основной раздел.')
        if k > 1:
            raise ValidationError('Основной раздел может быть только один!')
        return super().clean()


class ArticleSectionInline(admin.TabularInline):
    model = ArticleSection
    extra = 1
    formset = ArticleSectionInlineFormset



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleSectionInline]


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass

