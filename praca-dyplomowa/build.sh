#!/bin/bash

pdflatex Praca_magisterska.tex
bibtex Praca_magisterska.aux
pdflatex Praca_magisterska.tex
pdflatex Praca_magisterska.tex