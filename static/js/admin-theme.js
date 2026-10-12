(function () {
  const root = document.documentElement;
  const toggle = document.getElementById("admin-theme-toggle");
  if (!toggle) return;

  function updateButton() {
    const isLight = root.dataset.adminTheme === "light";
    toggle.textContent = isLight ? "Switch to dark mode" : "Switch to light mode";
    toggle.setAttribute("aria-pressed", String(isLight));
  }

  updateButton();
  toggle.addEventListener("click", function () {
    const nextTheme = root.dataset.adminTheme === "light" ? "dark" : "light";
    root.dataset.adminTheme = nextTheme;
    try {
      localStorage.setItem("mahin-admin-theme", nextTheme);
    } catch (error) {
      // Keep the selected theme for this page even when storage is unavailable.
    }
    updateButton();
  });
})();
