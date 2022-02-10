from django.shortcuts import render


# Create your views here.

def main_page(request):
    return render(request, template_name="main_test.html")


def main_page_ar(request):
    return render(request, template_name="base.html")
