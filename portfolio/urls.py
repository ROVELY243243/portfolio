from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_vue, name='index'),
    path('archives/', views.archives_vue, name='portfolio_archives'),
    
    # NOUVEAUX CHEMINS POUR DÉTAIL ET BLOG
    path('projet/<int:id>/', views.projet_detail, name='projet_detail'),
    path('blog/', views.liste_blog, name='liste_blog'),
    
    path('contact-ajax/', views.contact_ajax, name='contact_ajax'),
    path('newsletter-ajax/', views.newsletter_ajax, name='newsletter_ajax'),
]
