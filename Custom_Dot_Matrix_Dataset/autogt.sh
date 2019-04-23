#!/bin/bash
# Usage ./autogt n (where n is an integer). Changes into the directory Dot_Matrix_Test_n
# Creates a .gt.txt transcription file for each .tif file in each of the subdirectories
# 0-9, A-Z, Colon, Dash, Period, Slash.

declare -a arr=("Colon" "Dash" "Period" "Slash")

cd Dot_Matrix_Test_$1

for i in {0..9}
do
	cd $i
	for f in *.tif
	do
		echo "$i" > "${f%.tif}.gt.txt"	
	done
	cd ..
done

for i in {A..Z}
do
	cd $i
	for f in *.tif
	do
		echo "$i" > "${f%.tif}.gt.txt" 	
	done
	cd ..	
done

cd Colon
for f in *.tif
do
	echo ':' > "${f%.tif}.gt.txt"	
done
cd ..


cd Dash
for f in *.tif
do
	echo '-' > "${f%.tif}.gt.txt"	
done
cd ..


cd Period
for f in *.tif
do
	echo '.' > "${f%.tif}.gt.txt"	
done
cd ..


cd Slash
for f in *.tif
do
	echo '/' > "${f%.tif}.gt.txt"	
done
cd ..

