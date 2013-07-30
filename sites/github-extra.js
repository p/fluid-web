/**
host: github.com
*/

window.bsdpower.ready(function($) {
  $('.numbers-summary').each(function() {
    var starturl = this.childNodes[this.childNodes.length-1].childNodes[0].href;
    alert(starturl);
    var li = $('<li/>');
    //li[0].appendChild
  });
});
