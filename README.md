# ais-nord-stream
Code to process AIS data around the nord stream incidents 

# Files:
 -algo.py: Contains methods to determine if points fall in the NS1 or NS2 sabotage areas
- convert_ais.py: Filters AIS data to see what lies within NS1/NS2 areas
- helpy.py: some random functions for post processing

# Usage:

Read from a file
`python3 convert_ais.py -f rostock/aisdk-2022-09-06.csv`

Read from a directory (and process each file)
`python3 convert_ais.py -d rostock/`

Merge filtered files into csv, json, and kml outputs
`python3 convert_ais.py -merge output/`

Notes:
1. Processing a directory generates a file "processed.json" which stores processed files. This allows you to resume a job if there's an interruption or partially process. Unless you want to resume where you left off, delete this file before running convert_ais.py in directory mode.
