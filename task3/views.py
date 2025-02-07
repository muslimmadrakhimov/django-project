from django.shortcuts import render

# Create your views here.
# Главная страница
def home(request):
    return render(request, 'third_task/home.html')

# Магазин
def store(request):
    items = ["Игровая консоль", "Геймпад", "VR-шлем"]
    return render(request, 'third_task/store.html', {"items": items})

# Корзина
def cart(request):
    return render(request, 'third_task/cart.html')