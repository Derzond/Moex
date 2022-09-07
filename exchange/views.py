from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from exchange.async_tasks.get_prices import get_data
from exchange.models import Gold


class PreciousMetals(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'precious_metals.html'

    def get(self, request):
        get_data()

        queryset = Gold.objects.all()
        return Response({'gold_prices': queryset})
