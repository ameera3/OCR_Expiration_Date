#!/bin/bash
# Usage: ./automake n m (where n and m are integers). From each subdirectory in
# Dot_Matrix_Test_n, moves all .tiff files to the corresponding directory in 
# Dot_Matrix_Test_m

declare -a arr=("Colon" "Dash" "Period" "Slash")

source_dir=Dot_Matrix_Test_$1

dest_dir=Dot_Matrix_Test_$2

for i in {0..9}
do
	cp ~/Desktop/JPL/$source_dir/$i/*.tiff ~/Desktop/JPL/$dest_dir/$i
done

for i in {A..Z}
do
	cp ~/Desktop/JPL/$source_dir/$i/*.tiff ~/Desktop/JPL/$dest_dir/$i
done

for i in "${arr[@]}"
do
	cp ~/Desktop/JPL/$source_dir/$i/*.tiff ~/Desktop/JPL/$dest_dir/$i
done	





