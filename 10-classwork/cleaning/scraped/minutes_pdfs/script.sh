#!/bin/bash
FILES=*.pdf
for f in $FILES
do
  echo "Processing $f..."
  convert -density 300 $f -append $f.png
  tesseract $f.png $f.txt
done
