from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def films(request):
    films = [
        {"title": "Whiplash", "rating": 8.5},
        {"title": "The Dictator", "rating": 6.5},
        {"title": "Resident Evil", "rating": 7.5}
    ]

    context = {"films": films}
    return render(request, 'films.html', context)

