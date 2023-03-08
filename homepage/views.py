from django.shortcuts import render
from .models import Review

def home(request):
    reviews = Review.objects.all()
    return render(request, "index.html", {"title": "Home", 'reviews': reviews})


def handler404(request, exception, template_name="404.html"):
    response = render_to_response(template_name)
    response.status_code = 404
    return response


def handler500(request, exception, template_name="500.html"):
    response = render_to_response(template_name)
    response.status_code = 500
    return response