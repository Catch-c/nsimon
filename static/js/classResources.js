function fetchClassResources() {
  fetch("/api/getClasses", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      let dueCountText = document.getElementById("test123123");
      let resultsCountText = document.getElementById("test123123123");
      let overdueCountText = document.getElementById("test123123123123123");

      const classResourcesData = data["d"];
      dueCountText.textContent = classResourcesData["DueTasksStudent"].length;
      resultsCountText.textContent =
        classResourcesData["ResultTasksStudent"].length;
      overdueCountText.textContent =
        classResourcesData["OverDueTasksStudent"].length;
    })
    .catch((error) => console.error("Error fetching daily messages:", error));
}

document.addEventListener("DOMContentLoaded", () => {
  fetchClassResources();
});
