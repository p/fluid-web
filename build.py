#!/usr/bin/env python

import os, os.path, re

preamble = '''
function addstyle(css) {
  var style = document.createElement('style');
  style.type = 'text/css';
  style.appendChild(document.createTextNode(css));
  document.getElementsByTagName('head')[0].appendChild(style);
}
var styles = {};
'''

hostmap = {}

for file in os.listdir('sites'):
    with open(os.path.join('sites', file)) as f:
        content = f.read()
    match = re.compile('^host: (.*)', re.M).search(content)
    assert match
    host = match.group(1)
    
    content = re.compile(r'/\*.*?\*/', re.S).sub('', content)
    content = content.replace("\n", ' ').replace('"', r'\"')
    
    bits = hostmap.get(host, [])
    bits.append(content)
    hostmap[host] = bits

for host in hostmap:
    content = ''.join(hostmap[host])
    preamble += '''
        styles['%(host)s'] = "%(content)s";
        if (/\/\/%(host)s/.test(window.location.href)) {
            addstyle(styles['%(host)s']);
        }
    ''' % dict(host=host, content=content)

print preamble
