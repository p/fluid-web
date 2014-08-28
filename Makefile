all:
	./build.py >/home/pie/apps/unixtools/home/operajs/fluid.js
	rsync -av /home/pie/apps/unixtools/home/operajs/ /home/browser/operajs
