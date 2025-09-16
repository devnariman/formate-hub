const timerText = document.getElementById("timerText");
const progressCircle = document.getElementById("progressCircle");
const loadingWidget = document.getElementById("loadingWidget");
const target_file = document.getElementById("target_file");
const temp_link = document.getElementById("temp_link");
const file_download = document.getElementById("file_download")


let duration = 30; // ثانیه
let current = duration;

const interval = setInterval(() => {
    current--;
    timerText.textContent = current;

      // زاویه دایره پر شده
    let angle = ((duration - current) / duration) * 360;
    progressCircle.style.background = `conic-gradient(#4ade80 ${angle}deg, #1e293b ${angle}deg)`;

    if (current <= 0) {
        clearInterval(interval);
        loadingWidget.classList.add("hidden");
        target_file.classList.add("target_file_show");
        file_download.href = temp_link.textContent
    }
}, 1000);