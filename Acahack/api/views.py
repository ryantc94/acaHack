from django.http import HttpResponse
import json

def index(response):
    print(response)
    return HttpResponse(json.dumps({"success": question_id}))

def results(response, drug_letters):
    return ()

# Create your views here.
