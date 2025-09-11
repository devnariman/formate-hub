let video_pannel = document.getElementById("video_pannel")
let pannel = document.getElementById("pannel")
let video_Convert_btn = document.getElementById("video_Convert_btn")
let mp4_checkbox = document.getElementById("mp4_checkbox")
let AVI_checkbox = document.getElementById("AVI_checkbox")
let MOV_checkbox = document.getElementById("MOV_checkbox")
let MKV_checkbox = document.getElementById("MKV_checkbox")
let type_video = ""
let type_image = ""
let video_back_btn = document.getElementById("video_back_btn")
let img_back_btn = document.getElementById("img_back_btn")
let image_pannel = document.getElementById("image_pannel")
let jpg_checkbox = document.getElementById("jpg_checkbox")
let png_checkbox = document.getElementById("png_checkbox")
let gif_checkbox = document.getElementById("gif_checkbox")
let bmp_checkbox = document.getElementById("bmp_checkbox")
let audio_pannel = document.getElementById("audio_pannel")
let audio_back_btn = document.getElementById("audio_back_btn")
let mp3_checkbox = document.getElementById("mp3_checkbox")
let wav_checkbox = document.getElementById("wav_checkbox")
let ogg_checkbox = document.getElementById("ogg_checkbox")
let flac_checkbox = document.getElementById("flac_checkbox")
let type_audio = ""

function chooseFormat_audio(type) {
    if (type == "mp3"){
        mp3_checkbox.checked = true
        wav_checkbox.checked = false
        ogg_checkbox.checked = false
        flac_checkbox.checked = false
        type_audio = "mp3"
    }else if (type == "wav"){
        mp3_checkbox.checked = false
        wav_checkbox.checked = true
        ogg_checkbox.checked = false
        flac_checkbox.checked = false
        type_audio = "wav"
    }else if (type == "ogg"){
        mp3_checkbox.checked = false
        wav_checkbox.checked = false
        ogg_checkbox.checked = true
        flac_checkbox.checked = false
        type_audio = "ogg"
    }else if (type == "flac"){
        mp3_checkbox.checked = false
        wav_checkbox.checked = false
        ogg_checkbox.checked = false
        flac_checkbox.checked = true
        type_audio = "flac"
    }
}

audio_back_btn.addEventListener("click", ()=>{
    audio_pannel.classList.remove("active")
    pannel.classList.add("active")
})

img_back_btn.addEventListener("click", ()=>{
    pannel.classList.add("active")
    image_pannel.classList.remove("active")
})

video_Convert_btn.addEventListener("click", ()=>{
    if (type_video != ""){
        alert("You chose " + type_video + " format")
    }else{
        alert("Please choose a format")
    }
})

video_back_btn.addEventListener("click", ()=>{
    video_pannel.classList.remove("active")
    pannel.classList.add("active")
})

function chooseFormat_video(type) {
    if (type == "mp4"){
        mp4_checkbox.checked = true
        AVI_checkbox.checked = false
        MOV_checkbox.checked = false
        MKV_checkbox.checked = false
        type_video = "mp4"
    }else if (type == "AVI"){
        mp4_checkbox.checked = false
        AVI_checkbox.checked = true
        MOV_checkbox.checked = false
        MKV_checkbox.checked = false
        type_video = "AVI"
    }else if (type == "MOV"){
        mp4_checkbox.checked = false
        AVI_checkbox.checked = false
        MOV_checkbox.checked = true
        MKV_checkbox.checked = false
        type_video = "MOV"
    }else if (type == "MKV"){
        mp4_checkbox.checked = false
        AVI_checkbox.checked = false
        MOV_checkbox.checked = false
        MKV_checkbox.checked = true
        type_video = "MKV"
    }
}

function chooseFormat_image(type) {
    console.log(type)
    if (type == "jpg"){
        jpg_checkbox.checked = true
        png_checkbox.checked = false
        gif_checkbox.checked = false
        bmp_checkbox.checked = false
        type_image = "jpg"
    }else if (type == "png"){
        jpg_checkbox.checked = false
        png_checkbox.checked = true
        gif_checkbox.checked = false
        bmp_checkbox.checked = false
        type_image = "png"
    }else if (type == "gif"){
        jpg_checkbox.checked = false
        png_checkbox.checked = false
        gif_checkbox.checked = true
        bmp_checkbox.checked = false
        type_image = "gif"
    }else if (type == "bmp"){
        jpg_checkbox.checked = false
        png_checkbox.checked = false
        gif_checkbox.checked = false
        bmp_checkbox.checked = true
        type_image = "bmp"
    }
}

function chooseFormat(type) {
    console.log(type)

    if (type == "video"){
        pannel.classList.remove("active")
        video_pannel.classList.add("active")
    }else if (type == "image"){
        pannel.classList.remove("active")
        image_pannel.classList.add("active")
    }else if (type == "audio"){
        pannel.classList.remove("active")
        audio_pannel.classList.add("active")
    }
}


