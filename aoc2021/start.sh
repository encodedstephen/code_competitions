#!/bin/bash

DIR=`dirname $0`

if [[ $# -ne 1 ]]; then
  echo "usage: $0 <day>"
  exit
fi

num=$1
cp -R $DIR/template day$num
# sed -i '' "s/dayxxx/day${num}/g" day${num}/main.py
AOC_COOKIE=`cat .aoc-cookie`
curl -b "session=$AOC_COOKIE" https://adventofcode.com/2021/day/${num}/input > day${num}/input.txt
