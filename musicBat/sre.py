# coding=utf-8
import urllib


# 虾米凯撒阵列示例
# 8
# h2fmF 32246 4%ka% E%845 E
# tFii2 269%_ 23ee5 5554E -
# t%l.5 5%%51 _FybE 8E36% n
# p2ec6 652E6 la%1c f8985 u
# %F.o% %EF53 .u3c5 ba45E l
# 3mxm2 23149 mtD%8 9824- l
# A5i%F F8712 phb5% 3d-4%
# %.a22 78737 3_dE5 791%5

#h2fmF322464%ka%E%845EtFii2269%_23ee55554E-t%l.55%%51_FybE8E36%np2ec6652E6la%1cf8985u%F.o%%EF53.u3c5ba45El3mxm223149mtD%89824-lA5i%FF8712phb5%3d-4%%.a22787373_dE5791%5

class GetURL:
    def __init__(self):
        pass

    def get(self, url):
        org_url = url
        url_col_max = int(org_url[0])
        url_len = len(org_url) - 1
        url_row = url_len / url_col_max
        url_col = url_len % url_col_max
        org_url = org_url[1:]
        index_x = 0
        index_y = 0
        new_url = ''
        while index_x < url_row + 1:
            index_y = 0
            while index_y < url_col:
                new_url = new_url + org_url[index_x + index_y * (url_row + 1)]
                index_y += 1
            index_y = url_col
            if index_x == url_row:
                break
            while index_y < url_col_max:
                new_url = new_url + org_url[index_x + url_col * (url_row + 1) + (index_y - url_col) * url_row]
                index_y += 1
            index_x += 1
        new_url = urllib.unquote(new_url)
        new_url = new_url.replace('^', '0')
        return new_url

