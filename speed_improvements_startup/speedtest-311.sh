#!/bin/bash
SECONDS=0
for i in {1..250}
do
   /usr/bin/time python3.11 -c "pass"
done
duration=$SECONDS
echo "$(($duration % 60)) seconds elapsed."