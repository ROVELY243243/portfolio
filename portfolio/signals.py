from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Projet, NewsletterSubscriber

@receiver(post_save, sender=Projet)
def alerte_nouveau_projet(sender, instance, created, **kwargs):
    # 'created' est True uniquement s'il s'agit d'un NOUVEAU projet (pas une modification)
    if created:
        # 1. On récupère tous les abonnés de la newsletter
        abonnes = NewsletterSubscriber.objects.all()
        
        # 2. On prépare le sujet et le texte de l'e-mail
        sujet = f"Nouveau projet réalisé : {instance.titre}"
        
        # 3. On fait une boucle pour envoyer "Un mail pour une personne"
        for abonne in abonnes:
            texte_mail = f"Bonjour,\n\nJe viens de publier un tout nouveau travail sur mon portfolio ! \n\n🚀 Projet : {instance.titre}\n📝 Description : {instance.description}\n\nVous pouvez découvrir l'intégralité des détails et mes autres réalisations en électronique industrielle et automatisation directement sur mon site.\n\nÀ très vite !\n\nRovely Mayanda Manzanza\nIngénieur Technicien Licencié en Électronique"
            
            try:
                send_mail(
                    subject=sujet,
                    message=texte_mail,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[abonne.email], # Un seul destinataire à la fois !
                    fail_silently=True, # Si un mail échoue (adresse invalide), on passe au suivant sans bloquer l'admin
                )
            except Exception:
                continue
