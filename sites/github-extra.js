/**
host: github.com
*/

window.bsdpower.ready(function() {
  $('.numbers-summary').each(function() {
    var url = $('.numbers-summary li:first-child a').attr('href');
    var pullsurl = url.replace(/\/commits\/.*/, '/pulls');
    var li = $('<li><a href="">Pull requests</a></li>');
    li.find('a').attr('href', pullsurl);
    li.insertAfter($('.numbers-summary li:first-child'));
  });
});
