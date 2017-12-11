 #!/bin/bash
for i in `seq 1 10`;
do
	echo $i
	python calc_first_n_pythagorean_triple_splitup_size.py $i > results/$i.md
done

