function Mes() {
    alert("Вводите имя внимательно");
  }
  function Submit() {
    let name = document.getElementById("name").value;
    let iceCreamChecked = document.getElementById("iceCream").checked;
    let chocolateChecked = document.getElementById("chocolate").checked;
    if (iceCreamChecked && !chocolateChecked) {
      alert("Вы выбрали: мороженое");
    } else if (!iceCreamChecked && chocolateChecked) {
      alert("Вы выбрали: шоколад");
    } else if (iceCreamChecked && chocolateChecked) {
      alert("Вы выбрали: мороженое и шоколад");
    } else {
      alert("Вы ничего не выбрали");
    }
    alert("Спасибо, что приняли участие в опросе, " + name + "!");
  }