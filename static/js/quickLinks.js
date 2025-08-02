const QUICK_LINKS = [
  {
    name: "WebPrint",
    url: "http://bea-v-print-01.curric.stfx:9191/app",
  },
  { name: "Careers", url: "https://www.sfxcareers.com.au/" },
  { name: "CDF Pay", url: "https://user.cdfpay.flexischools.com.au/" },
  {
    name: "Clickview",
    url: "https://saml-in3.clickview.com.au/Shibboleth.sso/STF1792",
  },
  {
    name: "2026 Beaconsfield Leadership",
    url: "https://simon.sfx.vic.edu.au/WebHandlers/DownloadKnowledgeBankDocument.ashx?DocID=24786&KBankID=25&UserID=25",
  },
];

document.addEventListener("DOMContentLoaded", () => {
  let quickLinksContainer = document.getElementById("quickLinksContainer");

  QUICK_LINKS.forEach((link) => {
    const linkElement = document.createElement("a");
    linkElement.href = link.url;
    linkElement.target = "_blank";
    linkElement.className = "text-decoration-none";

    const card = document.createElement("div");
    card.className = "quick-link-card";

    const cardBody = document.createElement("div");
    cardBody.className =
      "card-body py-2 rounded bg-secondary-light shadow-sm m-0 mb-1 d-flex justify-content-between align-items-center";

    const leftDiv = document.createElement("div");
    const title = document.createElement("h6");
    title.className = "card-title h6 mb-1 fw-medium text-dark";
    title.textContent = link.name;
    leftDiv.appendChild(title);

    const rightDiv = document.createElement("div");
    rightDiv.className = "d-flex align-items-center gap-2";
    const icon = document.createElement("span");
    icon.className = "small text-muted fw-medium";
    icon.innerHTML = '<i class="bi bi-box-arrow-up-right"></i>';
    rightDiv.appendChild(icon);

    cardBody.appendChild(leftDiv);
    cardBody.appendChild(rightDiv);
    card.appendChild(cardBody);
    linkElement.appendChild(card);

    quickLinksContainer.appendChild(linkElement);
  });
  fetchClassResources();
});
