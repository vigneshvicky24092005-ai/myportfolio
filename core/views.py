from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
import requests

from .models import SiteProfile, Skill, Project, Education, Certification, ContactMessage
from .forms import ContactForm

def get_github_repositories(username, limit=6):
    """
    Optionally fetch repository stats directly from GitHub API for vigneshvicky24092005-ai.
    """
    if not username:
        return []
    
    url = f"https://api.github.com/users/{username}/repos?sort=updated&per_page={limit}"
    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'User-Agent': 'Vignesh-Portfolio-App'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=4)
        if response.status_code == 200:
            repos = response.json()
            cleaned_repos = []
            for repo in repos:
                cleaned_repos.append({
                    'name': repo.get('name'),
                    'description': repo.get('description') or 'Open source project by Vignesh.',
                    'html_url': repo.get('html_url'),
                    'language': repo.get('language') or 'Code',
                    'stars': repo.get('stargazers_count', 0),
                    'forks': repo.get('forks_count', 0),
                    'updated_at': (repo.get('updated_at') or '')[:10],
                })
            return cleaned_repos
    except Exception:
        pass
    
    return []


def index(request):
    profile = SiteProfile.objects.first()
    
    skills_software = Skill.objects.filter(category='software')
    skills_database = Skill.objects.filter(category='database')
    skills_ece = Skill.objects.filter(category='ece')
    skills_tools = Skill.objects.filter(category='tools')
    
    projects = Project.objects.all()
    educations = Education.objects.all()
    certifications = Certification.objects.all()
    
    github_username = getattr(settings, 'GITHUB_USERNAME', 'vigneshvicky24092005-ai')
    contact_email = getattr(settings, 'CONTACT_EMAIL', 'vigneshvicky24092005@gmail.com')
    github_repos = get_github_repositories(github_username)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_instance = form.save()
            
            subject = f"Portfolio Contact: {contact_instance.subject} (from {contact_instance.name})"
            body = (
                f"You have received a new contact message from your portfolio website!\n\n"
                f"Sender Name: {contact_instance.name}\n"
                f"Sender Email: {contact_instance.email}\n"
                f"Subject: {contact_instance.subject}\n"
                f"Sent At: {contact_instance.created_at.strftime('%Y-%m-%d %H:%M:%S') if contact_instance.created_at else 'Just now'}\n\n"
                f"Message Content:\n"
                f"----------------------------------------\n"
                f"{contact_instance.message}\n"
                f"----------------------------------------\n"
            )
            
            # 1. Native Django send_mail (SMTP when configured)
            try:
                send_mail(
                    subject,
                    body,
                    getattr(settings, 'DEFAULT_FROM_EMAIL', contact_email),
                    [contact_email],
                    fail_silently=True,
                )
            except Exception:
                pass

            # 2. FormSubmit Gateway (direct HTTP delivery straight to inbox)
            try:
                requests.post(
                    f"https://formsubmit.co/ajax/{contact_email}",
                    data={
                        'name': contact_instance.name,
                        'email': contact_instance.email,
                        '_subject': subject,
                        'message': contact_instance.message,
                        '_replyto': contact_instance.email,
                    },
                    headers={
                        'Accept': 'application/json',
                        'Referer': request.build_absolute_uri('/'),
                        'Origin': request.build_absolute_uri('/').rstrip('/')
                    },
                    timeout=5
                )
            except Exception:
                pass

            messages.success(
                request, 
                f"Thank you, {contact_instance.name}! Your message has been sent to {contact_email}."
            )
            return redirect('/#contact')
        else:
            messages.error(request, "Please check the form inputs and ensure all required fields are correctly filled.")
    else:
        form = ContactForm()

    context = {
        'profile': profile,
        'skills_software': skills_software,
        'skills_database': skills_database,
        'skills_ece': skills_ece,
        'skills_tools': skills_tools,
        'projects': projects,
        'educations': educations,
        'certifications': certifications,
        'github_repos': github_repos,
        'github_username': github_username,
        'contact_email': contact_email,
        'form': form,
    }
    return render(request, 'core/index.html', context)
