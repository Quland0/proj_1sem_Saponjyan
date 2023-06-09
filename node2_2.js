let x = +prompt('input num');
if (x < 0){
	var y = Math.abs(x-1);
}
else if (0 <= x && x <= 2){
	var y = 2*x;
}
else if (x > 2){
	var y = x+6;
}
alert(y);