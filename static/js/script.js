var swiper = new Swiper(".slide-container", {
  slidesPerView: 6,
  spaceBetween: 30,
  slidesPerGroup: 1,
  loop: true,
  centerSlide: "true",
  grabCursor: "true",
  fade: "true",
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
    dynamicBullets: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});