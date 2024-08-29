const images = ["images/image1.jpg", "images/image2.jpg", "images/image3.jpg"];
let currentIndex = 0;

const slide = document.getElementById('slide');
const prevButton = document.getElementById('prev');
const nextButton = document.getElementById('next');
const counter = document.getElementById('counter');

function updateSlide() {
    slide.src = images[currentIndex];
    counter.textContent = `Изображение ${currentIndex + 1} из ${images.length}`;
}

prevButton.addEventListener('click', () => {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    updateSlide();
});

nextButton.addEventListener('click', () => {
    currentIndex = (currentIndex + 1) % images.length;
    updateSlide();
});

// Инициализация
updateSlide();