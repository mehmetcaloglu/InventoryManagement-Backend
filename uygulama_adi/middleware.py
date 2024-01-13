# myapp/middleware.py

class CustomUserAgentMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['User-Agent'] = 'My Custom User Agent'  # Burada istediğiniz değeri ekleyin
        return response
