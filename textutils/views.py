# This File is created by Mayank Verma
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    capitalize = request.POST.get('capitalize','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charactercounter = request.POST.get('charactercounter','off')
    count = 0

    if removepunc == 'on':
        punctions = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctions:
                analyzed = analyzed+char
        djtext = analyzed
        
    
    if capitalize == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed+char.upper()
        
        djtext = analyzed
       

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed = analyzed+char
        
        djtext = analyzed
       
    
    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed+char
            
        djtext = analyzed
                
        

    if charactercounter == "on":
        
        for index, char in enumerate(djtext):
            if not(djtext[index] == " "):
                count = count+1

        djtext = count
    
    if(removepunc!="on" and charactercounter != "on" and extraspaceremover != "on" and newlineremover != "on" and capitalize != 'on'):
        return HttpResponse("Error")
        
    params = {"purpose":"Counting the Characters it has","analyzed_text":djtext}

    return render(request,'analyze.html',params)


