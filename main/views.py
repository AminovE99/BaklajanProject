from django.shortcuts import render



def main(request):
    if request.POST:
        id = request.POST.get('id','')
        form = request.POST.get('name','')
        print('Записать в бд')
    return render(request, 'baklajan/main_page.html', {'values': [1]})  # не так


def login(request):
    return render(request, 'baklajan/signin.html', {})
