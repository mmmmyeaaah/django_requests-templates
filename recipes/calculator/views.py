from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def omlet_view(request):
    servings = int(request.GET.get('servings', 1))
    context = {
        'recipe': {
            'яйца, шт': DATA['omlet']['яйца, шт'] * servings,
            'молоко, л': DATA['omlet']['молоко, л'] * servings,
            'соль, ч.л.': DATA['omlet']['соль, ч.л.'] * servings,
        }
    }
    return render(request, 'calculator/index.html', context)


def pasta_view(request):
    servings = int(request.GET.get('servings', 1))
    context = {
        'recipe': {
            'макароны, г': DATA['pasta']['макароны, г'] * servings,
            'сыр, г': DATA['pasta']['сыр, г'] * servings,
        }
    }
    return render(request, 'calculator/index.html', context)


def buter_view(request):
    servings = int(request.GET.get('servings', 1))
    context = {
        'recipe': {
            'хлеб, ломтик': DATA['buter']['хлеб, ломтик'] * servings,
            'колбаса, ломтик': DATA['buter']['колбаса, ломтик'] * servings,
            'сыр, ломтик': DATA['buter']['сыр, ломтик'] * servings,
            'помидор, ломтик': DATA['buter']['помидор, ломтик'] * servings,
        }
    }
    return render(request, 'calculator/index.html', context)


def home_view(request):
    template_name = 'calculator/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'omlet': reverse('omlet'),
        'buter': reverse('buter'),
        'pasta': reverse('pasta')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


