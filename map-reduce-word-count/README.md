- Map

`./map.py < toy.txt`


- Map + sort

`./map.py < toy.txt | sort`


- Map + sort + reduce

`./map.py < toy.txt | sort | ./reduce.py`


- Map + sort + reduce (with progress bars)

`pv -c -N mapProgress medium.txt | ./map.py | sort | pv -c -N reduceProgress | ./reduce.py > /dev/null`


