#!/bin/sh

ipynb-py-convert report.py report.ipynb
jupyter nbconvert --no-input --to html --execute report.ipynb

rm -f report.ipynb