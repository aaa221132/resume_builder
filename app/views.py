from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Resume, Skill, Experience, Education

@login_required
def resume_list(request):
    resumes = Resume.objects.filter(user=request.user)
    return render(request, 'app/resume_list.html', {'resumes': resumes})

@login_required
def create_resume(request):
    if request.method == 'POST':
        resume = Resume.objects.create(
            user=request.user,
            full_name=request.POST.get('full_name'),
            profession=request.POST.get('profession'),
            summary=request.POST.get('summary'),
        )
        return redirect('resume_detail', resume.id)
    return render(request, 'app/create_resume.html')

@login_required
def resume_detail(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id, user=request.user)
    return render(request, 'app/resume_detail.html', {'resume': resume})

@login_required
def add_skill(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id, user=request.user)
    if request.method == 'POST':
        Skill.objects.create(resume=resume, name=request.POST.get('name'))
        return redirect('resume_detail', resume.id)

@login_required
def add_experience(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id, user=request.user)
    if request.method == 'POST':
        Experience.objects.create(
            resume=resume,
            company=request.POST.get('company'),
            position=request.POST.get('position'),
            start_date=request.POST.get('start_date'),
            end_date=request.POST.get('end_date') or None,
            description=request.POST.get('description')
        )
        return redirect('resume_detail', resume.id)

@login_required
def add_education(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id, user=request.user)
    if request.method == 'POST':
        start_year = request.POST.get('start_year')
        end_year = request.POST.get('end_year')

        # Преобразуем в int, если передано
        start_year = int(start_year) if start_year else None
        end_year = int(end_year) if end_year else None

        Education.objects.create(
            resume=resume,
            institution=request.POST.get('institution'),
            degree=request.POST.get('degree'),
            start_year=start_year,
            end_year=end_year
        )
        return redirect('resume_detail', resume.id)
