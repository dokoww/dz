from django.http import HttpResponse


def index(request, n1, operator, n2):
    if operator =='+':
        return HttpResponse('Bilal')
