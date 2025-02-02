from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class FAQViewSet(viewsets.ModelViewSet):
    serializer_class = FAQSerializer
    queryset = FAQ.objects.all().order_by('-created_at')

    @method_decorator(cache_page(60*15))  # Cache for 15 minutes
    def list(self, request, *args, **kwargs):
        lang = request.GET.get('lang', 'en')
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        
        translated_data = []
        for item in serializer.data:
            translated_item = {
                'id': item['id'],
                'question': FAQ.objects.get(id=item['id']).question_translated(lang),
                'answer': FAQ.objects.get(id=item['id']).answer_translated(lang),
                'created_at': item['created_at'],
                'updated_at': item['updated_at']
            }
            translated_data.append(translated_item)
        
        return Response({'faqs': translated_data})
