from django.db import models

# 1. PROFIL GÉNÉRAL
class Profile(models.Model):
    nom_complet = models.CharField(max_length=100, default="Rovely Mayanda Manzanza")
    titre = models.CharField(max_length=150, default="Ingénieur Technicien Licencié en Électronique Industrielle")
    photo_profil = models.ImageField(upload_to="portfolio/profil/", blank=True, null=True, verbose_name="Photo de profil")
    a_propos = models.TextField(blank=True, verbose_name="À propos de moi / Introduction")
    email = models.EmailField(default="rovelymayanda1@gmail.com", verbose_name="Adresse Email Professionnelle")
    telephone = models.CharField(max_length=20, default="+243 892 793 895", verbose_name="Numéro de Téléphone")
    adresse = models.CharField(max_length=255, default="14, Avenue Kimbuku, Q. Mateba, Ngaba, Kinshasa", verbose_name="Adresse / Quartier")
    linkedin = models.URLField(blank=True, verbose_name="Lien LinkedIn (Optionnel)")
    github = models.URLField(blank=True, verbose_name="Lien GitHub (Optionnel)")
    cv_file = models.FileField(upload_to="portfolio/cv/", blank=True, null=True, verbose_name="Fichier CV PDF (Optionnel)")

    class Meta:
        verbose_name = "Mon Profil Général"
        verbose_name_plural = "Mon Profil Général"

    def __str__(self):
        return self.nom_complet

# 2. EXPÉRIENCES PROFESSIONNELLES
class Experience(models.Model):
    titre_poste = models.CharField(max_length=150, verbose_name="Titre du poste")
    entreprise = models.CharField(max_length=150, verbose_name="Entreprise")
    lieu = models.CharField(max_length=100, blank=True, verbose_name="Lieu")
    date_debut = models.CharField(max_length=50, verbose_name="Date de début")
    date_fin = models.CharField(max_length=50, blank=True, verbose_name="Date de fin")
    description = models.TextField(verbose_name="Description des tâches")
    image = models.ImageField(upload_to="portfolio/images/", blank=True, null=True, verbose_name="Logo/Image (Optionnel)")
    ordre = models.IntegerField(default=0, verbose_name="Ordre d'affichage")

    class Meta:
        verbose_name = "Expérience Professionnelle"
        verbose_name_plural = "Expériences Professionnelles"
        ordering = ['ordre', '-id']

    def __str__(self):
        return f"{self.titre_poste} - {self.entreprise}"

# 3. FORMATIONS
class Formation(models.Model):
    diplome = models.CharField(max_length=150, verbose_name="Diplôme")
    institution = models.CharField(max_length=150, verbose_name="Institution")
    annee = models.CharField(max_length=50, verbose_name="Année / Période")
    ordre = models.IntegerField(default=0, verbose_name="Ordre d'affichage")

    class Meta:
        verbose_name = "Formation"
        verbose_name_plural = "Formations"
        ordering = ['ordre', '-id']

    def __str__(self):
        return f"{self.diplome} - {self.institution}"

# 4. CERTIFICATIONS
class Certification(models.Model):
    titre = models.CharField(max_length=200, verbose_name="Titre de la certification")
    organisateur = models.CharField(max_length=150, verbose_name="Délivré par")
    date = models.CharField(max_length=50, verbose_name="Date d'obtention")

    class Meta:
        verbose_name = "Certification"
        verbose_name_plural = "Certifications"

    def __str__(self):
        return self.titre

# 5. COMPÉTENCES
class Competence(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nom de la compétence")
    description_details = models.TextField(blank=True, verbose_name="Détails (Optionnel)")
    icone = models.ImageField(upload_to="portfolio/icones/", blank=True, null=True, verbose_name="Icône (Optionnel)")

    class Meta:
        verbose_name = "Compétence"
        verbose_name_plural = "Compétences"

    def __str__(self):
        return self.nom

# 6. PROJETS (Classe unique et complète)
class Projet(models.Model):
    titre = models.CharField(max_length=150, verbose_name="Nom du projet")
    description = models.TextField(verbose_name="Description détaillée")
    technologies = models.CharField(max_length=200, help_text="Ex: Python, Django, Arduino, GSM Module")
    image = models.ImageField(upload_to="portfolio/projets/", blank=True, null=True)
    lien_github = models.URLField(blank=True, verbose_name="Lien vers le code (Optionnel)")
    lien_demonstration = models.URLField(blank=True, verbose_name="Lien démo / Vidéo (Optionnel)")
    ordre = models.IntegerField(default=0)
    est_archive = models.BooleanField(default=False, verbose_name="Mettre dans les archives ?")

    class Meta:
        verbose_name = "Projet"
        verbose_name_plural = "Projets"
        ordering = ['ordre', '-id']

    def __str__(self):
        return self.titre
class Article(models.Model):
    titre = models.CharField(max_length=200)
    slug = models.SlugField(unique=True) # Pour avoir des URLs jolies : /blog/mon-article
    contenu = models.TextField()
    image_couverture = models.ImageField(upload_to="blog/")
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

# 7. MESSAGES DE CONTACT
class ContactMessage(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nom de l'expéditeur")
    email = models.EmailField(verbose_name="Email de l'expéditeur")
    sujet = models.CharField(max_length=200, verbose_name="Sujet")
    message = models.TextField(verbose_name="Corps du message")
    date_envoi = models.DateTimeField(auto_now_add=True, verbose_name="Reçu le")

    class Meta:
        verbose_name = "Message de Contact"
        verbose_name_plural = "Messages de Contact"
        ordering = ['-date_envoi']

    def __str__(self):
        return f"{self.nom} - {self.sujet}"

# 8. ABONNÉS NEWSLETTER
class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True, verbose_name="Adresse Email")
    date_inscription = models.DateTimeField(auto_now_add=True, verbose_name="Date d'abonnement")

    class Meta:
        verbose_name = "Abonné Newsletter"
        verbose_name_plural = "Abonnés Newsletter"
        ordering = ['-date_inscription']

    def __str__(self):
        return self.email
