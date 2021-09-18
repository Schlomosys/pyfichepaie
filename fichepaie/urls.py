from django.urls import path, include
#from django.conf.urls.defaults import url, patterns
from wkhtmltopdf.views import PDFTemplateView

from . import views

app_name = 'fichepaie'
urlpatterns = [
    #path('', views.index, name='index'),
    #sondage/5/
    #path('detail/<int:question_id>/', views.detail, name='detail'),
     #sondage/5/results/
    #path('<int:question_id>/results/', views.resultats, name='resultats'),
     #sondage/5/vote/
    #path('<int:question_id>/vote/', views.vote, name='vote'),
    #path('', views.IndexView.as_view(), name='index'),
    #path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #path('<int:question_id>/vote/', views.vote, name='vote'),
    #path('register/', views.Register, name='register'),
    ##path('login/', views.Login, name='login'),
    #path('storeuser/',  views.Storeuser, name='storeuser'),/docmanag/
    
    path('home/', views.Home, name='home'),

    path('register/', views.Register, name='register'),
    path('storeuser/',  views.Storeuser, name='storeuser'),
    path('importexel/',  views.Importxl, name='importexcel'),
    path('accounts/', include('django.contrib.auth.urls')),
    #url(r'^pdf/$', PDFTemplateView.as_view(template_name='my_template.html',
                                         #  filename='my_pdf.pdf'), name='pdf'),
    path('pdf/',  views.MyPDF.as_view(), name='pdf'),
    path('celery-test/',views.index, name='celery_test_url'),
]