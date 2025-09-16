from django.shortcuts import render
from django.http import JsonResponse
import os
from django.conf import settings
import time
from PIL import Image

class convertor():
    def __init__(self , file_name,all_type , formate):
        self.f_name = file_name
        self.format = formate
        self.type = all_type
        self.path = self.get_input_path()
        # self.download_path = 

    def get_input_path(self):
        if self.type == "image":
            image_folder = os.path.join(settings.MEDIA_ROOT, 'image')
            file_path = os.path.join(image_folder, self.f_name)
            return file_path
    



def show_main(request):
    return render(request, 'main.html')


def show_sending(request, file_name,all_type, format):


    time.sleep(1)
    image_folder = os.path.join(settings.MEDIA_ROOT, 'image')
    file_path = os.path.join(image_folder, file_name)  # اینجا اسم دقیق فایل

    
    if os.path.exists(file_path):
        print("File exists ✅")
    else:
        print("File does not exist ❌")


    a = convertor(file_name , all_type, format)
    print(a.path) 
    return render(request, 'sending.html')






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



def upload_video(request):
    if request.method == 'POST' and request.FILES.get('video'):
        uploaded_file = request.FILES['video']
        
        # مسیر پوشه video داخل media
        video_folder = os.path.join(settings.MEDIA_ROOT, 'video')
        os.makedirs(video_folder, exist_ok=True)  # ایجاد پوشه اگر وجود نداشت
        
        # مسیر نهایی فایل
        save_path = os.path.join(video_folder, uploaded_file.name)
        
        # ذخیره فایل
        with open(save_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
        
        # پاسخ موفق
        return JsonResponse({'status': 'success', 'filename': uploaded_file.name})
    
    # اگر درخواست POST نبود یا فایل وجود نداشت
    return JsonResponse({'status': 'fail'}, status=400)