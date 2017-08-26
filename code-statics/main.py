import os
import re

basedir = "path/to/code/src"
count = 0

def statics(filepath):
  global count
  files = os.listdir(filepath)
  for fi in files:
    fi_d = os.path.join(filepath,fi)
    if os.path.isdir(fi_d):
      statics(fi_d)
    else:
      name = os.path.join(filepath,fi_d)
      # Only the js file is counted in this example
      if (name[-2:] == "js"):
        with open(name) as f:
          for l in f:
            # Remove whitespace line and annotations
            if (re.search(r'\\', l) == None and re.match(r'^\s?$', l) == None):
             count = count + 1

if __name__ == '__main__':
  statics(basedir)
  print count