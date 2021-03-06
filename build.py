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
    
    matches = re.compile('^host: (.*)', re.M).finditer(content)
    
    content = re.compile(r'/\*.*?\*/', re.S).sub('', content)
    content = content.replace("\n", ' ').replace('"', r'\"')
    
    for match in matches:
        host = match.group(1)
        #host_re = host.replace('.', '\\.')
        #host_re = host_re.replace('*', '.*')
        
        bits = css_hostmap.get(host, [])
        bits.append(content)
        css_hostmap[host] = bits

def process_js(file):
    global js_hostmap
    
    with open(os.path.join('sites', file)) as f:
        content = f.read()
    
    matches = re.compile('^host: (.*)', re.M).finditer(content)
    
    content = re.compile(r'^\s*//.*$', re.M).sub('', content)
    content = re.compile(r'/\*.*?\*/', re.S).sub('', content)
    content = content.replace("\n", ' ').replace('"', r'\"')
    
    for match in matches:
        host = match.group(1)
        
        bits = js_hostmap.get(host, [])
        bits.append(content)
        js_hostmap[host] = bits

for file in os.listdir('sites'):
    if file.endswith('.css'):
        process_css(file)
    if file.endswith('.js'):
        process_js(file)

def host_spec_to_regexp(host):
    host = host.replace('.', '\\.')
    host = host.replace('*', '.*')
    host = '\\/\\/' + host
    return host

with open('lib/ready.js') as f:
    preamble += f.read()

for host in css_hostmap:
    content = ''.join(css_hostmap[host])
    re_host = host_spec_to_regexp(host)
    preamble += '''
        styles['%(host)s'] = "%(content)s";
        if (/%(re_host)s/.test(window.location.href)) {
            addstyle(styles['%(host)s']);
            matched = true;
        }
    ''' % dict(host=host, re_host=re_host, content=content)

if 'all' in css_hostmap:
    content = ''.join(css_hostmap['all'])
    preamble += '''
        styles['all'] = "%(content)s";
        addstyle(styles['all']);
    ''' % dict(content=content)

for host in js_hostmap:
    content = ''.join(js_hostmap[host])
    re_host = host_spec_to_regexp(host)
    preamble += '''
        if (/%(re_host)s/.test(window.location.href)) {
            %(content)s
            ;matched = true;
        }
    ''' % dict(host=host, re_host=re_host, content=content)

if 'default' in css_hostmap:
    content = ''.join(css_hostmap['default'])
    preamble += '''
        styles['default'] = "%(content)s";
        if (!matched) {
            addstyle(styles['default']);
        }
    ''' % dict(content=content)

preamble += '''
    window.FluidWeb = window.FluidWeb || {};
    window.FluidWeb.matched = matched;
'''

print preamble
