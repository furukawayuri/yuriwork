from django.http import HttpResponse
from django.views.decorators.cache import never_cache
from django.contrib.admin.sites import site, AdminSite
import base64

class MyAdminSite(AdminSite):

    def __init__(self, name='admin'):
        super().__init__()

    def get_urls(self):
        self._registry = site._registry
        return super().get_urls()

    @never_cache
    def login(self, request, extra_context=None):
        if not self._basicAuth(request):
            return self._http401()
        return super().login(request, extra_context)

    def _basicAuth(self, request):
        if 'HTTP_AUTHORIZATION' not in request.META:
            return False
        (authscheme, base64_idpass) = request.META['HTTP_AUTHORIZATION'].split(' ', 1)
        if authscheme.lower() != 'basic':
            return self._http401()
        idpass = base64.decodestring(base64_idpass.strip().encode('ascii')).decode('ascii')
        (id_, password) = idpass.split(':', 1)
        if id_ == "foo" and password == "bar":
            return True
        else:
            return False

    def _http401(self):
        response = HttpResponse("Unauthorized", status=401)
        response['WWW-Authenticate'] = 'Basic realm="basic auth test"'

        return response


my_site = MyAdminSite()

