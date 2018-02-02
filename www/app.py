# !usr/bin/env python3
# -*- coding: utf-8 -*-
# Create by Jump on 2018/02/02 15:51
__author__ = 'Jump Hu'
# Github : https://github.com/jump1003
"""搭建web app骨架，借此可继续添加其他效果"""
import logging
import asyncio
import os
import json
import time
from datetime import datetime
from aiohttp import web

# 日志
logging.basicConfig(level=logging.INFO)


def index(request):
	return web.Response(body=b'<h1>This is Body! U can add something!</h1>', content_type='text/html')

@asyncio.coroutine
def init(loop):
	app = web.Application(loop=loop)
	app.router.add_route('GET', '/', index)
	srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 8080)
	logging.info('Server started at http://127.0.0.1:8080...')
	return srv


if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(init(loop))
	loop.run_forever()
