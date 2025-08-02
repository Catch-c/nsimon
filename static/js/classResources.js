function createTaskClickable(taskName, taskLink, taskClass, taskDueDate) {
  const linkElement = document.createElement("a");
  linkElement.href = `https://simon.sfx.vic.edu.au${taskLink}`;
  linkElement.target = "_blank";
  linkElement.className = "text-decoration-none";

  const card = document.createElement("div");
  card.className = "quick-link-card";

  const cardBody = document.createElement("div");
  cardBody.className =
    "card-body py-2 rounded content-card shadow-sm m-0 mb-1 d-flex justify-content-between align-items-center";

  const leftDiv = document.createElement("div");
  const title = document.createElement("h6");
  title.className = "card-title h6 mb-1 fw-medium text-dark";
  title.textContent = taskName;
  leftDiv.appendChild(title);

  const rightDiv = document.createElement("div");
  rightDiv.className = "d-flex align-items-center gap-2";
  const icon = document.createElement("span");
  icon.className = "small text-muted fw-medium";
  icon.innerHTML = taskClass;
  rightDiv.appendChild(icon);

  cardBody.appendChild(leftDiv);
  cardBody.appendChild(rightDiv);
  card.appendChild(cardBody);
  linkElement.appendChild(card);

  return linkElement;
}

function addDueTasksToModal(dueTasks) {
  for (const dueTask of dueTasks) {
    const taskName = dueTask["TaskTitle"];
    const taskLink = dueTask["ViewDetailsURL"];
    const taskClass = dueTask["ClassCode"];
    const taskDueDate = dueTask["DueDate"];

    const taskElement = createTaskClickable(
      taskName,
      taskLink,
      taskClass,
      taskDueDate
    );
    document.getElementById("dueTasksModalHolder").appendChild(taskElement);
  }
}

function addResultTasksToModal(resultTasks) {
  for (const resultTaskClasses of resultTasks) {
    for (const task of resultTaskClasses["Tasks"]) {
      const taskName = task["Title"];
      const taskLink = `/WebModules/LearningAreas/Tasks/StudentSubjectClass.aspx?NavBarItem=ViewAssessmentTasks&TaskID=${task["TaskID"]}&Class=${resultTaskClasses["ID"]}&Inactive=false`;
      const taskClass = task["FinalResult"];
      const taskDueDate = task["DueDate"];

      const taskElement = createTaskClickable(
        taskName,
        taskLink,
        taskClass,
        taskDueDate
      );
      document
        .getElementById("resultTasksModalHolder")
        .appendChild(taskElement);
    }
  }
}

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

      let ResultCount = 0;
      for (const resultsCountText of classResourcesData["ResultTasksStudent"]) {
        ResultCount += resultsCountText["Tasks"].length;
      }
      resultsCountText.textContent = ResultCount;
      overdueCountText.textContent =
        classResourcesData["OverDueTasksStudent"].length;

      addDueTasksToModal(classResourcesData["DueTasksStudent"]);
      addResultTasksToModal(classResourcesData["ResultTasksStudent"]);
    })
    .catch((error) => console.error("Error fetching class resources:", error));
}

document.addEventListener("DOMContentLoaded", () => {
  fetchClassResources();
});
