video_type = ""
image_type = ""
audio_type = ""

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// ---------------------------------------------------
let start_pannel = document.getElementById("pannel")
let video_pannel = document.getElementById("video_pannel")
let video_back_btn = document.getElementById('video_back_btn')
let image_pannel = document.getElementById("image_pannel")
let image_back_btn = document.getElementById('img_back_btn')
let audio_pannel = document.getElementById("audio_pannel")
let audio_back_btn = document.getElementById('audio_back_btn')

image_back_btn.addEventListener('click', function() {
    image_pannel.classList.remove("active")
    start_pannel.classList.add("active")
});

audio_back_btn.addEventListener('click', function() {
    audio_pannel.classList.remove("active")
    start_pannel.classList.add("active")
});

video_back_btn.addEventListener('click', function() {
    video_pannel.classList.remove("active")
    start_pannel.classList.add("active")
});

function chooseFormat(type){
    if (type === "video"){
        start_pannel.classList.remove("active")
        video_pannel.classList.add("active")
    }else if (type === "image"){
        start_pannel.classList.remove("active")
        image_pannel.classList.add("active")
    }else if (type === "audio"){
        start_pannel.classList.remove("active")
        audio_pannel.classList.add("active")
    }

}











// ---------------------------------------------------
const dropArea = document.getElementById("dropArea_img");
const fileInput = document.getElementById("imageInput");
const dropText = document.getElementById("dropText");
const convertBtn = document.getElementById("img_Convert_btn");

// وقتی روی dropArea کلیک شد، input باز بشه
dropArea.addEventListener("click", () => {
    fileInput.click();
});

// وقتی فایل انتخاب شد از پنجره
fileInput.addEventListener("change", (e) => {
    if (e.target.files.length > 0) {
        dropText.textContent = e.target.files[0].name;
    }
});

// جلوگیری از رفتار پیش‌فرض مرورگر
["dragenter", "dragover", "dragleave", "drop"].forEach(eventName => {
    dropArea.addEventListener(eventName, (e) => e.preventDefault());
    dropArea.addEventListener(eventName, (e) => e.stopPropagation());
});

// وقتی فایلی درگ شد روش
dropArea.addEventListener("drop", (e) => {
    const files = e.dataTransfer.files;
    if (files.length > 0) {
        dropText.textContent = files[0].name;
        fileInput.files = files; // ست کردن به input تا بتونی بعدا آپلودش کنی
    }
});

// آپلود فایل و تغییر href
convertBtn.addEventListener("click", function(e) {
    e.preventDefault(); // جلوگیری از پرش اولیه

    if (fileInput.files.length === 0) {
        alert("Please select an image file first.");
        return;
    }

    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append("file", file);

    // حالا فایل رو بفرست
    fetch("/upload_image/", {
        method: "POST",
        body: formData,
    headers: {
        'X-CSRFToken': getCookie('csrftoken')  // حتماً کلید همین باشه
    },
    credentials: 'same-origin'  // اضافه کن تا کوکی‌ها ارسال بشن
    })
    .then(response => response.json())
    .then(data => {
        // بعد از آپلود موفق، ریدایرکت به صفحه test
        window.location.href = `/sending/${data.filename}/${image_type}`;
    })
    .catch(() => {
        alert("Error uploading file.");
    });
});












// ---------------------------------------------------
// گرفتن المان‌ها
const videoDropArea = document.getElementById("dropArea");
const videoFileInput = document.getElementById("videoInput");
const videoDropText = document.getElementById("cideo_drop_text"); // توجه: اسم id رو از HTML گرفتم
const videoConvertBtn = document.getElementById("video_Convert_btn"); // دکمه آپلود ویدیو

// وقتی روی dropArea کلیک شد، input باز بشه
videoDropArea.addEventListener("click", () => {
    videoFileInput.click();
});

// وقتی فایل انتخاب شد از پنجره
videoFileInput.addEventListener("change", (e) => {
    if (e.target.files.length > 0) {
        videoDropText.textContent = e.target.files[0].name;
    }
});

// جلوگیری از رفتار پیش‌فرض مرورگر برای drag & drop
["dragenter", "dragover", "dragleave", "drop"].forEach(eventName => {
    videoDropArea.addEventListener(eventName, (e) => e.preventDefault());
    videoDropArea.addEventListener(eventName, (e) => e.stopPropagation());
});

// وقتی فایلی درگ شد روش
videoDropArea.addEventListener("drop", (e) => {
    const files = e.dataTransfer.files;
    if (files.length > 0) {
        videoDropText.textContent = files[0].name;
        videoFileInput.files = files; // ست کردن به input تا بتونی بعدا آپلودش کنی
    }
});

// آپلود فایل و تغییر href
videoConvertBtn.addEventListener("click", function(e) {
    e.preventDefault(); // جلوگیری از پرش صفحه

    if (videoFileInput.files.length === 0) {
        alert("Please select a video file first.");
        return;
    }

    const file = videoFileInput.files[0];
    const formData = new FormData();
    formData.append("video", file);

    fetch("/upload_video/", { // مسیر سرور برای ویدیو
        method: "POST",
        body: formData,
    headers: {
        'X-CSRFToken': getCookie('csrftoken')  // حتماً کلید همین باشه
    },
    credentials: 'same-origin'  // اضافه کن تا کوکی‌ها ارسال بشن
    })
    .then(response => response.json())
    .then(data => {
        // بعد از آپلود موفق، ریدایرکت
        // دقت کن که video_type باید قبل از این تعریف شود یا ثابت باشه
        window.location.href = `/sending_video/${data.filename}/${video_type}`;
    })
    .catch(() => {
        alert("Error uploading video.");
    });
});












// --------------------------------------------------------
// گرفتن المان‌ها
const audioDropArea = document.getElementById("dropArea_audio");
const audioFileInput = document.getElementById("audioInput");
const audioDropText = document.getElementById("audio_drop_text");
const audioConvertBtn = document.getElementById("audio_Convert_btn");

// کلیک روی dropArea → باز شدن پنجره انتخاب فایل
audioDropArea.addEventListener("click", () => {
    audioFileInput.click();
});

// وقتی از پنجره فایل انتخاب شد
audioFileInput.addEventListener("change", (e) => {
    if (e.target.files.length > 0) {
        audioDropText.textContent = e.target.files[0].name;
    }
});

// جلوگیری از رفتار پیش‌فرض مرورگر در درگ
["dragenter", "dragover", "dragleave", "drop"].forEach(eventName => {
    audioDropArea.addEventListener(eventName, (e) => {
        e.preventDefault();
        e.stopPropagation();
    });
});

// وقتی فایل روی dropArea درگ شد
audioDropArea.addEventListener("drop", (e) => {
    const files = e.dataTransfer.files;
    if (files.length > 0) {
        audioDropText.textContent = files[0].name;
        audioFileInput.files = files; // فایل رو تو input هم ست کن
    }
});

// آپلود فایل و ریدایرکت
audioConvertBtn.addEventListener("click", function(e) {
    e.preventDefault();

    if (audioFileInput.files.length === 0) {
        alert("Please select an audio file first.");
        return;
    }

    const file = audioFileInput.files[0];
    const formData = new FormData();
    formData.append("audio", file);

    fetch("/upload_audio/", {
        method: "POST",
        body: formData,
    headers: {
        'X-CSRFToken': getCookie('csrftoken')  // حتماً کلید همین باشه
    },
    credentials: 'same-origin'  // اضافه کن تا کوکی‌ها ارسال بشن
    })
    .then(response => response.json())
    .then(data => {
        // بعد از آپلود موفق
        window.location.href = `/sending/${data.filename}/${audio_type}`; 
    })
    .catch(() => {
        alert("Error uploading audio.");
    });
});














// --------------------------------------------------------
jpg_checkbox = document.getElementById("jpg_checkbox");
png_checkbox = document.getElementById("png_checkbox");
gif_checkbox = document.getElementById("gif_checkbox");
bmp_checkbox = document.getElementById("bmp_checkbox");

function chooseFormat_image(format) {
    if (format === "jpg") {
        jpg_checkbox.checked = true;
        png_checkbox.checked = false;
        gif_checkbox.checked = false;
        bmp_checkbox.checked = false;
    }   else if (format === "png") {
        jpg_checkbox.checked = false;
        png_checkbox.checked = true;
        gif_checkbox.checked = false;
        bmp_checkbox.checked = false;
    }   else if (format === "gif") {
        jpg_checkbox.checked = false;
        png_checkbox.checked = false;
        gif_checkbox.checked = true;
        bmp_checkbox.checked = false;
    }   else if (format === "bmp") {
        jpg_checkbox.checked = false;
        png_checkbox.checked = false;
        gif_checkbox.checked = false;
        bmp_checkbox.checked = true;
    }
    image_type = format
}
// --------------------------------------------------------
mp4_checkbox = document.getElementById("mp4_checkbox");
avi_checkbox = document.getElementById("AVI_checkbox");
mov_checkbox = document.getElementById("MOV_checkbox");
mkv_checkbox = document.getElementById("MKV_checkbox");

function chooseFormat_video(format) {
    if (format === "mp4") {
        mp4_checkbox.checked = true;
        avi_checkbox.checked = false;
        mov_checkbox.checked = false;
        mkv_checkbox.checked = false;
    }   else if (format === "AVI") {
        mp4_checkbox.checked = false;
        avi_checkbox.checked = true;
        mov_checkbox.checked = false;
        mkv_checkbox.checked = false;
    }   else if (format === "MOV") {
        mp4_checkbox.checked = false;
        avi_checkbox.checked = false;
        mov_checkbox.checked = true;
        mkv_checkbox.checked = false;
    }   else if (format === "MKV") {
        mp4_checkbox.checked = false;
        avi_checkbox.checked = false;
        mov_checkbox.checked = false;
        mkv_checkbox.checked = true;
    }
    video_type = format
}
// --------------------------------------------------------
mp3_checkbox = document.getElementById("mp3_checkbox");
wav_checkbox = document.getElementById("wav_checkbox");
aac_checkbox = document.getElementById("ogg_checkbox");
flac_checkbox = document.getElementById("flac_checkbox");

function chooseFormat_audio(format) {
    if (format === "mp3") {
        mp3_checkbox.checked = true;
        wav_checkbox.checked = false;
        aac_checkbox.checked = false;
        flac_checkbox.checked = false;
    }   else if (format === "wav") {
        mp3_checkbox.checked = false;
        wav_checkbox.checked = true;
        aac_checkbox.checked = false;
        flac_checkbox.checked = false;
    }   else if (format === "ogg") {
        mp3_checkbox.checked = false;
        wav_checkbox.checked = false;
        aac_checkbox.checked = true;
        flac_checkbox.checked = false;
    }   else if (format === "flac") {
        mp3_checkbox.checked = false;
        wav_checkbox.checked = false;
        aac_checkbox.checked = false;
        flac_checkbox.checked = true;
    }
    audio_type = format
}
// ---------------------------------------------------