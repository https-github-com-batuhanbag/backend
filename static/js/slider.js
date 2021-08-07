// Slider(all Slides in a container)
const slider = document.querySelector(".slider");
// All trails
const trail = document.querySelector(".trail").querySelectorAll("div");

// Transform value
let value = 0;
// trail index number
let trailValue = 0;
// interval (Duration)
let interval = 4000;

// Function to slide forward
const slide = (condition) => {
  // CLear interval
  clearInterval(start);
  // update value and trailValue
  condition === "increase" ? initiateINC() : initiateDEC();
  // move slide
  move(value, trailValue);
  // Restart Animation
  animate();
  // start interal for slides back
  start = setInterval(() => slide("increase"), interval);
};

// function for increase(forward, next) configuration
const initiateINC = () => {
  // Remove active from all trails
  trail.forEach((cur) => cur.classList.remove("active"));
  // increase transform value
  value === 80 ? (value = 0) : (value += 20);
  // update trailValue based on value
  trailUpdate();
};

// function for decrease(backward, previous) configuration
const initiateDEC = () => {
  // Remove active from all trails
  trail.forEach((cur) => cur.classList.remove("active"));
  // decrease transform value
  value === 0 ? (value = 80) : (value -= 20);
  // update trailValue based on value
  trailUpdate();
};

// function to transform slide
const move = (S, T) => {
  // transform slider
  slider.style.transform = `translateX(-${S}%)`;
  //add active class to the current trail
  trail[T].classList.add("active");
};
const h1 = document.querySelectorAll(".sliderh1");
const a = document.querySelectorAll(".sliderA");
const sliderButton = document.querySelectorAll(".sliderButton");
const tl = gsap.timeline({ defaults: { duration: 0.6, ease: "power2.inOut" } });
tl.from(".bg", { x: "-100%", opacity: 0 })
  .from(a, { opacity: 0 }, "-=0.3")
  .from(h1, { opacity: 0, y: "30px" }, "-=0.3")
  .from(sliderButton, { opacity: 0, y: "-40px" }, "-=0.8");

// function to restart animation
const animate = () => tl.restart();

// function to update trailValue based on slide value
const trailUpdate = () => {
  if (value === 0) {
    trailValue = 0;
  } else if (value === 20) {
    trailValue = 1;
  } else if (value === 40) {
    trailValue = 2;
  } else if (value === 60) {
    trailValue = 3;
  } else {
    trailValue = 4;
  }
};

// Start interval for slides
let start = setInterval(() => slide("increase"), interval);

// Next  and  Previous button function (SVG icon with different classes)
document.querySelectorAll("svg").forEach((cur) => {
  // Assign function based on the class Name("next" and "prev")
  cur.addEventListener("click", () =>
    cur.classList.contains("next") ? slide("increase") : slide("decrease")
  );
});

// function to slide when trail is clicked
const clickCheck = (e) => {
  // CLear interval
  clearInterval(start);
  // remove active class from all trails
  trail.forEach((cur) => cur.classList.remove("active"));
  // Get selected trail
  const check = e.target;
  // add active class
  check.classList.add("active");

  // Update slide value based on the selected trail
  if (check.classList.contains("box1")) {
    value = 0;
  } else if (check.classList.contains("box2")) {
    value = 20;
  } else if (check.classList.contains("box3")) {
    value = 40;
  } else if (check.classList.contains("box4")) {
    value = 60;
  } else {
    value = 80;
  }
  // update trail based on value
  trailUpdate();
  // transfrom slide
  move(value, trailValue);
  // start animation
  animate();
  // start interval
  start = setInterval(() => slide("increase"), interval);
};

// Add function to all trails
trail.forEach((cur) => cur.addEventListener("click", (ev) => clickCheck(ev)));

const touchSlide = (() => {
  let start, move, change, sliderWidth;

  slider.addEventListener("touchstart", (e) => {
    start = e.touches[0].clientX;
    sliderWidth = slider.clientWidth / trail.length;
  });

  slider.addEventListener("touchmove", (e) => {
    e.preventDefault();
    move = e.touches[0].clientX;
    change = start - move;
  });

  const mobile = (e) => {
    change > sliderWidth / 4 ? slide("increase") : null;
    change * -1 > sliderWidth / 4 ? slide("decrease") : null;

    [start, move, change, sliderWidth] = [0, 0, 0, 0];
  };
  slider.addEventListener("touchend", mobile);
})();
