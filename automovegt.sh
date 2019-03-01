#!/bin/bash
# Usage: ./automovegt n (where n and m are integers). From each subdirectory in
# Dot_Matrix_Test_1, moves all files to the ground truth directory 

declare -a arr=("Colon" "Dash" "Period" "Slash")

source_dir=Dot_Matrix_Test_$1

for i in {0..9}
do
	cp /home/JPL_OCR_Expiration_Date/$source_dir/$i/* /home/ocrd-train/data/ground-truth/
done

for i in {A..Z}
do
	cp /home/JPL_OCR_Expiration_Date/$source_dir/$i/* /home/ocrd-train/data/ground-truth/
done

for i in "${arr[@]}"
do
	cp /home/JPL_OCR_Expiration_Date/$source_dir/$i/* /home/ocrd-train/data/ground-truth/
done	





