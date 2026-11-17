document.addEventListener("DOMContentLoaded", () => {
  const year = new Date().getFullYear();
  const footer = document.querySelector(".footer-inner");

  if (footer) {
    const text = footer.querySelector("p:last-child");
    if (text) {
      text.textContent = `GitHub Pages demonstratie · ${year}`;
    }
  }
});
