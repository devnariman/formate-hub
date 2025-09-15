from django.shortcuts import render

# این ویو فایل main.html رو نشون میده
def show_main(request):
    return render(request, 'main.html')
