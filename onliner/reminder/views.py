from django.shortcuts import render

def post_list(request):
    return render(request, 'reminder/post_list.html', {})