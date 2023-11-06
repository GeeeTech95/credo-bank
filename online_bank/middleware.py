from django.http import HttpResponse
from django.template import loader

class AccountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.user.is_blocked  and request.path != "/":
            ctx = {"block_reason" : request.user.block_reason}
            template = loader.get_template('accounts-blocked.html')
            return HttpResponse(template.render(ctx), content_type='text/html', status=403)
        response = self.get_response(request)
        return response