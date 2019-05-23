from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login')
def index(request):
    current_user = request.user
    projects = Projects.objects.all()
    return render(request, 'index.html', locals())

@login_required(login_url='/accounts/login')
def profile(request):
    pass

@login_required(login_url='/accounts/login')
def edit_profile(request):
    pass

@login_required(login_url='/accounts/login')
def new_project(request):
    pass

@login_required(login_url='/accounts/login')
def project(request):
    pass

@login_required(login_url='/accounts/login')
def search(request):
    pass
