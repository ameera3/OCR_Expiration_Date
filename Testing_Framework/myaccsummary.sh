#!/bin/sh
# Copyright 2013 Nick White <nick.white@durham.ac.uk>
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.

usage="$0 inputdir

  inputdir    directory containing ground truth and accompanying
               .txt text files"

test $# -ne 1 && echo "Usage: $usage" && exit 1
inputdir="$1"

accprog=accuracy

sum=0
n=0
for i in `find "$inputdir" -type f -name '*.png' | sort`; do
	b=`basename "$i" .png`
        name=$(echo "$i" | sed -e 's/\.[^.]*$//')
        printf "%s: " "$b"
	acc=`ocrevalutf8 $accprog "$name-gt.txt" "$inputdir/$b.txt" \
	     | awk '/Accuracy$/ {print $1; exit}' | sed 's/%//'`
	n=`expr $n + 1`
	sum=`echo $sum + $acc | bc -l`

	printf "%.2f%%\n" "$acc"
done

if test $n -ne 0; then
        avg=`echo $sum / $n | bc -l`
        printf "$training - Average Accuracy: %.2f%%\n" "$avg"
fi

