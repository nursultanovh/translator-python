from django.shortcuts import render
from googletrans import Translator

def index(request):
    if request.method == "POST":
        text = request.POST.get("text")
        lang = request.POST.get("lang")
        if text and lang:
            data = Translator().translate(text, dest=lang)
        else:
            data = {"text": "", "src": "en", "dest":"en"}
        return render(request, "index.html", {"data": data})
    return render(request, "index.html")
