from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from django.core.cache import cache
from googletrans import Translator

class FAQ(models.Model):
    LANGUAGES = (
        ('en', 'English'),
        ('hi', 'Hindi'),
        ('bn', 'Bengali'),
    )

    question = models.TextField()
    answer = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_translated_field(self, field_name, lang):
        cache_key = f'faq_{self.id}_{field_name}_{lang}'
        cached = cache.get(cache_key)
        
        if cached:
            return cached
            
        translator = Translator()
        original_text = getattr(self, field_name)
        
        try:
            translation = translator.translate(original_text, dest=lang).text
        except:
            translation = original_text
            
        cache.set(cache_key, translation, timeout=60*60*24)
        return translation

    def question_translated(self, lang):
        return self.get_translated_field('question', lang)

    def answer_translated(self, lang):
        return self.get_translated_field('answer', lang)

    def __str__(self):
        return self.question[:50]

    class Meta:
        verbose_name = _('FAQ')
        verbose_name_plural = _('FAQs')
        ordering = ['-created_at']
