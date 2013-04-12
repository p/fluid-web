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
var matched = false;
'''

css_hostmap = {}
js_hostmap = {}

def process_css(file):
    global css_hostmap
    
    with open(os.path.join('sites', file)) as f:
        content = f.read()
    match = re.compile('^host: (.*)', re.M).search(content)
    assert match
    host = match.group(1)
    
    content = re.compile(r'/\*.*?\*/', re.S).sub('', content)
    content = content.replace("\n", ' ').replace('"', r'\"')
    
    bits = css_hostmap.get(host, [])
    bits.append(content)
    css_hostmap[host] = bits

def process_js(file):
    global js_hostmap
    
    with open(os.path.join('sites', file)) as f:
        content = f.read()
    match = re.compile('^host: (.*)', re.M).search(content)
    assert match
    host = match.group(1)
    
    content = re.compile(r'/\*.*?\*/', re.S).sub('', content)
    content = content.replace("\n", ' ').replace('"', r'\"')
    
    bits = js_hostmap.get(host, [])
    bits.append(content)
    js_hostmap[host] = bits

for file in os.listdir('sites'):
    if file.endswith('.css'):
        process_css(file)
    if file.endswith('.js'):
        process_js(file)

for host in css_hostmap:
    content = ''.join(css_hostmap[host])
    preamble += '''
        styles['%(host)s'] = "%(content)s";
        if (/\/\/%(host)s/.test(window.location.href)) {
            addstyle(styles['%(host)s']);
            matched = true;
        }
    ''' % dict(host=host, content=content)

for host in js_hostmap:
    content = ''.join(js_hostmap[host])
    preamble += '''
        if (/\/\/%(host)s/.test(window.location.href)) {
            %(content)s
            ;matched = true;
        }
    ''' % dict(host=host, content=content)

if 'default' in css_hostmap:
    content = ''.join(css_hostmap['default'])
    preamble += '''
        styles['default'] = "%(content)s";
        if (!matched) {
            addstyle(styles['default']);
        }
    ''' % dict(host=host, content=content)

preamble += '''
    window.FluidWeb = window.FluidWeb || {};
    window.FluidWeb.matched = matched;
'''

print preamble
