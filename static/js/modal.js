var modal = document.querySelector("#myModal");
var modalBtn = document.querySelector("#modalBtn");
var closebtn = document.querySelector("#close");
var forgotModal = document.querySelector("#forgotpasswordmodal");

var signUpModal = document.querySelector("#signupMyModal");
var signUpBtn = document.querySelector(".signupBtn");
var closebtnSignUp = document.querySelector("#closeSignUpModal");
var modalSignupBtn = document.querySelector(".modalSignupBtn");
var relativeModal = document.querySelector("#userIcon");
var forgotModalClose = document.querySelector(".closeFP");
var trailnone = document.querySelector(".trail");

var forgotpassword = document.querySelector(".loginboxa");

forgotpassword.onclick = function () {
  forgotModal.style.display = "block";
  modal.style.display = "none";
};

forgotModalClose.onclick = function () {
  forgotModal.style.display = "none";
  trailnone.style.display = "grid";
};

relativeModal.onclick = function () {
  modal.style.display = "block";
};
modalSignupBtn.onclick = function () {
  signUpModal.style.display = "block";
  modal.style.display = "none";
};

signUpBtn.onclick = function () {
  signUpModal.style.display = "block";
  trailnone.style.display = "none";
};
closebtnSignUp.onclick = function () {
  signUpModal.style.display = "none";
  trailnone.style.display = "grid";
};

modalBtn.onclick = function () {
  modal.style.display = "block";
  trailnone.style.display = "none";
};
closebtn.onclick = function () {
  modal.style.display = "none";
  trailnone.style.display = "grid";
};
window.onclick = function (event) {
  if (
    event.target == modal ||
    event.target == signUpModal ||
    event.target == forgotModal
  ) {
    modal.style.display = "none";
    signUpModal.style.display = "none";
    forgotModal.style.display = "none";
    trailnone.style.display = "grid";
  }
};
