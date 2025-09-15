from django.shortcuts import render
from django.http import JsonResponse
import os
from django.conf import settings

def show_main(request):
    return render(request, 'main.html')

# def upload_image(request):
#     if request.method == 'POST' and request.FILES.get('file'):
#         uploaded_file = request.FILES['file']
#         save_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)
#         os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
#         with open(save_path, 'wb+') as destination:
#             for chunk in uploaded_file.chunks():
#                 destination.write(chunk)
#         return JsonResponse({'status': 'success', 'filename': uploaded_file.name})
#     return JsonResponse({'status': 'fail'}, status=400)



def upload_image(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        
        # مسیر پوشه image داخل media
        image_folder = os.path.join(settings.MEDIA_ROOT, 'image')
        os.makedirs(image_folder, exist_ok=True)  # ایجاد پوشه اگر وجود نداشت
        
        # مسیر نهایی فایل
        save_path = os.path.join(image_folder, uploaded_file.name)
        
        # ذخیره فایل
        with open(save_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
        
        return JsonResponse({'status': 'success', 'filename': uploaded_file.name})
    
    return JsonResponse({'status': 'fail'}, status=400)



def upload_audio(request):
    if request.method == 'POST' and request.FILES.get('audio'):  # کلید مطابق JS
        uploaded_file = request.FILES['audio']
        
        # مسیر پوشه audio داخل media
        audio_folder = os.path.join(settings.MEDIA_ROOT, 'audio')
        os.makedirs(audio_folder, exist_ok=True)  # ایجاد پوشه اگر وجود نداشت
        
        # مسیر نهایی فایل
        save_path = os.path.join(audio_folder, uploaded_file.name)
        
        # ذخیره فایل
        with open(save_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
        
        return JsonResponse({'status': 'success', 'filename': uploaded_file.name})
    
    return JsonResponse({'status': 'fail'}, status=400)


