#!/bin/bash
#Usage: ./automake n (where n is an integer). Creates the directory
#Dot_Matrix_Test_n and creates subdirectories for each of the classes
#0-9, A-Z, Colon, Dash, Period, Slash

declare -a arr=("Colon" "Dash" "Period" "Slash")

test_dir=Dot_Matrix_Test_$1

mkdir $test_dir

cd $test_dir

for i in {0..9}
do
	mkdir $i
done

for i in {A..Z}
do
	mkdir $i
done

for i in "${arr[@]}"
do
	mkdir $i
done

