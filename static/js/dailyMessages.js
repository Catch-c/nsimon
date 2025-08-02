function removeColorStyles(htmlString) {
  const parser = new DOMParser();
  const doc = parser.parseFromString(htmlString, "text/html");
  const styledElements = doc.querySelectorAll("[style]");

  styledElements.forEach((elem) => {
    const styles = elem
      .getAttribute("style")
      .split(";")
      .filter((style) => {
        const trimmedStyle = style.trim();
        return (
          !trimmedStyle.startsWith("color:") &&
          !trimmedStyle.startsWith("background-color:") &&
          !trimmedStyle.startsWith("background:")
        );
      });
    elem.setAttribute("style", styles.join(";"));
  });

  return doc.body.innerHTML;
}

function fetchDailyMessages(date) {
  let dailyMessageContainer = document.getElementById("dailyMessageHolder");
  dailyMessageContainer.innerHTML = "";

  fetch("/api/getDailyMessages", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      date: date,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      const dailyMessagesData = data["d"]["SchoolMessages"];

      for (const message of dailyMessagesData) {
        const card = document.createElement("div");
        card.className =
          "card border-2 border-0 mx-0 rounded content-card-secondary shadow-sm mb-2";

        const cardBody = document.createElement("div");
        cardBody.className = "card-body py-2 rounded";

        const title = document.createElement("h6");
        title.className = "card-title h6 mb-1 fw-medium text-dark";
        title.textContent = message.MessageTitle;

        // Add category badge
        const categoryBadge = document.createElement("span");
        categoryBadge.className = "badge text-bg-secondary ms-2";
        categoryBadge.textContent = message.SchoolMessageCategoryTitle;
        title.appendChild(categoryBadge);

        const content = document.createElement("p");
        content.className = "card-text small text-muted mb-0";
        content.innerHTML = removeColorStyles(message.MessageContent);

        cardBody.appendChild(title);
        cardBody.appendChild(content);
        card.appendChild(cardBody);

        dailyMessageContainer.appendChild(card);
      }
    })
    .catch((error) => console.error("Error fetching daily messages:", error));
}

document.addEventListener("DOMContentLoaded", () => {
  const today = new Date().toISOString();

  fetchDailyMessages(today);
});
