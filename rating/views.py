from django.shortcuts import render
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
    try:
        current_user=request.user.id
        my_projects = Projects.objects.filter(user=current_user)
        my_profile = Profile.objects.get(user_id=current_user)
    except Exception as e:
        raise Http404()
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
            return redirect('edit_profile')
    else:
        form = ProfileForm()
    return render(request, 'edit_profile.html', {'form': form})

@login_required(login_url='/accounts/login')
def new_project(request):
    pass

@login_required(login_url='/accounts/login')
def project(request):
    try:
        project = Projects.objects.get(id=project_id)
    except Projects.DoesNotExist:
        raise Http404()
    return render(request, "project.html", locals())

@login_required(login_url='/accounts/login')
def search(request):
    pass
