let currentTimetablePeriods = null;
let currentDate = null;
function createPastTimetableCard(periodName, details, timeRange, teacherName) {
  const card = document.createElement("div");
  card.className = "card border-0 rounded";

  const cardBody = document.createElement("div");
  cardBody.className = "card-body py-2 px-2 d-flex flex-column rounded";

  const topRow = document.createElement("div");
  topRow.className = "d-flex justify-content-between align-items-center";

  const title = document.createElement("h6");
  title.className = "card-title h6 mb-0 fw-medium timetable-past";
  title.style.fontSize = "0.7rem";
  title.style.lineHeight = "1.5";
  title.textContent = periodName;

  const time = document.createElement("span");
  time.className = "timetable-past-secondary fw-medium";
  time.style.fontSize = "0.8rem";
  time.style.lineHeight = "1.1";
  time.textContent = timeRange;

  topRow.appendChild(title);
  topRow.appendChild(time);

  const subtitle = document.createElement("p");
  subtitle.className = "card-text mb-0 timetable-past-secondary";
  subtitle.style.fontSize = "0.9rem";
  subtitle.style.lineHeight = "1.1";
  subtitle.textContent = details;
  if (teacherName) {
    subtitle.setAttribute("data-bs-toggle", "tooltip");
    subtitle.setAttribute("data-bs-placement", "top");
    subtitle.setAttribute("title", teacherName);
  }
  cardBody.appendChild(topRow);
  cardBody.appendChild(subtitle);
  card.appendChild(cardBody);

  return card;
}

function createCurrentTimetableCard(
  periodName,
  details,
  timeRange,
  teacherName
) {
  const card = document.createElement("div");
  card.className = "card border-2 border-primary shadow-sm rounded";

  const cardBody = document.createElement("div");
  cardBody.className =
    "card-body py-2 px-2 d-flex flex-column border-start border-secondary border-3 rounded";

  const topRow = document.createElement("div");
  topRow.className = "d-flex justify-content-between align-items-center";

  const title = document.createElement("h6");
  title.className = "card-title h6 mb-0 fw-medium text-dark";
  title.style.fontSize = "0.7rem";
  title.style.lineHeight = "1.5";
  title.textContent = periodName;

  const time = document.createElement("span");
  time.className = "text-muted fw-medium";
  time.style.fontSize = "0.8rem";
  time.style.lineHeight = "1.1";
  time.textContent = timeRange;

  topRow.appendChild(title);
  topRow.appendChild(time);

  const subtitle = document.createElement("p");
  subtitle.className = "card-text mb-0 text-muted";
  subtitle.style.fontSize = "0.9rem";
  subtitle.style.lineHeight = "1.1";
  subtitle.textContent = details;
  if (teacherName) {
    subtitle.setAttribute("data-bs-toggle", "tooltip");
    subtitle.setAttribute("data-bs-placement", "top");
    subtitle.setAttribute("title", teacherName);
  }

  cardBody.appendChild(topRow);
  cardBody.appendChild(subtitle);
  card.appendChild(cardBody);

  return card;
}

function createFutureTimetableCard(
  periodName,
  details,
  timeRange,
  teacherName
) {
  const card = document.createElement("div");
  card.className = "card border-0 rounded";

  const cardBody = document.createElement("div");
  cardBody.className =
    "card-body py-2 px-2 d-flex flex-column border-0 rounded";

  const topRow = document.createElement("div");
  topRow.className = "d-flex justify-content-between align-items-center";

  const title = document.createElement("h6");
  title.className = "card-title h6 mb-0 fw-medium text-dark";
  title.style.fontSize = "0.7rem";
  title.style.lineHeight = "1.5";
  title.textContent = periodName;

  const time = document.createElement("span");
  time.className = "text-muted fw-medium";
  time.style.fontSize = "0.8rem";
  time.style.lineHeight = "1.1";
  time.textContent = timeRange;

  topRow.appendChild(title);
  topRow.appendChild(time);

  const subtitle = document.createElement("p");
  subtitle.className = "card-text mb-0 text-muted";
  subtitle.style.fontSize = "0.9rem";
  subtitle.style.lineHeight = "1.1";
  subtitle.textContent = details;
  if (teacherName) {
    subtitle.setAttribute("data-bs-toggle", "tooltip");
    subtitle.setAttribute("data-bs-placement", "top");
    subtitle.setAttribute("title", teacherName);
  }

  cardBody.appendChild(topRow);
  cardBody.appendChild(subtitle);
  card.appendChild(cardBody);

  return card;
}

function createNonTeachingTimetableCard(periodName, timeRange) {
  const card = document.createElement("div");
  card.className = "card border-0 rounded";

  const cardBody = document.createElement("div");
  cardBody.className =
    "card-body py-2 px-2 d-flex justify-content-between align-items-center border-0 rounded";
  cardBody.style.backgroundColor = "rgb(205, 205, 205)";

  const leftSection = document.createElement("div");
  leftSection.className = "d-flex align-items-center";

  const labelText = document.createElement("p");
  labelText.className = "card-text mb-0 text-muted fw-semibold";
  labelText.style.fontSize = "0.8rem";
  labelText.style.lineHeight = "1.1";
  labelText.textContent = periodName;

  leftSection.appendChild(labelText);

  const rightSection = document.createElement("div");
  rightSection.className = "d-flex align-items-center";

  const time = document.createElement("span");
  time.className = "text-muted fw-medium";
  time.style.fontSize = "0.8rem";
  time.style.lineHeight = "1.1";
  time.textContent = timeRange;

  rightSection.appendChild(time);

  cardBody.appendChild(leftSection);
  cardBody.appendChild(rightSection);
  card.appendChild(cardBody);

  return card;
}

function getCurrentMinutes() {
  const now = new Date();
  return now.getHours() * 60 + now.getMinutes();
}

function timeToMinutes(timeStr) {
  const [hours, minutes] = timeStr.split(":").map(Number);
  return hours * 60 + minutes;
}

function isNow(startTime, endTime) {
  const nowMinutes = getCurrentMinutes();
  const startMinutes = timeToMinutes(startTime);
  const endMinutes = timeToMinutes(endTime);

  if (nowMinutes < startMinutes) {
    return 1;
  } else if (nowMinutes >= startMinutes && nowMinutes < endMinutes) {
    return 2;
  } else {
    return 3;
  }
}

function convertTo12Hour(time24) {
  let [hour, minute] = time24.split(":").map(Number);

  const ampm = hour >= 12 ? "PM" : "AM";
  hour = hour % 12 || 12;

  return `${hour}:${minute.toString().padStart(2, "0")}${ampm}`;
}

function compareDateWithToday(dateString) {
  const inputDate = new Date(dateString);
  const today = new Date();

  inputDate.setHours(0, 0, 0, 0);
  today.setHours(0, 0, 0, 0);

  if (inputDate < today) {
    return -1;
  } else if (inputDate > today) {
    return 1;
  } else {
    return 0;
  }
}

function fetchTimetable(date) {
  let timetableContainer = document.getElementById("timetableContainer");

  const dateStatus = compareDateWithToday(date);
  currentDate = date;

  const requestDate = `${date}T04:39:50.000Z`;
  fetch("/api/getTimetable", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      date: requestDate,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      timetableContainer.innerHTML = "";
      const timetableData = data["d"];
      currentTimetablePeriods = data["d"]["Periods"];
      if (data["d"]["Periods"].length === 0) {
        let newTimetableItem = createNonTeachingTimetableCard(
          "Weekend (No Classes)",
          ``
        );
        timetableContainer.appendChild(newTimetableItem);
      } else {
        for (const period of data["d"]["Periods"]) {
          const isNowResult = isNow(period.StartTime, period.EndTime);

          if (period.IsTeachingPeriod) {
            if (dateStatus === 0) {
              const isNowResult = isNow(period.StartTime, period.EndTime);
              if (isNowResult === 1) {
                let newTimetableItem = createFutureTimetableCard(
                  period.Description,
                  `${period.Classes[0].TimeTableClass} @ ${period.Classes[0].Room}`,
                  `${convertTo12Hour(period.StartTime)} - ${convertTo12Hour(
                    period.EndTime
                  )}`,
                  period.Classes[0].TeacherName
                );
                timetableContainer.appendChild(newTimetableItem);
              } else if (isNowResult === 2) {
                let newTimetableItem = createCurrentTimetableCard(
                  period.Description,
                  `${period.Classes[0].TimeTableClass} @ ${period.Classes[0].Room}`,
                  `${convertTo12Hour(period.StartTime)} - ${convertTo12Hour(
                    period.EndTime
                  )}`,
                  period.Classes[0].TeacherName
                );
                timetableContainer.appendChild(newTimetableItem);
              } else {
                let newTimetableItem = createPastTimetableCard(
                  period.Description,
                  `${period.Classes[0].TimeTableClass} @ ${period.Classes[0].Room}`,
                  `${convertTo12Hour(period.StartTime)} - ${convertTo12Hour(
                    period.EndTime
                  )}`,
                  period.Classes[0].TeacherName
                );
                timetableContainer.appendChild(newTimetableItem);
              }
            } else if (dateStatus === -1) {
              let newTimetableItem = createPastTimetableCard(
                period.Description,
                `${period.Classes[0].TimeTableClass} @ ${period.Classes[0].Room}`,
                `${convertTo12Hour(period.StartTime)} - ${convertTo12Hour(
                  period.EndTime
                )}`,
                period.Classes[0].TeacherName
              );
              timetableContainer.appendChild(newTimetableItem);
            } else {
              let newTimetableItem = createFutureTimetableCard(
                period.Description,
                `${period.Classes[0].TimeTableClass} @ ${period.Classes[0].Room}`,
                `${convertTo12Hour(period.StartTime)} - ${convertTo12Hour(
                  period.EndTime
                )}`,
                period.Classes[0].TeacherName
              );
              timetableContainer.appendChild(newTimetableItem);
            }
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
      }

      const tooltipTriggerList = document.querySelectorAll(
        '[data-bs-toggle="tooltip"]'
      );
      const tooltipList = [...tooltipTriggerList].map(
        (tooltipTriggerEl) => new bootstrap.Tooltip(tooltipTriggerEl)
      );
    })
    .catch((error) => console.error("Error fetching timetable:", error));
}

function fetchTimetableNextDay(date) {
  let timetableContainer = document.getElementById("timetableContainer");

  const dateStatus = compareDateWithToday(date);
  currentDate = date;
  const requestDate = `${date}T04:39:50.000Z`;
  fetch("/api/getTimetable", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      date: requestDate,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      timetableContainer.innerHTML = "";
      const timetableData = data["d"];
      currentTimetablePeriods = data["d"]["Periods"];

      let newTimetableItem = createNonTeachingTimetableCard(
        "Weekend (No Classes) | Here are your classes for Monday.",
        ``
      );
      timetableContainer.appendChild(newTimetableItem);

      for (const period of data["d"]["Periods"]) {
        const isNowResult = isNow(period.StartTime, period.EndTime);

        if (period.IsTeachingPeriod) {
          if (dateStatus === 0) {
            const isNowResult = isNow(period.StartTime, period.EndTime);
            if (isNowResult === 1) {
              let newTimetableItem = createFutureTimetableCard(
                period.Description,
                `${period.Classes[0].TimeTableClass} @ ${period.Classes[0].Room}`,
                `${convertTo12Hour(period.StartTime)} - ${convertTo12Hour(
                  period.EndTime
                )}`,
                period.Classes[0].TeacherName
              );
              timetableContainer.appendChild(newTimetableItem);
            } else if (isNowResult === 2) {
              let newTimetableItem = createCurrentTimetableCard(
                period.Description,
                `${period.Classes[0].TimeTableClass} @ ${period.Classes[0].Room}`,
                `${convertTo12Hour(period.StartTime)} - ${convertTo12Hour(
                  period.EndTime
                )}`,
                period.Classes[0].TeacherName
              );
              timetableContainer.appendChild(newTimetableItem);
            } else {
              let newTimetableItem = createPastTimetableCard(
                period.Description,
                `${period.Classes[0].TimeTableClass} @ ${period.Classes[0].Room}`,
                `${convertTo12Hour(period.StartTime)} - ${convertTo12Hour(
                  period.EndTime
                )}`,
                period.Classes[0].TeacherName
              );
              timetableContainer.appendChild(newTimetableItem);
            }
          } else if (dateStatus === -1) {
            let newTimetableItem = createPastTimetableCard(
              period.Description,
              `${period.Classes[0].TimeTableClass} @ ${period.Classes[0].Room}`,
              `${convertTo12Hour(period.StartTime)} - ${convertTo12Hour(
                period.EndTime
              )}`,
              period.Classes[0].TeacherName
            );
            timetableContainer.appendChild(newTimetableItem);
          } else {
            let newTimetableItem = createFutureTimetableCard(
              period.Description,
              `${period.Classes[0].TimeTableClass} @ ${period.Classes[0].Room}`,
              `${convertTo12Hour(period.StartTime)} - ${convertTo12Hour(
                period.EndTime
              )}`,
              period.Classes[0].TeacherName
            );
            timetableContainer.appendChild(newTimetableItem);
          }
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

      const tooltipTriggerList = document.querySelectorAll(
        '[data-bs-toggle="tooltip"]'
      );
      const tooltipList = [...tooltipTriggerList].map(
        (tooltipTriggerEl) => new bootstrap.Tooltip(tooltipTriggerEl)
      );
    })
    .catch((error) => console.error("Error fetching timetable:", error));
}

function createTimetableShare() {
  fetch("/api/createTimetableShare", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      date: currentDate,
      timetable: currentTimetablePeriods,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      document.getElementById(
        "timetableShareInput"
      ).value = `https://amazing-earwig-reliably.ngrok-free.app/s/${data}`;
    })
    .catch((error) => console.error("Error fetching timetable:", error));
}

document.addEventListener("DOMContentLoaded", () => {
  const timetableDate = document.getElementById("timetableDate");

  function handleFetchTimetable(dateStr) {
    const selectedDate = new Date(dateStr);
    const day = selectedDate.getDay();

    if (day === 6 || day === 0) {
      const nextMonday = new Date(selectedDate);
      const daysToAdd = day === 6 ? 2 : 1;
      nextMonday.setDate(selectedDate.getDate() + daysToAdd);

      const formattedMonday = nextMonday.toISOString().split("T")[0];
      fetchTimetableNextDay(formattedMonday);
    } else {
      fetchTimetable(dateStr);
    }
  }

  handleFetchTimetable(timetableDate.value);

  timetableDate.addEventListener("change", () => {
    handleFetchTimetable(timetableDate.value);
  });
});
