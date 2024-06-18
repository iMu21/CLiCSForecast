from django.utils.deprecation import MiddlewareMixin

class CustomHeadersMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response['Cross-Origin-Opener-Policy'] = 'unsafe-none'
        response['Referrer-Policy'] = 'unsafe-url'
        response['Access-Control-Allow-Origin'] = '*'
        
        return response