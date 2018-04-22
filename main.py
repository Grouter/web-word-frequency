from Search import FreqSearch
from Visualization import FqVis

Search = FreqSearch()
Search.process("https://github.com/", 20)

Visual = FqVis()
Visual.insert_sorted_data(Search.get_data())

while True:
    Visual.run()
