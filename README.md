# Capture utm coordinates from public documents

## Description 

* A simple python script that captures utm geographic coordinates from Brazilian public documents and saves in a .txt files. 

## Why

* This was custom made for a GreenPeace analyst that needed to map a conservation unit but was spending hours of work to manually transcript these information.

## What it does:

* Captures string occurrences everytime it finds a matching pattern for E: 356.344,839 or N: 8.923.122,327 or similar.


<p float="left"> From pages of this ->
  <img src="https://github.com/nnbuainain/capt_utm_coords/blob/main/figs/print_document.png?raw=true" width="360" />
to ->>
  <img src="https://github.com/nnbuainain/capt_utm_coords/blob/main/figs/polygon_UC.jpeg?raw=true" width="190" /> 
-> in minutes
</p>

## How it works
*You need to have python 3 installed*

1) Copy and paste text whose coordinates you want to capture, from .pdf, .doc or whatever to .txt file, and name it text_public_doc.txt
2) Open terminal in the directory where this .txt file is
3) run ```python3 capt_utm_from_string.py ```
5) Your result should be in coords_results.txt
6) Open file in Microsoft Excel or other editor to format according to your GIS program and create your shapefile
