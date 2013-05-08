#!/bin/bash

FILE="$1.rst"
NAME=$1
TITLE=$2

echo ".. _$NAME:" > $FILE 
echo "" >> $FILE
echo "================================" >> $FILE
echo " $TITLE" >> $FILE
echo "================================" >> $FILE
echo "" >> $FILE
echo ".. contents::" >> $FILE
echo "    :local:" >> $FILE
echo "    :depth: 1" >> $FILE
echo "" >> $FILE
echo "TODO: needs content" >> $FILE
echo "" >> $FILE

echo "    $NAME" >> index.rst
