/**
host: github.com
*/

window.bsdpower.ready.push(function() {
  $('.tooltipped').each(function() {
    var e = $(this);
    e.attr('original-title', '');
  });
});
