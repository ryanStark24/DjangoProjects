
document.addEventListener('DOMContentLoaded', function () {
  particleground(document.getElementById('particles'), {
    dotColor: '#AAAA39',
    lineColor: '#2D882D'
  });
  var intro = document.getElementById('intro');
  intro.style.marginTop = -575 + 'px';
}, false);



function draw() {
	var color =  document.getElementById('body');
	color.style.background='#'+map(mouseX,0,width,0,255);
}