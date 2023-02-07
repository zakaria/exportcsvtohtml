#!/usr/bin/python3

import os
import argparse
import csv
from prettytable import PrettyTable
from prettytable import from_csv
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("--directory", help='directory of csv files')
args = parser.parse_args()

print(args.directory)

html_head = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
    <meta name="generator" content="Hugo 0.108.0">
    <title>Heroes · Bootstrap v5.3</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
  </head><body><div class="container">
"""

html_foot = '</div></body></html>'

folder = args.directory
output = ''

for file in os.listdir(folder):
    filepath = folder + '/' + file
    if( os.path.isfile(filepath) ):
        csv_file = open(filepath, "r")
        html_table = from_csv(csv_file)
        csv_file.close()
        output += '<h2>' + filepath + '</h2>'
        
        # Set className to table
        table_output = html_table.get_html_string()
        output += table_output.replace("<table", '<table class="table table-striped "')

filename = 'export_' + datetime.now().strftime("%Y%m%d%H%M%S") + '.html'
output_file = open(filename, 'w')
output_file.write(html_head + output + html_foot)
output_file.close()

print(filename)