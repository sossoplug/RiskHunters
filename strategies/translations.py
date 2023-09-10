from modeltranslation.translator import register, TranslationOptions, translator
from strategies.models import Pros, Cons, GrowthModel

@register(Pros)
class ProsTranslationOptions(TranslationOptions):
    fields = ('description', 'name',)

@register(Cons)
class ConsTranslationOptions(TranslationOptions):
    fields = ('description', 'name',)

@register(GrowthModel)
class GrowthModelTranslationOptions(TranslationOptions):
    fields = ('description', 'name', 'nickname',)