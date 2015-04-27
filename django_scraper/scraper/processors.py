# -*- coding: UTF-8 -*-   
import sys,re
reload(sys)
sys.setdefaultencoding("utf-8")

# attention: you will get nothing from loader_context
def pre_5253_content(text, loader_context):

    iframe_re = re.compile('<iframe src="')
    content = re.sub(iframe_re, '<iframe src="http://coc.m.5253.com', text)

    # remove ad
    content = re.sub(r'<script([\s\S]*)</script>', '', content)
    # remove style
    content = re.sub(r'style=".*?"', '', content)

    #remove space
    content = content.replace('<p>　　', '<p>')

    return content


def www_2_m(text, loader_context):
    return text.replace('www', 'm')

def gamedog_title(text, loader_context):
    return text.replace('·部落冲突', '')


def pre_gamedog_content(text, loader_context):
    return text.replace('http://mimg1', 'http://img1')