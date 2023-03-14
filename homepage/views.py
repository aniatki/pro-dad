from django.shortcuts import render
from admin_dashboard.models import Review, Package
from django.contrib import messages

def home(request):
    reviews = Review.objects.all()
    packages = Package.objects.all()
    return render(request, 'index.html', {
        'title': 'Home', 
        'reviews': reviews, 
        'packages': packages,
        'request': request,
        })


def handler404(request, exception, template_name='404.html'):
    response = render_to_response(template_name)
    response.status_code = 404
    return response


def handler500(request, exception, template_name='500.html'):
    response = render_to_response(template_name)
    response.status_code = 500
    return response