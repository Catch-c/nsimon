document.addEventListener("DOMContentLoaded", () => {
  function getURLParameter(name) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(name);
  }

  const shareCode = getURLParameter("shareCode");

  if (shareCode) {
    fetch("/api/getTimetableShare", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        shareCode: shareCode,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        timetableContainer = document.getElementById("timetableShareViewBody");
        timetableContainer.innerHTML = "";

        document.getElementById(
          "timetableShareViewModalLabel"
        ).textContent = `${data.username}'s Timetable for ${data.date}`;
        for (const period of data.timetable) {
          if (period.IsTeachingPeriod) {
            let newTimetableItem = createFutureTimetableCard(
              period.Description,
              `${period.Classes[0].TimeTableClass} @ ${period.Classes[0].Room}`,
              `${convertTo12Hour(period.StartTime)} - ${convertTo12Hour(
                period.EndTime
              )}`,
              period.Classes[0].TeacherName
            );
            timetableContainer.appendChild(newTimetableItem);
          } else {
            let newTimetableItem = createNonTeachingTimetableCard(
              period.Description,
              `${convertTo12Hour(period.StartTime)} - ${convertTo12Hour(
                period.EndTime
              )}`
            );
            timetableContainer.appendChild(newTimetableItem);
          }
        }
      })
      .catch((error) => console.error("Error fetching timetable:", error));
    const modal = new bootstrap.Modal(
      document.getElementById("timetableShareViewModal")
    );
    modal.show();
  }
});
