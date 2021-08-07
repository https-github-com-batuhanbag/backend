var $shareModal = $(".share-modal");

var toggleModal = function () {
  $shareModal.toggleClass("share-modal--open");
  $shareModal.toggleClass("share-modal--close");
};

$(".js-share-button").on("click", function (e) {
  e.preventDefault();
  toggleModal();
});

$(document).keyup(function (e) {
  if (e.keyCode === 27 && $shareModal.hasClass("share-modal--open")) {
    $shareModal.removeClass("share-modal--open");
    $shareModal.addClass("share-modal--close");
  }
});

$("#closeModalButton").on("click", function (e) {
  e.preventDefault();
  toggleModal();
});
