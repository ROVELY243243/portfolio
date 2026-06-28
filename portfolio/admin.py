from django.contrib import admin
from .models import Profile, Experience, Formation, Certification, Competence, ContactMessage, NewsletterSubscriber, Projet
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_publication')
    prepopulated_fields = {'slug': ('titre',)} # Très pratique pour générer l'URL automatiquement
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('nom_complet', 'titre', 'email', 'telephone')

@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    # Fusion de tes deux configurations précédentes
    list_display = ('titre', 'est_archive', 'technologies', 'ordre')
    list_editable = ('est_archive', 'ordre')
    search_fields = ('titre', 'technologies')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('titre_poste', 'entreprise', 'date_debut', 'date_fin', 'ordre')
    list_editable = ('ordre',)

@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display = ('diplome', 'institution', 'annee', 'ordre')
    list_editable = ('ordre',)

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('titre', 'organisateur', 'date')

@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ('nom',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'sujet', 'date_envoi')
    readonly_fields = ('nom', 'email', 'sujet', 'message', 'date_envoi')
    search_fields = ('nom', 'email', 'sujet')

@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_inscription')
    search_fields = ('email',)
