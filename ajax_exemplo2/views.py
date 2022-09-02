from django.shortcuts import render
from .models import Profile
from django.http import JsonResponse


# Create your views here.
def index(request):
    return render(request, 'ajax_exemplo2/index.html')


def getProfiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': list(profiles.values())}
    return JsonResponse(context)
