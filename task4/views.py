from django.shortcuts import render

# Create your views here.
# Главная страница
def home(request):
    return render(request, 'fourth_task/home.html')

# Магазин
def store(request):
    games = ["Atomic Heart", "Cyberpunk 2077", "PayDay2"]
    return render(request, 'fourth_task/store.html', {"games": games})

# Корзина
def cart(request):
    return render(request, 'fourth_task/cart.html')
