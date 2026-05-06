const form = document.querySelector("#chat-form");
const input = document.querySelector("#message-input");
const messages = document.querySelector("#messages");

function addMessage(text, sender) {
  const article = document.createElement("article");
  article.className = `message ${sender}`;

  const bubble = document.createElement("div");
  bubble.className = "bubble";
  bubble.textContent = text;

  article.appendChild(bubble);
  messages.appendChild(article);
  messages.scrollTop = messages.scrollHeight;
}

async function sendMessage(message) {
  const response = await fetch("/api/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message }),
  });

  const data = await response.json();
  return data.reply || "I could not make a reply for that.";
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const message = input.value.trim();
  if (!message) {
    return;
  }

  addMessage(message, "user");
  input.value = "";
  input.focus();
  form.querySelector("button").disabled = true;

  try {
    const reply = await sendMessage(message);
    addMessage(reply, "bot");
  } catch {
    addMessage("I cannot reach the chatbot server right now.", "bot");
  } finally {
    form.querySelector("button").disabled = false;
  }
});
