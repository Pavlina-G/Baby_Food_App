from django.shortcuts import render


class CustomServerErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if response.status_code >= 500:
            return render(request, '500.html')

        return response


class CustomClientErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if 400 <= response.status_code <= 499:
            return render(request, '404.html')

        return response
