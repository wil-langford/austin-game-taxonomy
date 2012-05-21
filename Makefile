all:

run:
	qsub execute.sh

watch:
	watch showq -r

clean:
	rm -rf execute.sh.[eo]*

squeaky: clean
	rm -rf *.pyc data/*.dat
