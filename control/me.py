#
# 关于我控制器
#

import tornado.web


class MeHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")