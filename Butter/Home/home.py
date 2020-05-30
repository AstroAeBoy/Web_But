from django.http import HttpResponse

def home_call(request):
    return HttpResponse('PRABAKARAN PAGE!')