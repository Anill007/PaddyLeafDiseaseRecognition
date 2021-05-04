function plant() {
  let popup = document.getElementById("popup");
  popup.style.visibility = "visible";
}

function paddy() {
  let popup = document.getElementById("popup");
  popup.style.visibility = "hidden";
}

let cancel = document.getElementById("cancel");
cancel.addEventListener("click", function (event) {
  event.preventDefault();
});

let submitbutton = document.getElementById("submitbutton");
submitbutton.addEventListener("click", function (event) {
  event.preventDefault();

  try {
    let image = document.getElementById("file1").files[0].name;
  } catch {
    alert(
      "Error! No Image is selected. Click on the PC icon to select an image."
    );
    return false;
  }
  document.getElementById("myform").submit();
});
