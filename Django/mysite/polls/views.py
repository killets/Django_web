from django.shortcuts import render
from .models import Msg
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

# Create your views here.
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    
    # msg_lastest = Msg.objects.get(pk=1)
    # if Msg.objects.all().exists():
      # msg_lastest = Msg.objects.all()[0]
   # else:
      # msg_lastest = "No News"

    # msgs = Msg.objects.all()
    posts = Msg.objects.filter(expire_date__gte = timezone.now())
    s = ".             . " 
    # msgs = s.join((map(str, posts)) )
    msgs = " "
    for post in posts:
       msgs += post.name
       #msgs +=  s

    return render(
        request,
        'index.html',
        context= {'msgs': msgs},
    )


from django.http import HttpResponseRedirect

from .forms import NameForm


def contact(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            data = form.cleaned_data

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            # context = {
            # 'ChineseName': data['ChineseName'],
            # 'PinYinName': data['PinYinName'],
            # 'EnglishName': EnglishName,
            # 'DateBirth': DateBirth,
            # 'Age': Age,
            # 'Email': Email,
            # 'Phone' : Phone,
            # 'WeChat': WeChat,
            # 'City': City,
            # 'School':  School,
            # 'Grade' : Grade,
            # 'DateEnroll' : DateEnroll,
            # 'NeedTravel' : NeedTravel,
            # 'GPA' : GPA,
            # 'TOEFL' :  TOEFL,
            # 'SAT' :SAT,
            # 'UsSchool': UsSchool,
            # 'Background' : Background,
            # 'Questions' : Questions,
            # }

            content = template.render(data)

            email = EmailMessage(
                "New contact form submission",
                content,
                'web_sharronart@163.com',
                ['web_sharronart@163.com'],
            )
            email.send()

            return HttpResponseRedirect('contact.html')

    # if a GET (or any other method) we'll create a blank form
    else:	
        form = NameForm()

    form = NameForm()
    # print('22222222')

    return render(request, 'contact.html', {'form': form})
