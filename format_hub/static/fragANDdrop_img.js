
const dropArea_img = document.getElementById("dropArea_img");
const imageInput = document.getElementById("imageInput");

// Drag & Drop
dropArea_img.addEventListener("dragover", (e) => {
  e.preventDefault();
  dropArea_img.classList.add("dragover");
});

dropArea_img.addEventListener("dragleave", () => {
  dropArea_img.classList.remove("dragover");
});

dropArea_img.addEventListener("drop", (e) => {
  e.preventDefault();
  dropArea_img.classList.remove("dragover");
  
  const files = e.dataTransfer.files;
  if(files.length > 0){
    handleImage(files[0]);
  }
});

// Click to select file
dropArea_img.addEventListener("click", () => imageInput.click());
imageInput.addEventListener("change", () => {
  if(imageInput.files.length > 0){
    handleImage(imageInput.files[0]);
  }
});

// مدیریت فایل انتخاب‌شده (برای نمایش یا ذخیره موقت در کلاینت)
function handleImage(file){
  // فقط مطمئن بشیم فایل تصویر هست
  if(!file.type.startsWith("image/")){
    alert("Please select an image file!");
    return;
  }

  alert(`Selected image: ${file.name} (${Math.round(file.size/1024)} KB)`);

  // حذف نمایش قبلی
  const old = dropArea_img.querySelector("p.selected-file");
  if(old) old.remove();

  // نمایش نام فایل
  const fileNameDisplay = document.createElement("p");
  fileNameDisplay.textContent = `Selected: ${file.name}`;
  fileNameDisplay.style.marginTop = "10px";
  fileNameDisplay.classList.add("selected-file");
  dropArea_img.appendChild(fileNameDisplay);

  // نمایش پیش‌نمایش تصویر
  const reader = new FileReader();
  reader.onload = function(e){
    const preview = document.createElement("img");
    preview.src = e.target.result;
    preview.style.maxWidth = "100%";
    preview.style.marginTop = "10px";

    // حذف پیش‌نمایش قبلی
    const oldPreview = dropArea_img.querySelector("img");
    if(oldPreview) oldPreview.remove();

    dropArea_img.appendChild(preview);
  };
  reader.readAsDataURL(file);
}