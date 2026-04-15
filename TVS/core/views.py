from django.shortcuts import render
from .models import records

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        grade = request.POST.get('grade')

        # Save the data to the database
        record = records(name=name, age=age, grade=grade)
        record.save()
        
    return render(request, 'core/index.html')