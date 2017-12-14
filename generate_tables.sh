 #!/bin/bash
 # generates markdown tables for n in range [1,40] with limit n+1000 for m
for i in `seq 1 40`;
do
	python generate_triple_table_for_n.py $i > results/$i.md
done

