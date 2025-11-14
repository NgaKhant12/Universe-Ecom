document.querySelectorAll(".nav-link").forEach((link) => {
  link.addEventListener("click", () => {
    const navbarCollapse = document.querySelector(".navbar-collapse");
    const bsCollapse = new bootstrap.Collapse(navbarCollapse, {
      toggle: false,
    });
    bsCollapse.hide();

    console.log("Link clicked:", link.classList);
    // Remove 'activve' from all links
    document
      .querySelectorAll(".nav-link")
      .forEach((l) => l.classList.remove("active"));

    // Add 'activve' to the clicked link
    link.classList.add("active");
  });
});




// // JS: add / remove .scrolled class on scroll
// document.addEventListener('DOMContentLoaded', function () {
//   const navbar = document.getElementById('navbar');
//   if (!navbar) return;

//   // threshold in px when navbar should become solid
//   const scrollThreshold = 50;

//   const onScroll = () => {
//     if (window.scrollY > scrollThreshold) {
//       if (!navbar.classList.contains('scrolled')) navbar.classList.add('scrolled');
//     } else {
//       if (navbar.classList.contains('scrolled')) navbar.classList.remove('scrolled');
//     }
//   };

//   // run once on load
//   onScroll();

//   // throttled scroll for performance
//   let ticking = false;
//   window.addEventListener('scroll', function () {
//     if (!ticking) {
//       window.requestAnimationFrame(function () {
//         onScroll();
//         ticking = false;
//       });
//       ticking = true;
//     }
//   });
// });
