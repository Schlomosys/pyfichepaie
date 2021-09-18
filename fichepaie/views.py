from fichepaie.models import Bullpaie
from django import views
from django.shortcuts import render, redirect
from django.contrib  import messages # Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

from django.template import loader

from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db.models import F
from django.utils import timezone
from django.contrib.auth.models import User
from django.views import generic

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from wkhtmltopdf.views import PDFTemplateView

User = get_user_model()

#excel
from django.http import HttpResponse
from .resources import BullpaieResource
from tablib import Dataset

#task celery
from django.http import HttpResponse
from celery import Celery
from .tasks import my_first_task




#___________________________________________________________________________________



#____________________________________________________________________________________
                 

#celery task

def index(request):
    
    
    my_first_task.delay(10)
    return HttpResponse('response done')
#utilisation des vues generiques de python

def Home(request):
    return render(request,'fichepaie/home.html' )
def Login(request):
    return render(request,'registration/login.html' )
def Register(request):
   
        return render(request,'registration/registration.html' )

def Storeuser(request):
    
    email=request.POST['email']
    password=request.POST['password']
    password2=request.POST['password2']
    if password ==password2:
        if User.objects.filter(email=email).exists():
            messages.info(request, 'Cet email est déja utilisé pour un autre compte')
            return redirect('fichepaie:register')
       
        else:
            user=User.objects.create_user( email=email, password=password)
            user.save();
            return redirect('fichepaie:login')       
    else:
        messages.info(request, 'Les mots de passe ne correspondent pas')
        return redirect('fichepaie:register')

    #return redirect('register')

      

# def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
   # context = {'latest_question_list': latest_question_list}
   # return render(request, 'sondage/index.html', context)

# def detail(request, question_id):
   # try:
        #question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
      #  raise Http404("Question does not exist")#question = get_object_or_404(Question, pk=question_id)
   # return render(request, 'sondage/detail.html', {'question': question})

# def resultats(request, question_id):
   # question= get_object_or_404(Question, pk=question_id )
   #  try:
      #  selected_choice = question.choice_set.get(pk=request.POST['choice'])
    #except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
       ## })
   # else:
        #empecher les conclits de concurence
       # selected_choice.votes=F('votes') + 1
        #eviter une double mise a jour
        #selected_choice.refresh_from_db()
       # selected_choice.save()#
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        #return HttpResponseRedirect(reverse('sondage:resultats', args=(question.id,)))#
def Importxl(request):
    if request.method == 'POST':
        person_resource = BullpaieResource()
        dataset = Dataset()
        new_persons = request.FILES['files']

        #imported_data = dataset.load(new_persons.read())
        imported_data = dataset.load(new_persons.read())
        for data in imported_data:
            value=Bullpaie(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
                data[10],
                data[11],
                data[12],
                data[13],
                data[14],
                data[15],
                data[16],
                data[17],
                data[18],
                data[19],
                data[20],
                data[21],
                data[22],
                data[23],
                data[24],
                data[25],
                data[26],
                data[27],
                data[28],
                data[29],
                data[30],
                data[31], )
            value.save()    
        #result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        #if not result.has_errors():
            #person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'fichepaie/importexcel.html')




class MyPDF(PDFTemplateView):
    filename = 'my_pdf.pdf'
    template_name = 'fichepaie/pdfview.html'
    cmd_options = {
        'margin-top': 3,
    }
    
        