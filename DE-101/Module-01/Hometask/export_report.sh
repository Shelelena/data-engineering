#!/bin/sh

jupytext --from py:percent --to notebook report.py
jupyter nbconvert --no-input --to html --execute report.ipynb

rm -f report.ipynb