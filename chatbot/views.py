from django.shortcuts import render
from django.http import JsonResponse
import json
from .chatbot_engine import get_response

def home(request):
    return render(request, "chatbot/index.html")


def chat(request):

    if request.method == "POST":

        data = json.loads(request.body)

        message = data.get("message")

        return JsonResponse({
                  "response": get_response(message)
})
        

    return JsonResponse({
        "response": "Invalid Request"
    })