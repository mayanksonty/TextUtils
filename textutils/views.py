# This File is created by Mayank Verma
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("<h1>Hello</h1>  <a href = https://www.codewithharry.com/videos/python-gui-tkinter-hindi-1>Code with HArry </a>")

def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    capitalize = request.POST.get('capitalize','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charactercounter = request.POST.get('charactercounter','off')
    count = 0
    # print(removepunc1)
    if removepunc == 'on':
        punctions = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctions:
                analyzed = analyzed+char
        djtext = analyzed
        # params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
    
    if capitalize == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed+char.upper()
        
        djtext = analyzed
        # params = {'purpose':'Capitalised Text','analyzed_text':analyzed}

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed = analyzed+char
        
        djtext = analyzed
        # params = {"purpose":"New Line Removal","analyzed_text":analyzed}
    
    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed+char
            
        djtext = analyzed
                
        # params = {"purpose":"Removing extra spaces","analyzed_text":analyzed}

    if charactercounter == "on":
        
        for index, char in enumerate(djtext):
            if not(djtext[index] == " "):
                count = count+1

        djtext = count
    
    if(removepunc!="on" and charactercounter != "on" and extraspaceremover != "on" and newlineremover != "on" and capitalize != 'on'):
        return HttpResponse("Error")
        
    params = {"purpose":"Counting the Characters it has","analyzed_text":djtext}

    return render(request,'analyze.html',params)


