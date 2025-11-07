document.addEventListener("DOMContentLoaded", function() {
  const bodyId = document.body.id;

  if (bodyId === "home-page") {
    alert("Hey, this is Home Page!");
  } else if (bodyId === "about-page") {
    alert("Hey, this is About Page!");
  } else if (bodyId === "contact-page") {
    alert("Hey, this is Contact Page!");
  }
});
