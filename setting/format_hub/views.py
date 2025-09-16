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
        self.download_file = os.path.join(settings.MEDIA_ROOT, 'download')
        self.status = self.test_file()
        self.ext = os.path.splitext(self.f_name)[1]
        self.ext = self.ext[1:]
        if self.ext == "png":
            self.convert_to_jpg()
        


    def test_file(self):
        if os.path.exists(self.path):
            return True
        else:
            return False
        

    def convert_to_jpg(self):
    # باز کردن عکس
        add = os.path.join(settings.MEDIA_ROOT, 'download')
        file_name = name_only = os.path.splitext(self.f_name)[0]
        file_name = file_name + ".jpg"
        out_put = os.path.join(add, file_name)
        img = Image.open(self.path)
        rgb_img = img.convert("RGB")   # JPG از شفافیت (alpha channel) پشتیبانی نمی‌کنه
        rgb_img.save(out_put, "JPEG")
                

    def get_input_path(self):
        if self.type == "image":
            image_folder = os.path.join(settings.MEDIA_ROOT, 'image')
            file_path = os.path.join(image_folder, self.f_name)
            return file_path
        elif self.type == "video":
            image_folder = os.path.join(settings.MEDIA_ROOT, 'video')
            file_path = os.path.join(image_folder, self.f_name)
            return file_path
        elif self.type == "audio":
            image_folder = os.path.join(settings.MEDIA_ROOT, 'audio')
            file_path = os.path.join(image_folder, self.f_name)
            return file_path   



def show_main(request):
    return render(request, 'main.html')


def show_sending(request, file_name,all_type, format):


    time.sleep(1)
    a = convertor(file_name , all_type, format)
 
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