all:

clean:
	rm -rf execute.sh.[eo]*

squeaky: clean
	rm -rf *.pyc data/*.dat
