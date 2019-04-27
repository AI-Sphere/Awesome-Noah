# -*- coding: UTF-8 -*-.
import json
import os
import urllib.parse

cv = './InfoCenter/cv.json'
nlp = './InfoCenter/nlp.json'
dm = './InfoCenter/data_mining.json'
# ongoing = './InfoCenter/ongoing.json'

base_url = "https://github.com/AI-Sphere/Awesome-AI-Competitions/tree/master/"

header_tmp = """
# {}

比赛链接：{}

## 解决方案
|排名|地址|
|----|----|
"""

def generate_sub_md(path, prefix='NLP'):


    try:
        contents = json.load(open('%s' % path, encoding='utf-8'))
    except:
        print("JSON FORMAT ERROR: please check your %s file." % path)
        exit(1)

    res_dct = {}
    for content in contents:
        os.makedirs('{}/{}'.format(prefix, content['title']), exist_ok=True)
        with open('{}/{}/readme.md'.format(prefix, content['title']), 'w') as fout:
            if not content['game link']:
                content['game link'] = 'You can search it on baidu or google.'
            concat_md = header_tmp.format(content['title'], content['game link'])
            for k, v in content['solutions'].items():
                if type(v) is list:
                    v = '<br>'.join(v)
                concat_md += "|{}|{}|\n".format(k, v)
            fout.write(concat_md)
            encoded_prefix = urllib.parse.quote(prefix)
            encoded_title = urllib.parse.quote(content['title'])
            concat_url = base_url + '{}/{}'.format(encoded_prefix, encoded_title)
            res_dct[(content['title'], concat_url)] = len(content['solutions'])
    return [i[0] for i in sorted(res_dct.items(), key=lambda d:d[1], reverse=True)]

def generate_home_md(contents):
    md = '\n'.join(['    - [{}]({})'.format(c[0], c[1]) for c in contents])
    return md

cv = generate_sub_md(cv, 'CV')
nlp = generate_sub_md(nlp, 'NLP')
dm = generate_sub_md(dm, 'Data Mining')
# ongoing = generate_sub_md(ongoing, 'Ongoing')


with open('./res/home_templete.md', 'r') as fin, open('readme.md', 'w') as fout:
    s = ''.join(fin.readlines())
    # ongoing_1 = '\n'.join(['- [{}]({})'.format(c[0], c[1]) for c in ongoing])
    nlp = generate_home_md(nlp)
    cv = generate_home_md(cv)
    dm = generate_home_md(dm)
    fout.write(s.format(nlp, cv, dm))