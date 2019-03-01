#!/bin/bash
# Usage ./autorename n (where n is an integer). Changes into the directory Dot_Matrix_Test_n
# Renames all the .tiff files to .tif files 
# 0-9, A-Z, Colon, Dash, Period, Slash.

declare -a arr=("Colon" "Dash" "Period" "Slash")

cd Dot_Matrix_Test_$1

for i in {0..9}
do
	cd $i
	for f in *.tiff
	do
		mv "$f" "${f%.tiff}.tif"	
	done
	cd ..
done

for i in {A..Z}
do
	cd $i
	for f in *.tiff
	do
		mv "$f" "${f%.tiff}.tif"	
	done
	cd ..	
done

for i in "${arr[@]}"
do	
	cd $i
	for f in *.tiff
	do
		mv "$f" "${f%.tiff}.tif"	
	done
	cd ..
done

