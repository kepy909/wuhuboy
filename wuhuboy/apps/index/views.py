# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render


def index(request):

    return render(request, "index.html")

@csrf_exempt
def get_baidu(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        import requests
        usrname = request.POST.get("usrname")
        usrpwd = request.POST.get("usrpass")
        docinfo = request.POST.get("docinfo")

        cookies = {
            'usrname': usrname,
            'usrpwd': usrpwd,
        }

        """
        用户：a9t6w5密码：qr6yn   剩余2000+点（提示用户名不存在就是今天下载超过5次了）
        用户：tkg1vq 密码：ehc12 剩余9000+点
        （付费的无法下载）
        每个ip每天限制5次。如果拨号上网请重启路由器还能继续下载。如果固定ip用完五次可以使用备用方法。"""

        headers = {
            'Origin': 'http://139.224.236.108',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-HK;q=0.6',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept': '*/*',
            'Referer': 'http://139.224.236.108/mobile.html',
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep-alive',
        }

        data = [
            ('usrname', usrname),
            ('usrpass', usrpwd),
            ('docinfo', docinfo),
            ('taskid', 'up_down_doc'),
        ]

        response = requests.post('http://139.224.236.108/post.php', headers=headers, cookies=cookies, data=data)

        return JsonResponse(response, safe=False)
