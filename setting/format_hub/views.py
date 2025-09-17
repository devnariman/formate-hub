from django.shortcuts import render
from django.http import JsonResponse
import os
from django.conf import settings
import subprocess
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
        if self.status == True:


            if self.type == "image":
                if self.ext == "png":
                    if self.format == "jpg":
                        self.result_path = self.convert_to_jpg()
                    elif self.format == "png":
                        self.result_path = self.path
                    elif self.format == "gif":
                        self.result_path = self.convert_to_gif()
                    elif self.format == "bmp":
                        self.result_path = self.convert_to_bmp()
                elif self.ext == "jpg":
                    if self.format == "png":
                        self.result_path = self.convert_to_png()
                    elif self.format == "jpg":
                        self.result_path = self.path
                    elif self.format == "gif":
                        self.result_path = self.convert_to_gif()
                    elif self.format == "bmp":
                        self.result_path = self.convert_to_bmp()

                
            
            elif self.type == "video":
                if self.ext == "mp4":
                    if self.format == "MKV":
                        self.result_path = self.convert_mp4_to_mkv()
                    elif self.format == "AVI":
                        self.result_path = self.convert_mp4_to_avi()
                    elif self.format == "MOV":
                        self.result_path = self.convert_mp4_to_mov()
                    elif self.format == "mp4":
                        self.result_path = self.path
                elif self.ext == "mkv":
                    if self.format == "mp4":
                        self.result_path = self.convert_mkv_to_mp4()
                    elif self.format == "AVI":
                        self.result_path = self.convert_mkv_to_avi()
                    elif self.format == "MOV":
                        self.result_path = self.convert_mkv_to_mov()
                    elif self.format == "mkv":
                        self.result_path = self.path
                elif self.ext == "mov":
                    if self.format == "mp4":
                        self.result_path = self.convert_mov_to_mp4()
                    elif self.format == "AVI":
                        self.result_path = self.convert_mov_to_avi()
                    elif self.format == "MOV":
                        self.result_path = self.path
                    elif self.format == "mkv":
                        self.result_path = self.convert_mov_to_mkv()
                elif self.ext == "avi":
                    if self.format == "mp4":
                        self.result_path = self.convert_avi_to_mp4()
                    elif self.format == "AVI":
                        self.result_path = self.path
                    elif self.format == "MOV":
                        self.result_path = self.convert_avi_to_mov()
                    elif self.format == "mkv":
                        self.result_path = self.convert_avi_to_mkv()

            elif self.type == "audio":
                print(False)
                print(self.ext)
                print(self.format)
            else:
                None
        else:
            None

    def convert_avi_to_mkv(self):
        # مسیر فولدر خروجی
        add = os.path.join(settings.MEDIA_ROOT, 'download')
        os.makedirs(add, exist_ok=True)

        # اسم فایل بدون پسوند + پسوند mkv
        file_name = os.path.splitext(self.f_name)[0] + ".mkv"
        output_path = os.path.join(add, file_name)

        # re-encode برای سازگاری کامل
        subprocess.run([
            "ffmpeg",
            "-i", self.path,
            "-c:v", "libx264",  # ویدیو → H.264
            "-c:a", "aac",      # صدا → AAC
            output_path
        ], check=True)

        return output_path

    def convert_mov_to_mkv(self):
        # مسیر فولدر خروجی
        add = os.path.join(settings.MEDIA_ROOT, 'download')
        os.makedirs(add, exist_ok=True)

        # اسم فایل بدون پسوند + پسوند mkv
        file_name = os.path.splitext(self.f_name)[0] + ".mkv"
        output_path = os.path.join(add, file_name)

        # دستور ffmpeg برای تغییر فرمت
        subprocess.run([
            "ffmpeg",
            "-i", self.path,    # مسیر فایل ورودی MOV
            "-c", "copy",       # فقط تغییر container بدون encode دوباره
            output_path
        ], check=True)

        return output_path

    def convert_avi_to_mov(self):
        # مسیر فولدر خروجی
        add = os.path.join(settings.MEDIA_ROOT, 'download')
        os.makedirs(add, exist_ok=True)

        # اسم فایل بدون پسوند + پسوند mov
        file_name = os.path.splitext(self.f_name)[0] + ".mov"
        output_path = os.path.join(add, file_name)

        # re-encode برای سازگاری کامل
        subprocess.run([
            "ffmpeg",
            "-i", self.path,
            "-c:v", "libx264",  # ویدیو → H.264
            "-c:a", "aac",      # صدا → AAC
            output_path
        ], check=True)

        return output_path


    def convert_avi_to_mp4(self):
        # مسیر فولدر خروجی
        add = os.path.join(settings.MEDIA_ROOT, 'download')
        os.makedirs(add, exist_ok=True)

        # اسم فایل بدون پسوند + پسوند mp4
        file_name = os.path.splitext(self.f_name)[0] + ".mp4"
        output_path = os.path.join(add, file_name)

        # re-encode برای سازگاری کامل
        subprocess.run([
            "ffmpeg",
            "-i", self.path,
            "-c:v", "libx264",  # ویدیو → H.264
            "-c:a", "aac",      # صدا → AAC
            output_path
        ], check=True)

        return output_path


    def convert_mov_to_avi(self):
        # مسیر فولدر خروجی
        add = os.path.join(settings.MEDIA_ROOT, 'download')
        os.makedirs(add, exist_ok=True)

        # اسم فایل بدون پسوند + پسوند avi
        file_name = os.path.splitext(self.f_name)[0] + ".avi"
        output_path = os.path.join(add, file_name)

        # دستور ffmpeg برای تغییر فرمت
        subprocess.run([
            "ffmpeg",
            "-i", self.path,    # مسیر فایل ورودی MOV
            "-c", "copy",       # فقط تغییر container (بدون encode دوباره)
            output_path
        ], check=True)

        return output_path


    def convert_mkv_to_mov(self):
        # مسیر فولدر خروجی
        add = os.path.join(settings.MEDIA_ROOT, 'download')
        os.makedirs(add, exist_ok=True)

        # اسم فایل بدون پسوند + پسوند mov
        file_name = os.path.splitext(self.f_name)[0] + ".mov"
        output_path = os.path.join(add, file_name)

        # دستور ffmpeg برای تغییر فرمت
        subprocess.run([
            "ffmpeg",
            "-i", self.path,    # فایل ورودی
            "-c", "copy",       # فقط تغییر container (بدون افت کیفیت)
            output_path
        ], check=True)

        return output_path

    def convert_mov_to_mp4(self):
        # مسیر فولدر خروجی
        add = os.path.join(settings.MEDIA_ROOT, 'download')
        os.makedirs(add, exist_ok=True)

        # اسم فایل بدون پسوند + پسوند mp4
        file_name = os.path.splitext(self.f_name)[0] + ".mp4"
        output_path = os.path.join(add, file_name)

        # دستور ffmpeg برای تغییر فرمت
        subprocess.run([
            "ffmpeg",
            "-i", self.path,   # مسیر فایل ورودی
            "-c", "copy",      # فقط تغییر container بدون re-encode
            output_path
        ], check=True)

        return output_path


    def convert_mkv_to_avi(self):
        add = os.path.join(settings.MEDIA_ROOT, 'download')
        os.makedirs(add, exist_ok=True)

        file_name = os.path.splitext(self.f_name)[0] + ".avi"
        output_path = os.path.join(add, file_name)

        # re-encode برای سازگاری کامل با AVI
        subprocess.run([
            "ffmpeg",
            "-i", self.path,
            "-c:v", "libx264",   # ویدیو → H.264
            "-c:a", "mp3",       # صدا → MP3
            output_path
        ], check=True)

        return output_path


    def convert_mkv_to_mp4(self):
        # مسیر فولدر خروجی
        add = os.path.join(settings.MEDIA_ROOT, 'download')
        os.makedirs(add, exist_ok=True)

        # اسم فایل بدون پسوند + پسوند mp4
        file_name = os.path.splitext(self.f_name)[0] + ".mp4"
        output_path = os.path.join(add, file_name)

        # دستور ffmpeg برای تغییر فرمت
        subprocess.run([
            "ffmpeg",
            "-i", self.path,    # مسیر فایل ورودی
            "-c", "copy",       # فقط تغییر container بدون encode دوباره
            output_path
        ], check=True)

        return output_path

    def convert_mp4_to_mov(self):
        # مسیر فولدر خروجی
        add = os.path.join(settings.MEDIA_ROOT, 'download')
        os.makedirs(add, exist_ok=True)

        # اسم فایل بدون پسوند + پسوند mov
        file_name = os.path.splitext(self.f_name)[0] + ".mov"
        output_path = os.path.join(add, file_name)

        # دستور ffmpeg برای تغییر فرمت
        subprocess.run([
            "ffmpeg",
            "-i", self.path,    # مسیر فایل ورودی
            "-c", "copy",       # فقط تغییر container بدون encode دوباره
            output_path
        ], check=True)

        return output_path

    def test_file(self):
        if os.path.exists(self.path):
            return True
        else:
            return False
        
    def convert_mp4_to_avi(self):
        # مسیر فولدر خروجی
        add = os.path.join(settings.MEDIA_ROOT, 'download')
        os.makedirs(add, exist_ok=True)

        # اسم فایل بدون پسوند + پسوند avi
        file_name = os.path.splitext(self.f_name)[0] + ".avi"
        output_path = os.path.join(add, file_name)

        # دستور ffmpeg برای تغییر فرمت
        subprocess.run([
            "ffmpeg",
            "-i", self.path,    # مسیر فایل ورودی
            "-c", "copy",       # فقط تغییر container بدون encode دوباره
            output_path
        ], check=True)

        return output_path


    def convert_mp4_to_mkv(self):
        # مسیر فولدر خروجی
        add = os.path.join(settings.MEDIA_ROOT, 'download')
        os.makedirs(add, exist_ok=True)

        # اسم فایل بدون پسوند + پسوند mkv
        file_name = os.path.splitext(self.f_name)[0] + ".mkv"
        output_path = os.path.join(add, file_name)

        # دستور ffmpeg برای تغییر فرمت
        subprocess.run([
            "ffmpeg",
            "-i", self.path,    # مسیر فایل ورودی
            "-c", "copy",       # فقط تغییر container بدون encode دوباره
            output_path
        ], check=True)

        return output_path


    def convert_to_png(self):
        # مسیر پوشه خروجی
        add = os.path.join(settings.MEDIA_ROOT, 'download')

        # اسم فایل بدون پسوند + پسوند PNG
        file_name = os.path.splitext(self.f_name)[0] + ".png"

        # مسیر نهایی خروجی
        out_put = os.path.join(add, file_name)

        # باز کردن تصویر
        img = Image.open(self.path)

        # JPG → PNG (تبدیل به RGB برای سازگاری)
        rgb_img = img.convert("RGB")

        # ذخیره به صورت PNG
        rgb_img.save(out_put, "PNG")

        return out_put

    def convert_to_jpg(self):
        add = os.path.join(settings.MEDIA_ROOT, 'download')
        file_name = name_only = os.path.splitext(self.f_name)[0]
        file_name = file_name + ".jpg"
        out_put = os.path.join(add, file_name)
        img = Image.open(self.path)
        rgb_img = img.convert("RGB")   # JPG از شفافیت (alpha channel) پشتیبانی نمی‌کنه
        rgb_img.save(out_put, "JPEG")
        return out_put
                

    def convert_to_gif(self):
        # مسیر پوشه خروجی
        add = os.path.join(settings.MEDIA_ROOT, 'download')
        # اسم فایل بدون پسوند
        file_name = os.path.splitext(self.f_name)[0] + ".gif"
        # مسیر نهایی خروجی
        out_put = os.path.join(add, file_name)
        # باز کردن تصویر
        img = Image.open(self.path)
        # برای GIF بهتره RGB باشه، ولی اگه شفافیت میخوای RGBA بذار
        rgb_img = img.convert("RGBA")
        # ذخیره به صورت GIF
        rgb_img.save(out_put, "GIF")
        return out_put

    def convert_to_bmp(self):
        # مسیر پوشه خروجی
        add = os.path.join(settings.MEDIA_ROOT, 'download')
        # اسم فایل بدون پسوند + پسوند BMP
        file_name = os.path.splitext(self.f_name)[0] + ".bmp"
        # مسیر نهایی خروجی
        out_put = os.path.join(add, file_name)
        # باز کردن تصویر
        img = Image.open(self.path)
        # تبدیل به RGB چون BMP شفافیت نمی‌تونه داشته باشه
        rgb_img = img.convert("RGB")
        # ذخیره به صورت BMP
        rgb_img.save(out_put, "BMP")
        return out_put
    
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
    a = convertor(file_name , all_type , format)
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