function convertTo12Hour(datetimeString) {
  const date = new Date(datetimeString);
  let hours = date.getHours();
  const minutes = date.getMinutes().toString().padStart(2, "0");
  const ampm = hours >= 12 ? "PM" : "AM";

  hours = hours % 12;
  hours = hours === 0 ? 12 : hours;

  return `${hours}:${minutes} ${ampm}`;
}

function fetchWeather() {
  fetch("/api/getWeather", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      document.getElementById("currentWeatherConditions").innerText =
        data.currentDescription;

      document.getElementById(
        "currentWeatherTemp"
      ).innerText = `${data.currentTemperature}°C`;
      document.getElementById(
        "currentWeatherIcon"
      ).src = `/static/icons/airy/${data.currentIcon}@4x.png`;
      document.getElementById(
        "currentFeelsLike"
      ).innerText = `Feels like ${data.currentFeelsLike}°C`;
      document.getElementById("todayMinTemp").innerText = `${data.todayMin}°C`;
      document.getElementById("todayMaxTemp").innerText = `${data.todayMax}°C`;
      document.getElementById("todayUVIndex").innerText = `${data.todayUV}`;
      document.getElementById("todaySunrise").innerText = `${convertTo12Hour(
        data.todaySunrise
      )}`;

      document.getElementById("todaySunset").innerText = `${convertTo12Hour(
        data.todaySunset
      )}`;
    })
    .catch((error) => console.error("Error fetching weather:", error));
}

document.addEventListener("DOMContentLoaded", () => {
  fetchWeather();
});
