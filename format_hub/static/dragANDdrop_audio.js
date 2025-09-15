
const dropArea_audio = document.getElementById("dropArea_audio");
const audioInput = document.getElementById("audioInput");

// Drag & Drop
dropArea_audio.addEventListener("dragover", (e) => {
  e.preventDefault();
  dropArea_audio.classList.add("dragover");
});

dropArea_audio.addEventListener("dragleave", () => {
  dropArea_audio.classList.remove("dragover");
});

dropArea_audio.addEventListener("drop", (e) => {
  e.preventDefault();
  dropArea_audio.classList.remove("dragover");
  
  const files = e.dataTransfer.files;
  if(files.length > 0){
    handleAudio(files[0]);
  }
});

// Click to select file
dropArea_audio.addEventListener("click", () => audioInput.click());
audioInput.addEventListener("change", () => {
  if(audioInput.files.length > 0){
    handleAudio(audioInput.files[0]);
  }
});

// مدیریت فایل انتخاب‌شده (برای نمایش یا ذخیره موقت در کلاینت)
function handleAudio(file){
  // فقط مطمئن بشیم فایل صوتی هست
  if(!file.type.startsWith("audio/")){
    alert("Please select an audio file!");
    return;
  }

  alert(`Selected audio: ${file.name} (${Math.round(file.size/1024)} KB)`);

  // حذف نمایش قبلی
  const oldFile = dropArea_audio.querySelector("p.selected-file");
  if(oldFile) oldFile.remove();
  const oldPlayer = dropArea_audio.querySelector("audio");
  if(oldPlayer) oldPlayer.remove();

  // نمایش نام فایل
  const fileNameDisplay = document.createElement("p");
  fileNameDisplay.textContent = `Selected: ${file.name}`;
  fileNameDisplay.style.marginTop = "10px";
  fileNameDisplay.classList.add("selected-file");
  dropArea_audio.appendChild(fileNameDisplay);

  // نمایش پلیر صوتی
  const audioPlayer = document.createElement("audio");
  audioPlayer.controls = true;
  audioPlayer.style.marginTop = "10px";

  const reader = new FileReader();
  reader.onload = function(e){
    audioPlayer.src = e.target.result;
  };
  reader.readAsDataURL(file);

  dropArea_audio.appendChild(audioPlayer);
}