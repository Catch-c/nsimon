document.addEventListener("DOMContentLoaded", () => {
  const switchIds = ["musicSwitch", "canteenSwitch", "sportSwitch"];

  switchIds.forEach((id) => {
    const el = document.getElementById(id);

    const storedValue = localStorage.getItem(id);
    const isChecked = storedValue === null ? true : storedValue === "true";

    el.checked = isChecked;

    el.addEventListener("change", () => {
      localStorage.setItem(id, el.checked);
      const today = new Date().toISOString();
      fetchDailyMessages(today);
    });
  });
});
