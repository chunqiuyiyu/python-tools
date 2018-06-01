import os

# Set blog path here
path = '../../my-blogs/public/tags'
tags = [x for x in os.listdir(path) if os.path.isdir(os.path.join(path,x))]
tmp = '  {}: {}\n'

# print(tags)
with open('./tagslug.yaml', 'w') as f:
  f.write('tag_map:\n')
  for tag in tags:
    f.write(tmp.format(tag, tag.lower()))
