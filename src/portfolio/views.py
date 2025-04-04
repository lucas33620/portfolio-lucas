from datetime import datetime
from django.shortcuts import render

def homepage(request):
    return render(request, 'portfolio/homepage.html', {'year': datetime.now().year})
