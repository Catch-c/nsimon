function showLessonPlan(classID) {
  fetch("/api/getClassLessonPlans", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      classID: classID,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data["d"]["CurrentPlans"]) {
        document.getElementById("lessonPlanModalLabel").innerText =
          data["d"]["CurrentPlans"][0]["LessonPlanTitle"];

        fetch("/api/getLessonPlan", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            classID: classID,
            lessonID: data["d"]["CurrentPlans"][0]["LessonPlanID"],
          }),
        })
          .then((response) => response.json())
          .then((data) => {
            document.getElementById("lessonPlanModalBody").innerHTML =
              data.d.LessonPlanDetails.LessonSections[0].SectionContent;
          })
          .catch((error) =>
            console.error("Error fetching lesson plan:", error)
          );

        const modal = new bootstrap.Modal(
          document.getElementById("lessonPlanModal")
        );
        modal.show();
      }
    })
    .catch((error) => console.error("Error fetching weather:", error));
}
