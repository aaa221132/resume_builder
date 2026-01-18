from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Resume, Skill, Experience, Education


def home(request):
    return render(request, 'app/home.html')



@login_required
def resume_list(request):
    search = request.GET.get('q', '')
    per_page = request.GET.get('per_page', '4')

    try:
        per_page = int(per_page)
        if per_page not in [4, 6, 8, 10]:
            per_page = 4
    except ValueError:
        per_page = 4

    resumes = Resume.objects.filter(user=request.user).filter(
        full_name__icontains=search
    ) | Resume.objects.filter(
        user=request.user,
        profession__icontains=search
    )

    resumes = resumes.distinct().order_by('-id')

    paginator = Paginator(resumes, per_page)
    page_number = request.GET.get('page')
    resume_page = paginator.get_page(page_number)

    return render(request, 'app/resume_list.html', {
        'resumes': resume_page,
        'search': search,
        'per_page': per_page
    })


@login_required
def create_resume(request):
    resume = Resume.objects.create(
        user=request.user,
        full_name='Нове резюме',
        profession='',
        summary=''
    )
    return redirect('resume_detail', resume.id)


@login_required
def resume_detail(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id, user=request.user)

    if request.method == 'POST':
        resume.full_name = request.POST.get('full_name')
        resume.profession = request.POST.get('profession')
        resume.summary = request.POST.get('summary')
        resume.save()

    return render(request, 'app/resume_detail.html', {'resume': resume})


@login_required
def delete_resume(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id, user=request.user)
    if request.method == 'POST':
        resume.delete()
        return redirect('resume_list')
    return render(request, 'app/delete_resume.html', {'resume': resume})



@login_required
def add_skill(request, resume_id):
    Skill.objects.create(
        resume_id=resume_id,
        name=request.POST.get('name')
    )
    return redirect('resume_detail', resume_id)


@login_required
def delete_skill(request, skill_id):
    skill = get_object_or_404(Skill, id=skill_id)
    rid = skill.resume.id
    skill.delete()
    return redirect('resume_detail', rid)



@login_required
def add_experience(request, resume_id):
    Experience.objects.create(
        resume_id=resume_id,
        company=request.POST.get('company'),
        position=request.POST.get('position'),
        start_date=request.POST.get('start_date'),
        end_date=request.POST.get('end_date') or None,
        description=request.POST.get('description')
    )
    return redirect('resume_detail', resume_id)


@login_required
def delete_experience(request, exp_id):
    exp = get_object_or_404(Experience, id=exp_id)
    rid = exp.resume.id
    exp.delete()
    return redirect('resume_detail', rid)


@login_required
def add_education(request, resume_id):
    Education.objects.create(
        resume_id=resume_id,
        institution=request.POST.get('institution'),
        degree=request.POST.get('degree'),
        start_year=request.POST.get('start_year'),
        end_year=request.POST.get('end_year') or None
    )
    return redirect('resume_detail', resume_id)


@login_required
def delete_education(request, edu_id):
    edu = get_object_or_404(Education, id=edu_id)
    rid = edu.resume.id
    edu.delete()
    return redirect('resume_detail', rid)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/resumes/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/resumes/')
        else:
            messages.error(request, 'Невірний логін або пароль')

    return render(request, 'app/login.html')



def register_view(request):
    if request.user.is_authenticated:
        # Уже залогинен → редирект на свои резюме
        return redirect('/resumes/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'Паролі не співпадають')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Користувач вже існує')
        else:
            user = User.objects.create_user(username=username, password=password1)
            login(request, user)
            return redirect('/resumes/')

    return render(request, 'app/register.html')



def logout_view(request):
    logout(request)
    return redirect('home')
