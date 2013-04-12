/**
host: www.google.com
*/

//alert(1);

if (window.location == window.top.location) {
  window.location = window.location.href.replace('www.google.com', 'gs');
  alert(window.location.href.replace('www.google.com', 'gs'));
  //alert(window.location);
}
