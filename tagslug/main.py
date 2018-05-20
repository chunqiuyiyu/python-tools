import os

tags = [x for x in os.listdir('./') if os.path.isdir(os.path.join('./',x))]

with open('./tagslug.yaml', 'w') as f:
  f.write('tag_map:\n')
  for tag in tags:
    f.write(tag + '\n')
