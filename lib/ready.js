if (window.bsdpower === undefined) {
  window.bsdpower = {};
}

window.bsdpower.check = function() {
  //alert('check');
  var state = document.readyState;
  if (state == 'loaded' || state == 'complete') {
      window.bsdpower.ready();
  } else {
    setTimeout(window.bsdpower.check, 250);
  }
};

setTimeout(window.bsdpower.check, 250);

if (window.bsdpower.readylist === undefined) {
  window.bsdpower.readylist = [];
}

//alert(window.jQuery);
window.bsdpower.ready = function(arg) {
  if (arg) {
    window.bsdpower.readylist.push(arg);
  } else {
    for (var i = 0; i < window.bsdpower.readylist.length; ++i) {
      window.bsdpower.readylist[i]();
    }
  }
};
