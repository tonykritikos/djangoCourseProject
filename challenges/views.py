from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
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
    "december": "Read Django every day!"
}


# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path= reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


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
        response_data = render_to_string("challenges/challenge.html")
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This is not a supported month!</h1>")
