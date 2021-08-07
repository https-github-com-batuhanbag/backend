//   Modal ---------------------------------------------------------

var modal = document.querySelector("#myModal");
var modalBtn = document.querySelector("#modalBtn");
var closebtn = document.querySelector("#close");

var signUpModal = document.querySelector("#signupMyModal");
var signUpBtn = document.querySelector(".signupBtn");

var closebtnSignUp = document.querySelector("#closeSignUpModal");
var modalSignupBtn = document.querySelector(".modalSignupBtn");
var relativeModal = document.querySelector("#userIcon");

relativeModal.onclick = function () {
  modal.style.display = "block";
};
modalSignupBtn.onclick = function () {
  signUpModal.style.display = "block";
  modal.style.display = "none";
};

signUpBtn.onclick = function () {
  signUpModal.style.display = "block";
};
closebtnSignUp.onclick = function () {
  signUpModal.style.display = "none";
};

modalBtn.onclick = function () {
  modal.style.display = "block";
};
closebtn.onclick = function () {
  modal.style.display = "none";
};
window.onclick = function (event) {
  if (event.target == modal || event.target == signUpModal) {
    modal.style.display = "none";
    signUpModal.style.display = "none";
  }
};
