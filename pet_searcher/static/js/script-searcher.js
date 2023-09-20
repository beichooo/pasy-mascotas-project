console.log("hello pasy searcher");

//popup for search results indication

const divResultsMsg = document.querySelector(".results-list");
const popupResultsMsg = document.querySelector("#resultsMsgPopup");

function resultsShowPopup() {
  popupResultsMsg.style.display = "block";
}

function resultsClosePopup() {
  popupResultsMsg.style.display = "none";
}

function isTargetElementLoadedResults() {
  return divResultsMsg !== null;
}

document.addEventListener("DOMContentLoaded", function () {
  if (isTargetElementLoadedResults()) {
    resultsShowPopup();

    setTimeout(resultsClosePopup, 4000);
  }
});

const divsConfirmVisit = document.querySelectorAll(".links-confirm-visit");
const popupConfirmVisitDivs = document.querySelector("#confirmVisitPopup");

function confirmShowPopup() {
  popupConfirmVisitDivs.style.display = "block";
}

function confirmClosePopup() {
  popupConfirmVisitDivs.style.display = "none";
}

function confirmClosePopup() {
  popupConfirmVisitDivs.style.display = "none";
}

divsConfirmVisit.forEach((div) => {
  div.addEventListener("click", confirmShowPopup);
});
