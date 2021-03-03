from django.urls import reverse
from rest_framework import fields, routers, serializers, viewsets
from rest_framework.decorators import action
from wagtail.core.models import Page, Site

from .models import AbTest


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'hostname']
        model = Site


class PageSerializer(serializers.ModelSerializer):
    path = fields.SerializerMethodField('get_path')

    def get_path(self, page):
        return page.get_url_parts()[2]

    class Meta:
        fields = ['id', 'path']
        model = Page


class AbTestGoalSerializer(serializers.ModelSerializer):
    page = PageSerializer(source='goal_page')
    event = fields.ReadOnlyField(source='goal_event')

    class Meta:
        fields = ['page', 'event']
        model = AbTest


class AbTestSerializer(serializers.ModelSerializer):
    site = SiteSerializer(source='page.get_site')
    page = PageSerializer()
    goal = AbTestGoalSerializer(source='*')
    variant_html_url = fields.SerializerMethodField()

    def get_variant_html_url(self, test):
        return reverse('wagtail_ab_testing_api:abtest-serve-variant', args=[test.id])

    class Meta:
        fields = ['id', 'site', 'page', 'goal', 'variant_html_url']
        model = AbTest


class AbTestViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AbTestSerializer
    queryset = AbTest.objects.filter(status=AbTest.STATUS_RUNNING)

    @action(detail=True, methods=['get'])
    def serve_variant(self, request, pk=None):
        test = self.get_object()
        return test.variant_revision.as_page_object().serve(request)


router = routers.SimpleRouter()
router.register(r'tests', AbTestViewSet)

app_name = 'wagtail_ab_testing_api'
urlpatterns = router.urls
