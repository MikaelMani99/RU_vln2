let addVal = 1;
displayDivs(addVal);

function plusDivs(n) {
  displayDivs(addVal += n);
}

function displayDivs(n) {
  let el = document.getElementsByClassName("product-detail-img");
  if (n > el.length) {
    addVal = 1
  };
  if (n < 1) {
    addVal = el.length
  };
  for (let i = 0; i < el.length; i++) {
    el[i].style.display = "none";
  }
  el[addVal-1].style.display = "block";
}
