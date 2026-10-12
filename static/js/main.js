(function () {
  const toggle = document.querySelector(".nav-toggle");
  const links = document.querySelector(".nav-links");
  if (toggle && links) {
    toggle.addEventListener("click", function () {
      const isOpen = links.classList.toggle("open");
      toggle.setAttribute("aria-expanded", String(isOpen));
      toggle.setAttribute("aria-label", isOpen ? "Close menu" : "Open menu");
      toggle.innerHTML = isOpen ? '<span aria-hidden="true">&times;</span>' : '<span aria-hidden="true">&#9776;</span>';
    });
  }

  const chatToggle = document.getElementById("chat-toggle");
  const chatPanel = document.getElementById("chat-panel");
  const chatClose = document.getElementById("chat-close");
  const chatForm = document.getElementById("chat-form");
  const chatInput = document.getElementById("chat-input");
  const chatLog = document.getElementById("chat-log");

  if (chatToggle && chatPanel) {
    chatToggle.addEventListener("click", function () {
      chatPanel.hidden = !chatPanel.hidden;
      chatToggle.hidden = !chatPanel.hidden;
      chatToggle.setAttribute("aria-expanded", String(!chatPanel.hidden));
      if (!chatPanel.hidden && chatInput) chatInput.focus();
    });
  }

  if (chatClose && chatToggle && chatPanel) {
    chatClose.addEventListener("click", function () {
      chatPanel.hidden = true;
      chatToggle.hidden = false;
      chatToggle.setAttribute("aria-expanded", "false");
      chatToggle.focus();
    });
  }

  function addLine(text, who) {
    const p = document.createElement("p");
    p.className = who;
    p.textContent = text;
    chatLog.appendChild(p);
    chatLog.scrollTop = chatLog.scrollHeight;
  }

  if (chatForm) {
    chatForm.addEventListener("submit", async function (event) {
      event.preventDefault();
      const message = chatInput.value.trim();
      if (!message) return;
      addLine(message, "user");
      chatInput.value = "";
      addLine("One moment, traveller...", "bot");
      const pending = chatLog.lastElementChild;
      const body = new FormData(chatForm);
      body.set("message", message);

      try {
        const response = await fetch("/chat/", { method: "POST", body: body });
        if (!response.ok) throw new Error("Chat request failed");
        const data = await response.json();
        pending.textContent = data.reply || "No reply received.";
      } catch (error) {
        pending.textContent = "Could not reach the assistant. Please try again.";
      }
    });
  }
})();
