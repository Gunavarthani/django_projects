from django.shortcuts import render
from .models import BusTiming
# Create your views here.
def bus_timings(request):
    timings = BusTiming.objects.all()
    return render(request, 'bus_timings.html', {'timings': timings})
