from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Eat no meat for the month!",
    "february": "Walk 20 mins every day!",
    "march": "Read Django every day!",
    "april": "Eat no meat for the month!",
    "may": "Walk 20 mins every day!",
    "june": "Read Django every day!",
    "july": "Eat no meat for the month!",
    "august": "Walk 20 mins every day!",
    "september": "Read Django every day!",
    "october": "Eat no meat for the month!",
    "november": "Walk 20 mins every day!",
    "december": None
}


# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())
    
    return render(request, "challenges/index.html", {"months": months})


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month!")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {"text": challenge_text, "month_name": month})
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
