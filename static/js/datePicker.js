document.addEventListener("DOMContentLoaded", () => {
  const now = new Date();
  const aestDate = new Date(
    now.toLocaleString("en-US", { timeZone: "Australia/Sydney" })
  );

  const year = aestDate.getFullYear();
  const month = String(aestDate.getMonth() + 1).padStart(2, "0");
  const day = String(aestDate.getDate()).padStart(2, "0");
  const today = `${year}-${month}-${day}`;

  document.getElementById("timetableDate").value = today;
});
