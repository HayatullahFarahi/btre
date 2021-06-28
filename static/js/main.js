const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

//alert message fade out
setTimeout(function () {
  $('#message').fadeOut('slow');
}, 3000);
