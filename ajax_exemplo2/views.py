from django.shortcuts import render
from .models import Profile
from django.http import JsonResponse, HttpResponse


# Create your views here.
def index(request):
    return render(request, 'ajax_exemplo2/index.html')


def getProfiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': list(profiles.values())}
    return JsonResponse(context)


def profile_form(request):
    return render(request, 'ajax_exemplo2/submit-form.html')


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST['email']
        bio = request.POST['bio']

        new_profile = Profile.objects.create(
            name=name,
            email=email,
            bio=bio
        )
        new_profile.save()
        return HttpResponse('New Profile Created Successfully')

