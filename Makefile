all:

run:
	qsub -N atax_job -j oe execute.sh

watch:
	watch showq -r

clean:
	rm -rf execute.sh.[eo]*

squeaky: clean
	rm -rf *.pyc data/*.dat

report: 
	for each in execute.sh.e* ; do echo ---- $$each ---- ; cat $$each ; done
	for each in execute.sh.o* ; do echo ---- $$each ---- ; cat $$each ; done
