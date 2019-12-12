from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    # Obtener la informacion que se ingresa en el
    # TextArea
    user = request.GET['user']
    wordlist = user.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #increase
            worddictionary[word] +=1
        else:
            #add worddictionary
            worddictionary[word]=1

        sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'user':user,'count':len(wordlist),'sortedwords':sortedwords})
