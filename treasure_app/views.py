from django.shortcuts import render

# Create your views here.
def treasure_island(request):
    return render(request, 'treasure_island.html')
