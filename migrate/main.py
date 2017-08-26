# coding=utf-8
import MySQLdb
import time
import re
import requests

# connect database
conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='root',
        db ='typecho',
        charset='utf8',
        use_unicode=True
        )
cur = conn.cursor()
datas = cur.execute("select * from typecho_contents where type = 'post'")
info = cur.fetchmany(datas)

# output data to files
index = 0
for data in info:
  index += 1
  with open('posts/' + data[2] + '.md', 'w') as f:
    f.write('---\n')
    # title
    f.write('title: ' + data[1].encode('utf8') + '\n')
    # date
    curtime = data[3];
    date = time.strftime('%Y-%m-%d %H:%M', time.localtime(curtime))
    f.write('date: %s\n' % date)

    # tags
    tag_str = '';
    tags = cur.execute("select mid from typecho_relationships where cid = %d" % data[0])
    tags = cur.fetchmany(tags)
    for tag in tags:
      meta = cur.execute("select name from typecho_metas where mid = %d and type = 'tag'" % tag)
      names = cur.fetchmany(meta)
      for name in names:
        tag_str += name[0].encode('utf8') + ', '

    if len(tag_str) > 0:
      tag_str = '[' + tag_str[:-2] + ']'
      f.write('tags: %s\n' % tag_str)
    f.write('---\n')

    # article
    article = data[5].encode('utf8');
    # delete the flag of markdown: <!--markdown-->
    article = article.replace('<!--markdown-->', '')
    article = article.replace('\n', '')

    # download img in blogs
    pattern = re.compile(r'https?://.[^=+\\\r]*?\.(?:gif|png|jpg|jpeg)')
    match = re.findall(pattern, article)
    if match:
        for img in match:
            name = img.split('/')[-1]
            article = article.replace(img, '/img/' + name);
            ir = requests.get(img)
            if ir.status_code == 200:
                open('img/' + name, 'wb').write(ir.content)
    f.write(article + '\n')
  print 'Posts: %d / %d' % (index, len(info))
  index = 0

# out put tags
datas = cur.execute("select * from typecho_metas where type = 'tag'")
tags = cur.fetchmany(datas)
for tag in tags:
  index += 1
  with open('tags.yaml', 'a') as f:
    f.write(tag[1].encode('utf8') + ': ' + tag[2].encode('utf8') + '\n')

  print 'Tags: %d / %d' % (index, len(tags))

cur.close()
conn.commit()
conn.close()
