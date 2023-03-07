# ais-nord-stream
Code to process AIS data around the nord stream incidents 

# Files:
 -algo.py: Contains methods to determine if points fall in the NS1 or NS2 sabotage areas
- convert_ais.py: Filters AIS data to see what lies within NS1/NS2 areas
- helpy.py: some random functions for post processing

# Usage:

python3 convert_ais.py -f rostock/aisdk-2022-09-06.csv
