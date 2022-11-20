from django.shortcuts import render, HttpResponse

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


def recipe_view(request, recipe):
    servings = 1
    data_for_context = dict()
    context = dict()
    if request.GET:
        servings = int(request.GET.get('qnt'))
    if recipe in DATA.keys():
        for item, value in DATA[recipe].items():
            data_for_context[item] = round(value * servings, 2)
        context = {
            'recipe': data_for_context
        }
    return render(request, 'calculator/index.html', context=context)


