function kt_3_1() {
    let shape = document.getElementById('shape').value;
    let color = document.getElementById('color').value;
    let length = shape.length;
  
    alert('Мне нравится ' + shape +  ', цвет '+ color + '\n' + ' длина фигуры = ' + length);
  }
  function kt_3_2() {
    let shape = document.getElementById('shapeField').value;
    let color = document.getElementById('colorField').value;
    let length = shape.length;
  
    alert('Мне нравится ' + shape + ', цвет ' + color + '\n' + ' длина фигуры = ' + length);
  }
  function kt_3_2_name() {
          alert('Вводите имя внимательно');
      }
  function kt_3_2_submit() {
    let name = document.getElementById('name').value;
    let iceCreamChecked = document.getElementById('iceCream').checked;
    let chocolateChecked = document.getElementById('chocolate').checked;
    if (iceCreamChecked && !chocolateChecked) {
      alert('Вы выбрали: мороженое');
    } else if (!iceCreamChecked && chocolateChecked) {
      alert('Вы выбрали: шоколад');
    } else if (iceCreamChecked && chocolateChecked) {
      alert('Вы выбрали: мороженое и шоколад');
    } else {
      alert('Вы ничего не выбрали');
    }
    alert('Спасибо, что приняли участие в опросе, '+name+'!');
      }