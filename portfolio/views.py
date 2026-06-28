from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import (
    Profile, Experience, Formation, Certification, 
    Competence, Projet, Article, ContactMessage, NewsletterSubscriber
)

# --- VUES D'AFFICHAGE ---

def index_vue(request):
    profil = Profile.objects.first()
    experiences = Experience.objects.all().order_by('ordre')
    formations = Formation.objects.all().order_by('ordre')
    certifications = Certification.objects.all()
    competences = Competence.objects.all()
    
    # Projets non archivés, max 6
    projets = Projet.objects.filter(est_archive=False).order_by('-id')[:6]
    
    for p in projets:
        p.tech_list = [t.strip() for t in p.technologies.split(',')] if p.technologies else []
            
    context = {
        'profil': profil,
        'projets': projets,
        'experiences': experiences,
        'formations': formations,
        'certifications': certifications,
        'competences': competences,
    }
    return render(request, 'portfolio/index.html', context)

def archives_vue(request):
    projets = Projet.objects.filter(est_archive=True).order_by('-id')
    for p in projets:
        p.tech_list = [t.strip() for t in p.technologies.split(',')] if p.technologies else []
    return render(request, 'portfolio/archives.html', {'projets': projets})

def projet_detail(request, id):
    projet = get_object_or_404(Projet, id=id)
    projet.tech_list = [t.strip() for t in projet.technologies.split(',')] if projet.technologies else []
    return render(request, 'portfolio/projet_detail.html', {'projet': projet})

def liste_blog(request):
    articles = Article.objects.all().order_by('-date_publication')
    return render(request, 'portfolio/blog.html', {'articles': articles})

# --- VUES AJAX ---

def contact_ajax(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        nom = request.POST.get('name')
        email = request.POST.get('email')
        sujet = request.POST.get('subject')
        message = request.POST.get('message')
        
        if nom and email and sujet and message:
            ContactMessage.objects.create(nom=nom, email=email, sujet=sujet, message=message)
            
            texte_reponse = f"Bonjour {nom},\n\nMerci d'avoir pris contact. J'ai bien reçu votre message : '{sujet}'.\nJe reviendrai vers vous rapidement."
            
            try:
                send_mail(f"Accusé de réception : {sujet}", texte_reponse, settings.EMAIL_HOST_USER, [email])
                send_mail(f"[Contact] {sujet}", f"De: {nom} ({email})\n\n{message}", settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
                return JsonResponse({'status': 'success', 'message': 'Message envoyé !'})
            except Exception:
                return JsonResponse({'status': 'success', 'message': 'Message enregistré (Erreur envoi email).'})
        return JsonResponse({'status': 'error', 'message': 'Champs manquants.'})
    return JsonResponse({'status': 'error', 'message': 'Requête invalide.'})

def newsletter_ajax(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        email = request.POST.get('email')
        if email:
            if NewsletterSubscriber.objects.filter(email=email).exists():
                return JsonResponse({'status': 'warning', 'message': 'Déjà inscrit.'})
            
            NewsletterSubscriber.objects.create(email=email)
            try:
                send_mail("Merci pour votre abonnement !", "Bienvenue dans ma newsletter technique.", settings.EMAIL_HOST_USER, [email])
            except Exception:
                pass
            return JsonResponse({'status': 'success', 'message': 'Inscription validée !'})
        return JsonResponse({'status': 'error', 'message': 'Email invalide.'})
    return JsonResponse({'status': 'error', 'message': 'Requête invalide.'})
