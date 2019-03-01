#!/bin/bash
# Usage ./autoprocess n (where n is an integer). Changes into the directory Dot_Matrix_Test_n
# Processes all the .tiff files so they can be read by Tesseract without error 
# 0-9, A-Z, Colon, Dash, Period, Slash.

declare -a arr=("Colon" "Dash" "Period" "Slash")

cd Dot_Matrix_Test_$1

for i in {0..9}
do
	cd $i
	for f in *.tiff
	do
		convert -density 300 ./$f -depth 8 -strip -background white -alpha off $f	
	done
	cd ..
done

for i in {A..Z}
do
	cd $i
	for f in *.tiff
	do
		convert -density 300 ./$f -depth 8 -strip -background white -alpha off $f	
	done
	cd ..	
done

for i in "${arr[@]}"
do	
	cd $i
	for f in *.tiff
	do
		convert -density 300 ./$f -depth 8 -strip -background white -alpha off $f	
	done
	cd ..
done

