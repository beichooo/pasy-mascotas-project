console.log("hello pasy");

//index page buttons

//buttons 'como adoptar'
let howAdoptBtn = document.getElementById("in-adoption-box");
let howAdoptPopup = document.getElementById("popup");

//buttons 'preguntas frecuentes'
let freQuestions = document.querySelector("#faq-box");
let faqPopup = document.querySelector("#faqPopup");

//popup for health message

function howAdoptShowPopup() {
  howAdoptPopup.style.display = "block";
}

function howAdoptClosePopup() {
  howAdoptPopup.style.display = "none";
}

howAdoptBtn.addEventListener("click", howAdoptShowPopup);

function faqShowPopup() {
  faqPopup.style.display = "block";
}

function faqClosePopup() {
  faqPopup.style.display = "none";
}

freQuestions.addEventListener("click", faqShowPopup);
