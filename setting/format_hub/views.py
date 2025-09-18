from django.shortcuts import render
from django.http import JsonResponse
import os
from django.conf import settings
import subprocess
import time
from PIL import Image
from django.http import HttpResponse
import shutil

class convertor():
    def __init__(self , file_name,all_type , formate):
        self.f_name = file_name
        self.format = formate
        self.type = all_type
        self.path = self.get_input_path()
        self.download_file = os.path.join(settings.MEDIA_ROOT, 'download')
        try:
            self.status = self.test_file()
        except:
            self.status = 110
        self.ext = os.path.splitext(self.f_name)[1]
        self.ext = self.ext[1:]
        self.html110 = """
        <html>
            <head>
                <meta http-equiv="refresh" content="3;url=/main" />
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        background-color: #f9f9f9;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                    }
                    .error-box {
                        background: #fff;
                        border: 1px solid #ddd;
                        border-radius: 6px;
                        padding: 30px 40px;
                        text-align: center;
                        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
                    }
                    .error-title {
                        font-size: 22px;
                        color: #d9534f;
                        margin-bottom: 10px;
                    }
                    .error-message {
                        font-size: 16px;
                        color: #555;
                        margin-bottom: 15px;
                    }
                    .redirect {
                        font-size: 14px;
                        color: #888;
                    }
                </style>
            </head>
            <body>
                <div class="error-box">
                    <div class="error-title">⚠ Base Error 110</div>
                    <div class="error-message">Something went wrong.</div>
                    <div class="redirect">Redirecting to main page in 3 seconds...</div>
                </div>
            </body>
        </html>
        """

        self.html120 = """
        <html>
            <head>
                <meta http-equiv="refresh" content="3;url=/main" />
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        background-color: #f9f9f9;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                    }
                    .error-box {
                        background: #fff;
                        border: 1px solid #ddd;
                        border-radius: 6px;
                        padding: 30px 40px;
                        text-align: center;
                        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
                    }
                    .error-title {
                        font-size: 22px;
                        color: #d9534f;
                        margin-bottom: 10px;
                    }
                    .error-message {
                        font-size: 16px;
                        color: #555;
                        margin-bottom: 15px;
                    }
                    .redirect {
                        font-size: 14px;
                        color: #888;
                    }
                </style>
            </head>
            <body>
                <div class="error-box">
                    <div class="error-title">⚠ No Category Selected</div>
                    <div class="error-message">Please choose a category before proceeding.</div>
                    <div class="redirect">Redirecting to main page in 3 seconds...</div>
                </div>
            </body>
        </html>
        """

        self.html160 = """
        <html>
            <head>
                <meta http-equiv="refresh" content="4;url=/main" />
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        background-color: #f9f9f9;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                    }
                    .error-box {
                        background: #fff;
                        border: 1px solid #e6e6e6;
                        border-radius: 8px;
                        padding: 28px 38px;
                        text-align: center;
                        box-shadow: 0 6px 20px rgba(0,0,0,0.08);
                        max-width: 420px;
                    }
                    .error-title {
                        font-size: 20px;
                        color: #d9534f;
                        margin-bottom: 8px;
                        font-weight: 700;
                    }
                    .error-message {
                        font-size: 15px;
                        color: #444;
                        margin-bottom: 16px;
                    }
                    .hint {
                        font-size: 13px;
                        color: #777;
                        margin-bottom: 18px;
                    }
                    .actions {
                        display: flex;
                        gap: 10px;
                        justify-content: center;
                    }
                    .btn {
                        padding: 8px 14px;
                        border-radius: 6px;
                        border: none;
                        text-decoration: none;
                        font-size: 14px;
                        cursor: pointer;
                        box-shadow: 0 2px 6px rgba(0,0,0,0.06);
                    }
                    .btn-primary {
                        background: #007bff;
                        color: #fff;
                    }
                    .btn-secondary {
                        background: transparent;
                        color: #007bff;
                        border: 1px solid #cfe3ff;
                    }
                </style>
            </head>
            <body>
                <div class="error-box" role="alert" aria-live="polite">
                    <div class="error-title">⚠ Already Converted</div>
                    <div class="error-message">This file has already been downloaded and converted once.</div>
                    <div class="hint">You will be redirected to the main page in 4 seconds.</div>
                    <div class="actions">
                        <a href="/main" class="btn btn-primary">Go to downloads</a>
                        <a href="/main" class="btn btn-secondary">Go to main now</a>
                    </div>
                </div>
            </body>
        </html>
        """

        self.html130 = """
        <html>
            <head>
                <meta http-equiv="refresh" content="3;url=/main" />
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        background-color: #f9f9f9;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                    }
                    .error-box {
                        background: #fff;
                        border: 1px solid #e6e6e6;
                        border-radius: 8px;
                        padding: 28px 38px;
                        text-align: center;
                        box-shadow: 0 6px 20px rgba(0,0,0,0.08);
                        max-width: 420px;
                    }
                    .error-title {
                        font-size: 20px;
                        color: #d9534f;
                        margin-bottom: 8px;
                        font-weight: 700;
                    }
                    .error-message {
                        font-size: 15px;
                        color: #444;
                        margin-bottom: 16px;
                    }
                    .hint {
                        font-size: 13px;
                        color: #777;
                        margin-bottom: 18px;
                    }
                    .actions {
                        display: flex;
                        gap: 10px;
                        justify-content: center;
                    }
                    .btn {
                        padding: 8px 14px;
                        border-radius: 6px;
                        border: none;
                        text-decoration: none;
                        font-size: 14px;
                        cursor: pointer;
                        box-shadow: 0 2px 6px rgba(0,0,0,0.06);
                    }
                    .btn-primary {
                        background: #007bff;
                        color: #fff;
                    }
                    .btn-secondary {
                        background: transparent;
                        color: #007bff;
                        border: 1px solid #cfe3ff;
                    }
                </style>
            </head>
            <body>
                <div class="error-box" role="alert" aria-live="polite">
                    <div class="error-title">⚠ Unsupported Image Format</div>
                    <div class="error-message">The format of your uploaded image is not supported by our site.</div>
                    <div class="hint">Redirecting to main page in 3 seconds...</div>
                    <div class="actions">
                        <a href="/main" class="btn btn-primary">Go to main now</a>
                    </div>
                </div>
            </body>
        </html>
        """

        self.html140_150 = """
        <html>
            <head>
                <meta http-equiv="refresh" content="3;url=/main" />
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        background-color: #f9f9f9;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                    }
                    .error-box {
                        background: #fff;
                        border: 1px solid #e6e6e6;
                        border-radius: 8px;
                        padding: 28px 38px;
                        text-align: center;
                        box-shadow: 0 6px 20px rgba(0,0,0,0.08);
                        max-width: 460px;
                    }
                    .error-title {
                        font-size: 20px;
                        color: #d9534f;
                        margin-bottom: 8px;
                        font-weight: 700;
                    }
                    .error-message {
                        font-size: 15px;
                        color: #444;
                        margin-bottom: 16px;
                    }
                    .hint {
                        font-size: 13px;
                        color: #777;
                        margin-bottom: 18px;
                    }
                    .actions {
                        display: flex;
                        gap: 10px;
                        justify-content: center;
                    }
                    .btn {
                        padding: 8px 14px;
                        border-radius: 6px;
                        border: none;
                        text-decoration: none;
                        font-size: 14px;
                        cursor: pointer;
                        box-shadow: 0 2px 6px rgba(0,0,0,0.06);
                    }
                    .btn-primary {
                        background: #007bff;
                        color: #fff;
                    }
                    .btn-secondary {
                        background: transparent;
                        color: #007bff;
                        border: 1px solid #cfe3ff;
                    }
                </style>
            </head>
            <body>
                <div class="error-box" role="alert" aria-live="polite">
                    <div class="error-title">⚠ Unsupported File Format</div>
                    <div class="error-message">
                        The format of your uploaded file is not supported. <br>
                        This applies to images, videos, and audio files.
                    </div>
                    <div class="hint">Redirecting to the main page in 3 seconds...</div>
                    <div class="actions">
                        <a href="/main" class="btn btn-primary">Go to main now</a>
                    </div>
                </div>
            </body>
        </html>
        """

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
                elif self.ext == "gif":
                    if self.format == "png":
                        self.result_path = self.convert_gif_to_png()
                    elif self.format == "jpg":
                        self.result_path = self.convert_gif_to_jpg()
                    elif self.format == "gif":
                        self.result_path = self.path
                    elif self.format == "bmp":
                        self.result_path = self.convert_gif_to_bmp()
                elif self.ext == "bmp":
                    if self.format == "png":
                        self.result_path = self.convert_bmp_to_png()
                    elif self.format == "jpg":
                        self.result_path = self.convert_bmp_to_jpg()
                    elif self.format == "gif":
                        self.result_path = self.convert_bmp_to_gif()
                    elif self.format == "bmp":
                        self.result_path = self.path
                else:
                    self.status = 130

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
                else:
                    self.status = 140

            elif self.type == "audio":
                if self.ext == "mp3":
                    if self.format == "mp3":
                        self.result_path = self.path
                    elif self.format == "wav":
                        self.result_path = self.convert_mp3_to_wav()
                    elif self.format == "ogg":
                        self.result_path = self.convert_mp3_to_ogg()
                    elif self.format == "flac":
                        self.result_path = self.convert_mp3_to_flac()
                elif self.ext == "wav":
                    if self.format == "mp3":
                        self.result_path = self.convert_wav_to_mp3()
                    elif self.format == "wav":
                        self.result_path = self.path
                    elif self.format == "ogg":
                        self.result_path = self.convert_wav_to_ogg()
                    elif self.format == "flac":
                        self.result_path = self.convert_wav_to_flac()
                elif self.ext == "ogg":
                    if self.format == "mp3":
                        self.result_path = self.convert_ogg_to_mp3()
                    elif self.format == "wav":
                        self.result_path = self.convert_ogg_to_wav()
                    elif self.format == "ogg":
                        self.result_path = self.path
                    elif self.format == "flac":
                        self.result_path = self.convert_ogg_to_flac()
                elif self.ext == "flac":
                    if self.format == "mp3":
                        self.result_path = self.convert_flac_to_mp3()
                    elif self.format == "wav":
                        self.result_path = self.convert_flac_to_wav()
                    elif self.format == "ogg":
                        self.result_path = self.convert_flac_to_ogg()
                    elif self.format == "flac":
                        self.result_path = self.path
                else:
                    self.status = 150
      
            else:
                self.status = 120
        else:
            self.status = 160

    def convert_flac_to_mp3(self):
        # مسیر فولدر خروجی
        add = os.path.join(settings.MEDIA_ROOT, 'download')
        os.makedirs(add, exist_ok=True)

        # اسم فایل خروجی با پسوند .mp3
        file_name = os.path.splitext(self.f_name)[0] + ".mp3"
        output_path = os.path.join(add, file_name)

        # اجرای ffmpeg برای تبدیل FLAC به MP3
        subprocess.run([
            "ffmpeg",
            "-i", self.path,        # ورودی FLAC
            "-c:a", "libmp3lame",   # کدک MP3
            "-q:a", "2",            # کیفیت خروجی (0 بهترین، 9 بدترین)
            output_path
        ], check=True)

        return output_path

    def convert_flac_to_wav(self):
        # مسیر فولدر خروجی
        add = os.path.join(settings.MEDIA_ROOT, 'download')
        os.makedirs(add, exist_ok=True)

        # اسم فایل خروجی با پسوند .wav
        file_name = os.path.splitext(self.f_name)[0] + ".wav"
        output_path = os.path.join(add, file_name)

        # اجرای ffmpeg برای تبدیل FLAC به WAV
        subprocess.run([
            "ffmpeg",
            "-i", self.path,   # ورودی FLAC
            output_path        # خروجی WAV
        ], check=True)

        return output_path

    def convert_flac_to_ogg(self):
        # مسیر فولدر خروجی
        add = os.path.join(settings.MEDIA_ROOT, 'download')
        os.makedirs(add, exist_ok=True)

        # اسم فایل خروجی با پسوند .ogg
        file_name = os.path.splitext(self.f_name)[0] + ".ogg"
        output_path = os.path.join(add, file_name)

        # اجرای ffmpeg برای تبدیل FLAC به OGG
        subprocess.run([
            "ffmpeg",
            "-i", self.path,       # ورودی FLAC
            "-c:a", "libvorbis",   # کدک OGG (Vorbis)
            output_path
        ], check=True)

        return output_path


    def convert_wav_to_ogg(self):
        # مسیر فولدر خروجی
        add = os.path.join(settings.MEDIA_ROOT, 'download')
        os.makedirs(add, exist_ok=True)

        # اسم فایل خروجی با پسوند .ogg
        file_name = os.path.splitext(self.f_name)[0] + ".ogg"
        output_path = os.path.join(add, file_name)

        # اجرای ffmpeg برای تبدیل WAV به OGG
        subprocess.run([
            "ffmpeg",
            "-i", self.path,       # ورودی WAV
            "-c:a", "libvorbis",   # کدک OGG (Vorbis)
            output_path
        ], check=True)

        return output_path

    def convert_wav_to_flac(self):
        # مسیر فولدر خروجی
        add = os.path.join(settings.MEDIA_ROOT, 'download')
        os.makedirs(add, exist_ok=True)

        # اسم فایل خروجی با پسوند .flac
        file_name = os.path.splitext(self.f_name)[0] + ".flac"
        output_path = os.path.join(add, file_name)

        # اجرای ffmpeg برای تبدیل WAV به FLAC
        subprocess.run([
            "ffmpeg",
            "-i", self.path,   # ورودی WAV
            "-c:a", "flac",    # کدک FLAC
            output_path
        ], check=True)

        return output_path

    def convert_ogg_to_mp3(self):
        # مسیر فولدر خروجی
        add = os.path.join(settings.MEDIA_ROOT, 'download')
        os.makedirs(add, exist_ok=True)

        # اسم فایل خروجی با پسوند .mp3
        file_name = os.path.splitext(self.f_name)[0] + ".mp3"
        output_path = os.path.join(add, file_name)

        # اجرای ffmpeg برای تبدیل OGG به MP3
        subprocess.run([
            "ffmpeg",
            "-i", self.path,        # ورودی OGG
            "-c:a", "libmp3lame",   # کدک MP3
            "-q:a", "2",            # کیفیت خروجی (0 بهترین، 9 بدترین)
            output_path
        ], check=True)

        return output_path

    def convert_ogg_to_wav(self):
        # مسیر فولدر خروجی
        add = os.path.join(settings.MEDIA_ROOT, 'download')
        os.makedirs(add, exist_ok=True)

        # اسم فایل خروجی با پسوند .wav
        file_name = os.path.splitext(self.f_name)[0] + ".wav"
        output_path = os.path.join(add, file_name)

        # اجرای ffmpeg برای تبدیل OGG به WAV
        subprocess.run([
            "ffmpeg",
            "-i", self.path,   # ورودی OGG
            output_path        # خروجی WAV
        ], check=True)

        return output_path

    def convert_ogg_to_flac(self):
        # مسیر فولدر خروجی
        add = os.path.join(settings.MEDIA_ROOT, 'download')
        os.makedirs(add, exist_ok=True)

        # اسم فایل خروجی با پسوند .flac
        file_name = os.path.splitext(self.f_name)[0] + ".flac"
        output_path = os.path.join(add, file_name)

        # اجرای ffmpeg برای تبدیل OGG به FLAC
        subprocess.run([
            "ffmpeg",
            "-i", self.path,   # ورودی OGG
            "-c:a", "flac",    # کدک FLAC
            output_path
        ], check=True)

        return output_path


    def convert_mp3_to_flac(self):
        # مسیر پوشه خروجی
        add = os.path.join(settings.MEDIA_ROOT, 'download')
        os.makedirs(add, exist_ok=True)

        # اسم فایل خروجی با پسوند .flac
        file_name = os.path.splitext(self.f_name)[0] + ".flac"
        output_path = os.path.join(add, file_name)

        # اجرای ffmpeg برای تبدیل MP3 به FLAC
        subprocess.run([
            "ffmpeg",
            "-i", self.path,      # ورودی MP3
            "-c:a", "flac",       # کدک FLAC
            output_path
        ], check=True)

        return output_path

    def convert_wav_to_mp3(self):
        # مسیر پوشه خروجی
        add = os.path.join(settings.MEDIA_ROOT, 'download')
        os.makedirs(add, exist_ok=True)

        # اسم فایل خروجی با پسوند .mp3
        file_name = os.path.splitext(self.f_name)[0] + ".mp3"
        output_path = os.path.join(add, file_name)

        # اجرای ffmpeg برای تبدیل WAV به MP3
        subprocess.run([
            "ffmpeg",
            "-i", self.path,        # ورودی WAV
            "-c:a", "libmp3lame",   # کدک MP3
            "-q:a", "2",            # کیفیت خروجی (0 بهترین، 9 بدترین)
            output_path
        ], check=True)

        return output_path


    def convert_mp3_to_ogg(self):
        # مسیر پوشه خروجی
        add = os.path.join(settings.MEDIA_ROOT, 'download')
        os.makedirs(add, exist_ok=True)

        # اسم فایل خروجی با پسوند .ogg
        file_name = os.path.splitext(self.f_name)[0] + ".ogg"
        output_path = os.path.join(add, file_name)

        # اجرای ffmpeg برای تبدیل MP3 به OGG
        subprocess.run([
            "ffmpeg",
            "-i", self.path,    # ورودی MP3
            "-c:a", "libvorbis", # کدک OGG (Vorbis)
            output_path
        ], check=True)

        return output_path


    def convert_mp3_to_wav(self):
        # مسیر پوشه خروجی
        add = os.path.join(settings.MEDIA_ROOT, 'download')
        os.makedirs(add, exist_ok=True)

        # اسم فایل خروجی با پسوند .wav
        file_name = os.path.splitext(self.f_name)[0] + ".wav"
        output_path = os.path.join(add, file_name)

        # اجرای ffmpeg برای تبدیل MP3 به WAV
        subprocess.run([
            "ffmpeg",
            "-i", self.path,   # ورودی MP3
            output_path        # خروجی WAV
        ], check=True)

        return output_path

    def convert_bmp_to_gif(self):
        # مسیر پوشه خروجی
        add = os.path.join(settings.MEDIA_ROOT, 'download')
        os.makedirs(add, exist_ok=True)

        # اسم فایل خروجی (هم‌نام فایل ورودی، ولی با پسوند .gif)
        file_name = os.path.splitext(self.f_name)[0] + ".gif"
        output_path = os.path.join(add, file_name)

        # باز کردن تصویر (BMP)
        img = Image.open(self.path)

        # تبدیل به پالت رنگی برای GIF
        gif_img = img.convert("P", palette=Image.ADAPTIVE)

        # ذخیره به صورت GIF
        gif_img.save(output_path, "GIF")

        return output_path


    def convert_bmp_to_jpg(self):
        # مسیر پوشه خروجی
        add = os.path.join(settings.MEDIA_ROOT, 'download')
        os.makedirs(add, exist_ok=True)

        # اسم فایل خروجی (هم‌نام فایل ورودی، ولی با پسوند .jpg)
        file_name = os.path.splitext(self.f_name)[0] + ".jpg"
        output_path = os.path.join(add, file_name)

        # باز کردن تصویر (BMP)
        img = Image.open(self.path)

        # چون JPG شفافیت رو پشتیبانی نمی‌کنه → تبدیل به RGB
        rgb_img = img.convert("RGB")

        # ذخیره به صورت JPG
        rgb_img.save(output_path, "JPEG")

        return output_path


    def convert_bmp_to_png(self):
        # مسیر پوشه خروجی
        add = os.path.join(settings.MEDIA_ROOT, 'download')
        os.makedirs(add, exist_ok=True)

        # اسم فایل خروجی (هم‌نام فایل ورودی، ولی با پسوند .png)
        file_name = os.path.splitext(self.f_name)[0] + ".png"
        output_path = os.path.join(add, file_name)

        # باز کردن تصویر (BMP)
        img = Image.open(self.path)

        # تبدیل به RGB برای سازگاری (اگر 8bit باشه هم درست میشه)
        rgb_img = img.convert("RGB")

        # ذخیره به صورت PNG
        rgb_img.save(output_path, "PNG")

        return output_path



    def convert_gif_to_bmp(self):
        # مسیر پوشه خروجی
        add = os.path.join(settings.MEDIA_ROOT, 'download')
        os.makedirs(add, exist_ok=True)

        # اسم فایل خروجی (هم‌نام فایل ورودی، ولی با پسوند .bmp)
        file_name = os.path.splitext(self.f_name)[0] + ".bmp"
        output_path = os.path.join(add, file_name)

        # باز کردن تصویر (GIF)
        img = Image.open(self.path)

        # چون BMP شفافیت نداره → تبدیل به RGB
        rgb_img = img.convert("RGB")

        # ذخیره به صورت BMP
        rgb_img.save(output_path, "BMP")

        return output_path


    def convert_gif_to_jpg(self):
        # مسیر پوشه خروجی
        add = os.path.join(settings.MEDIA_ROOT, 'download')
        os.makedirs(add, exist_ok=True)

        # اسم فایل خروجی
        file_name = os.path.splitext(self.f_name)[0] + ".jpg"
        output_path = os.path.join(add, file_name)

        # باز کردن تصویر
        img = Image.open(self.path)

        # تبدیل به RGB چون JPG شفافیت نداره
        rgb_img = img.convert("RGB")

        # ذخیره به صورت JPG
        rgb_img.save(output_path, "JPEG")

        return output_path


    def convert_gif_to_png(self):
        # مسیر پوشه خروجی
        add = os.path.join(settings.MEDIA_ROOT, 'download')
        os.makedirs(add, exist_ok=True)

        # اسم فایل بدون پسوند + پسوند PNG
        file_name = os.path.splitext(self.f_name)[0] + ".png"
        output_path = os.path.join(add, file_name)

        # باز کردن تصویر
        img = Image.open(self.path)

        # ذخیره به صورت PNG
        img.save(output_path, "PNG")

        return output_path

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

    def remove_this_file(self):
        if os.path.isfile(self.path):
            os.remove(self.path)
        else:
            None

    def make_download_link(self):
        # مسیر کامل فایل
        file_path = self.result_path
        # تبدیل مسیر کامل به مسیر نسبی نسبت به MEDIA_ROOT
        relative_path = os.path.relpath(file_path, settings.MEDIA_ROOT)
        # مسیر قابل استفاده در URL برای مرورگر
        link_download = settings.MEDIA_URL + relative_path.replace("\\", "/")
        return link_download

def show_main(request):
    return render(request, 'main.html')


def show_sending(request, file_name,all_type = "", format = ""):
    time.sleep(1)
    file_convertor = convertor(file_name , all_type , format)

    if file_convertor.status == True:
        if file_convertor.ext == file_convertor.format:
            try: 
                file_convertor.result_path = shutil.move(file_convertor.result_path, file_convertor.download_file) 
            except:
                file_convertor.remove_this_file()
                adde = file_convertor.result_path
                file_convertor.result_path = adde.replace("image" , "download")
        else:    
            file_convertor.remove_this_file()


        link_download = file_convertor.make_download_link()

        context = {
            "link_download": link_download,
        }
        return render(request, 'sending.html', context=context)
    elif file_convertor.status == 110:
        return HttpResponse(file_convertor.html110)
    elif file_convertor.status == 120:
        return HttpResponse(file_convertor.html120)
    elif file_convertor.status == 160:
        return HttpResponse(file_convertor.html160)
    elif file_convertor.status == 130:
        return HttpResponse(file_convertor.html130) 
    elif file_convertor.status == 140 or file_convertor == 150 : 
        return HttpResponse(file_convertor.html140_150)

    
def show_sending2(request, file_name,all_type = ""):
    html = """
    <html>
        <head>
            <meta http-equiv="refresh" content="3;url=/main" />
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f9f9f9;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                .error-box {
                    background: #fff;
                    border: 1px solid #e6e6e6;
                    border-radius: 8px;
                    padding: 28px 38px;
                    text-align: center;
                    box-shadow: 0 6px 20px rgba(0,0,0,0.08);
                    max-width: 420px;
                }
                .error-title {
                    font-size: 20px;
                    color: #d9534f;
                    margin-bottom: 8px;
                    font-weight: 700;
                }
                .error-message {
                    font-size: 15px;
                    color: #444;
                    margin-bottom: 16px;
                }
                .hint {
                    font-size: 13px;
                    color: #777;
                    margin-bottom: 18px;
                }
                .actions {
                    display: flex;
                    gap: 10px;
                    justify-content: center;
                }
                .btn {
                    padding: 8px 14px;
                    border-radius: 6px;
                    border: none;
                    text-decoration: none;
                    font-size: 14px;
                    cursor: pointer;
                    box-shadow: 0 2px 6px rgba(0,0,0,0.06);
                }
                .btn-primary {
                    background: #007bff;
                    color: #fff;
                }
                .btn-secondary {
                    background: transparent;
                    color: #007bff;
                    border: 1px solid #cfe3ff;
                }
            </style>
        </head>
        <body>
            <div class="error-box" role="alert" aria-live="polite">
                <div class="error-title">⚠ No Output Format Selected</div>
                <div class="error-message">You did not select any output format while converting your file.</div>
                <div class="hint">Redirecting to main page in 3 seconds...</div>
                <div class="actions">
                    <a href="/main" class="btn btn-primary">Go to main now</a>
                </div>
            </div>
        </body>
    </html>
    """
    return HttpResponse(html)


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