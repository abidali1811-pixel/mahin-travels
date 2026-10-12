(function () {
  const toggle = document.querySelector(".nav-toggle");
  const links = document.querySelector(".nav-links");
  if (toggle && links) {
    toggle.addEventListener("click", function () {
      links.classList.toggle("open");
    });
  }

  const chatToggle = document.getElementById("chat-toggle");
  const chatPanel = document.getElementById("chat-panel");
  const chatForm = document.getElementById("chat-form");
  const chatInput = document.getElementById("chat-input");
  const chatLog = document.getElementById("chat-log");

  if (chatToggle && chatPanel) {
    chatPanel.hidden = true;
    chatPanel.style.display = "none";
    chatToggle.addEventListener("click", function () {
      chatPanel.hidden = !chatPanel.hidden;
      chatPanel.style.display = chatPanel.hidden ? "none" : "flex";
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
      addLine("Thinking…", "bot");
      const pending = chatLog.lastElementChild;

      const body = new FormData();
      body.append("message", message);
      const csrf = chatForm.querySelector("[name=csrfmiddlewaretoken]");
      if (csrf) body.append("csrfmiddlewaretoken", csrf.value);

      try {
        const response = await fetch("/chat/", { method: "POST", body: body });
        const data = await response.json();
        pending.textContent = data.reply || "No reply received.";
      } catch (err) {
        pending.textContent = "Could not reach the assistant. Please try again.";
      }
    });
  }
})();
