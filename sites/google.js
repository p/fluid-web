/**
host: www.google.com
*/

//alert(1);

if (window.location == window.top.location) {
  // window.location does not seem to work - overridden by google js?
  // googles grabby hands seem to catch nearly everything
  //var head = document.getElementsByTagName('head')[0];
  var url = window.location.href.replace('www.google.com', 'gs');
  //var meta = document.createElement('meta');
  //meta.att
  //head.appendChild(meta);
  //alert(url);
  //head.innerHTML += '<meta http-equiv="refresh" content="0;url=' + url + '">';
  window.bsdpower.ready(function() {
  var body = document.getElementsByTagName('body')[0];
  body.innerHTML += '<form id=rr method=get action="http://gs/x"><input type=submit></form>';
    //setTimeout(function() {
    var form = document.getElementById('rr');
    form.action = url.split('?')[0];
    var pairs = location.href.split('?')[1].split('&');
    for (var i = 0; i < pairs.length; ++i) {
      var kw = pairs[i].split('=');
      var child = document.createElement('input');
      child.type = 'hidden';
      child.name = kw[0];
      child.value = kw[1];
      form.appendChild(child);
    }
    //alert(form.innerHTML);
      form[0].click();
    //}, 100);
    //alert('ok');
  });
}
