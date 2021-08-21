# created by me

from django.http import HttpResponse, response
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
    # return HttpResponse("hello")

def analyze(request):
    # get the text
    djtext = request.POST.get('text','default')

    # Check checkbox value
    rempun = request.POST.get('rempun','off')
    capitalize = request.POST.get('capitalize','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')

    # Check which checkboc is on
    if rempun =="on":
        punctuations = ''' !@#%^&*()_+?.,><'";:\|[](){}~` '''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params = {'purpose': 'Removed Puctuaions', 'analyzed_text': analyzed}
        djtext = analyzed

    if(capitalize == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Capitalize', 'analyzed_text': analyzed}
        djtext = analyzed          

    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        djtext = analyzed 
    
    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Capitalize', 'analyzed_text': analyzed}

    if (rempun != 'on' and newlineremover != 'on' and capitalize != 'on' and extraspaceremover != 'on'):
        return HttpResponse('error')
    return render(request,"analyze.html", params)        

