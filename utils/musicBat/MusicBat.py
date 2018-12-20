# coding=utf-8
import os
import urllib
import requests
import sys
import re
import sre

reload(sys)
sys.setdefaultencoding("utf-8")

# 虾米XML示例
# http://www.xiami.com/song/playlist/id/1774966620/object_name/default/object_id
urls = {"http://www.xiami.com/chart/data?c=101&type=0&page=1&limit=50&_=1446955470849",
        "http://www.xiami.com/chart/data?c=101&type=0&page=2&limit=50&_=1446955470849",
        "http://www.xiami.com/chart/data?c=101&type=0&page=3&limit=50&_=1446955470849",
        "http://www.xiami.com/chart/data?c=101&type=0&page=4&limit=50&_=1446955470849"}
head = {
    'Referer': 'http://www.xiami.com/chart/index/c/101/type/0?spm=a1z1s.2943549.6827461.1.V82Q6I',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
}
i = 0

for url in urls:
    req = requests.get(url, headers=head)
    type = sys.getfilesystemencoding()
    req_content = req.text.decode("UTF-8").encode(type)

    strs = re.findall('data-mp3="(.*?)".*data-title="(.*?)"', req_content)
    # strs_title = re.findall('data-title="(.*?)"', req_content)

    # 凯撒阵列解析
    s = sre.GetURL()

    path = os.getcwd()
    parent_path = os.path.dirname(path)
    f = open('org_url.txt', 'a')
    for strItem in strs:
        musciUrl = s.get(strItem[0])
        musciName = strItem[1].replace('<', '').replace('>', '').replace('/', '').replace('\\', '').replace('|', '').replace(':', '').replace(
            '\"', '').replace('\*', '').replace('?', '')
        # <>,/,\,|,:,"",*,?
        urllib.urlretrieve(musciUrl, parent_path + '\\com.cherie.src\\' + musciName + ".mp3")
        f.write(musciUrl + '\n')
        print musciName + '\tNo' + str(i) + '\tcomplete!'
        i += 1
    f.close()

