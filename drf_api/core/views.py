from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def test_view(request):

    data = dict(name="json", age=23)

    return JsonResponse(data)
