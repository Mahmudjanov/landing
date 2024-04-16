from django.shortcuts import render
from django.shortcuts import redirect
from.models import *


def index_view(request):
    context = {
        'banner': Banner.objects.last(),
        'service': Services.objects.all().order_by('-id')[:6],
        'about': About.objects.last(),
        'portfolio':Portfolio.objects.all(),
        'testimonials':Testimonials.objects.all(),
        'client':Client.objects.all(),
        'conatact':Conatact.objects.all(),
        'smedia':Smedia.objects.all(),
        'address':Address.objects.last(),
        'information':Information.objects.last()

    }
    return render(request,'index.html',context)

def create_form(request):
    if request.method == "POST":
        Form.objects.create(
            name = request.POST.get("name"),
            last_name = request.POST.get("last_name"),
            email = request.POST.get("email"),
            subject = request.POST.get("subject"),
            text = request.POST.get("text")
        )
        return redirect("index")
    return redirect("index")