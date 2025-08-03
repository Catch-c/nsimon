function getGreeting() {
  const now = new Date();
  const hour = now.getHours();

  if (hour < 12) {
    return "Good Morning";
  } else if (hour < 18) {
    return "Good Afternoon";
  } else {
    return "Good Evening";
  }
}

function fetchUserInformation() {
  fetch("/api/getUserInformation", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      document.getElementById(
        "dashboardHeaderText"
      ).innerText = `${getGreeting()}, ${data["d"]["name"]}.`;
      document.getElementById("sidebarName").innerText = data["d"]["name"];
    })
    .catch((error) => console.error("Error fetching weather:", error));
}

document.addEventListener("DOMContentLoaded", () => {
  fetchUserInformation();
});
