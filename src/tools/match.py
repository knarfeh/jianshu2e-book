# -*- coding: utf-8 -*-
import re


class Match(object):
    @staticmethod
    def xsrf(content=''):
        xsrf = re.search(r'(?<=name="_xsrf" value=")[^"]*(?="/>)', content)
        if xsrf:
            return '_xsrf=' + xsrf.group(0)
        return ''

    @staticmethod
    def html_body(content=''):
        return re.search('(?<=<body>).*(?=</body>)', content, re.S).group(0)

    # 以上是zhihu相关

    @staticmethod
    def fix_html(content=''):
        content = content.replace('</br>', '').replace('</img>', '')
        content = content.replace('<br>', '<br/>')
        content = content.replace('<wbr>', '').replace('</wbr>', '<br/>')  # for SinaBlog

        for item in re.findall(r'\<span class="img2"\>.*?\</span\>', content):
            content = content.replace(item, '')
        for item in re.findall(r'\<script\>.*?\</script\>', content, re.S):
            content = content.replace(item, '')
        for item in re.findall(r'height=\".*?\" ', content):     # 因为新浪博客的图片的高,宽是js控制的,不加
            content = content.replace(item, '')                 # 这一段会导致无法匹配
        for item in re.findall(r'width=\".*?\" ', content):
            content = content.replace(item, '')
        for item in re.findall(r'\<cite\>.*?\</cite\>', content):
            content = content.replace(item, '')
        return content

    @staticmethod
    def jianshu(content=''):
        u"""

        :param content: jianshu个人主页的地址
        :return: re.match object
        """
        return re.search(r'(?<=jianshu\.com/users/)(?P<jianshu_id>[^/\n\r]*)(/latest_articles)', content)

    @staticmethod
    def jianshu_article_id(content=''):
        u"""

        :param content:
        :return:
        """
        return re.search(r'(?<=www\.jianshu\.com/p/)(?P<jianshu_article_id>[^/\n\r\']*)()', content)

    @staticmethod
    def fix_filename(filename):
        illegal = {
            '\\': '＼',
            '/': '',
            ':': '：',
            '*': '＊',
            '?': '？',
            '<': '《',
            '>': '》',
            '|': '｜',
            '"': '〃',
            '!': '！',
            '\n': '',
            '\r': ''
        }
        for key, value in illegal.items():
            filename = filename.replace(key, value)
        return unicode(filename[:80])
