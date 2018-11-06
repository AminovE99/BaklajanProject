from django.shortcuts import render





def main(request):
    return render(request, 'baklajan/main_page.html', {}) # не так


def login(request):
    return render(request, 'baklajan/main_page.html', {})