from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from .models import Project, Profile, Rating, categories, technologies
from .forms import ProfileForm, UploadForm

@login_required(login_url='/accounts/login')
def index(request):
    current_user = request.user
    projects = Project.objects.all()
    return render(request, 'index.html', locals())

@login_required(login_url='/accounts/login')
def profile(request):
    current_user=request.user
    my_projects = Project.objects.filter(user=current_user)
    my_profile = Profile.objects.get(user=current_user)
    return render(request, 'profile.html', locals())

@login_required(login_url='/accounts/login')
def edit_profile(request):
    current_user = request.user
    profile=Profile.objects.filter(user=current_user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            prof = form.save(commit=False)
            prof.user = current_user
            prof.save()
            return redirect('myprofile')
    else:
        form = ProfileForm()
    return render(request, 'edit_profile.html', {'form': form})

@login_required(login_url='/accounts/login')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
            return redirect('index')
    else:
        form = UploadForm()
    return render(request, 'new_project.html', {'form': form})

@login_required(login_url='/accounts/login')
def project(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        raise Http404()
    return render(request, "project.html", locals())

@login_required(login_url='/accounts/login')
def search(request):
    pass
