#!/bin/bash
# Usage ./autocount n (where n is an integer). Changes into the directory Dot_Matrix_Test_n
# Counts the number of .tiff images for each of the classes 
# 0-9, A-Z, Colon, Dash, Period, Slash.

declare -a arr=("Colon" "Dash" "Period" "Slash")

cd Dot_Matrix_Test_$1

for i in {0..9}
do
	cd $i
	tiff_count="$(ls *.tiff -l | wc -l)"
	echo $i $tiff_count
	cd ..
done

for i in {A..Z}
do
	cd $i
	tiff_count="$(ls *.tiff -l | wc -l)"
	echo $i $tiff_count
	cd ..
done

for i in "${arr[@]}"
do
	cd $i
	tiff_count="$(ls *.tiff -l | wc -l)"
	echo $i $tiff_count
	cd ..
done

