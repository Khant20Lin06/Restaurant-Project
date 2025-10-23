from django.shortcuts import redirect
from django.urls import reverse

class AdminAccessControlMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith(reverse('admin_dashboard')):  # /admin/ ဆိုတဲ့ path တွေ
            user = request.user
            if not user.is_authenticated:
                return redirect('loginPage')  
            elif not user.is_staff:
                return redirect('homePage')  

        response = self.get_response(request)
        return response
