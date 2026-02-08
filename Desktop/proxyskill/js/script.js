// Mobile menu
const menuBtn = document.getElementById("menuBtn");
const mobileMenu = document.getElementById("mobileMenu");

menuBtn.addEventListener("click", () => {
  mobileMenu.classList.toggle("hidden");
});

// Theme toggle
const toggle = document.getElementById("themeToggle");
toggle.addEventListener("click", () => {
  document.documentElement.classList.toggle("dark");
});

// Formspree submit
const form = document.getElementById("contactForm");
const status = document.getElementById("formStatus");

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const data = new FormData(form);

  const res = await fetch(form.action, {
    method: "POST",
    body: data,
    headers: { "Accept": "application/json" }
  });

  if (res.ok) {
    status.textContent = "✅ Message sent successfully!";
    form.reset();
  } else {
    status.textContent = "❌ Failed. Try again.";
  }
});
