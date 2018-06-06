import re

x = "3. Structuring Machine Learning Projects  (deeplearning.ai)"

#match = re.match(' (.).jpg', x)

match = re.findall('.\s+(.*.jpg)', x)

print(match)