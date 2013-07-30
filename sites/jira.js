/**
host: *.atlassian.net
*/

window.bsdpower.ready(function() {
          var doit = function () {
            //alert(document.getElementById('stalker').style.position);
          //document.getElementById('stalker').id = 'no-stalker';
            //$('#stalker').removeClass('js-stalker');
            var node = $('#stalker')[0];
            if (!node) return;
            var parent = node.parentNode;
            var rep = document.createElement('header');
            rep.innerHTML = node.innerHTML;
            rep.className = node.className;
            node.innerHTML = '';
            parent.insertBefore(rep, parent.childNodes[0]);
            parent.removeChild(node);
          };
          window.bsdpower.ready(doit);
          var old = history.pushState;
          history.pushState = function() {
            //alert('here');
            setTimeout(doit, 500);
            return old.apply(this, arguments);
          };
});
