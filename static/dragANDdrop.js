const dropArea = document.getElementById("dropArea");
const videoInput = document.getElementById("videoInput");

// Drag & Drop
dropArea.addEventListener("dragover", (e) => {
  e.preventDefault();
  dropArea.classList.add("dragover");
});

dropArea.addEventListener("dragleave", () => {
  dropArea.classList.remove("dragover");
});

dropArea.addEventListener("drop", (e) => {
  e.preventDefault();
  dropArea.classList.remove("dragover");
  
  const files = e.dataTransfer.files;
  if(files.length > 0){
    handleFile(files[0]);
  }
});

// Click to select file
dropArea.addEventListener("click", () => videoInput.click());
videoInput.addEventListener("change", () => {
  if(videoInput.files.length > 0){
    handleFile(videoInput.files[0]);
  }
});

// مدیریت فایل انتخاب شده (برای نمایش یا ذخیره موقت در کلاینت)
function handleFile(file){
  alert(`Selected file: ${file.name} (${Math.round(file.size/1024)} KB)`);
  
  // مثال: نمایش نام فایل در پنل
  const fileNameDisplay = document.createElement("p");
  fileNameDisplay.textContent = `Selected: ${file.name}`;
  fileNameDisplay.style.marginTop = "10px";
  
  // حذف نمایش قبلی
  const old = dropArea.querySelector("p.selected-file");
  if(old) old.remove();
  fileNameDisplay.classList.add("selected-file");
  dropArea.appendChild(fileNameDisplay);
  
  // اینجا می‌تونی بعدا کد آپلود یا پردازش فایل رو اضافه کنی
}
