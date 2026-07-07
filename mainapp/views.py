# i have created this file - Raj

from django.http import HttpResponse
from django.shortcuts import render


def analyzer(request):
    #get the text
    djtext = request.POST.get('text', 'default')

    # check checkbox value
    clearpunc = request.POST.get('clearpunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    # check which checkbox is on
    if clearpunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'clear punctuation', 'analyzed_text': analyzed}
        djtext = analyzed

        #analyze the text 
    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'changed to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
    
    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose':'Removed New Line', 'analyzed_text': analyzed}
        djtext = analyzed
    
    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose':'Removed Extra Space', 'analyzed_text': analyzed}
    
    if(clearpunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on"):
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)

def tem(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def search(request):
    search = request.GET.get('search', 'off')

    if search == 'about':
        msg = {'message' : 'Your Search item is founded'}
        return render(request, 'about.html', msg)
    
    elif search == 'contact us':
        msg = {'message' : 'Your Search item is founded'}
        return render(request, 'contact.html', msg)
    
    else:
        context = {'search' : search}
        return render(request, 'search.html', context)