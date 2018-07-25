#
# WEB入口
#

import os.path

import tornado.ioloop

from control.index import *
from control.me import *
from control.blog import *


if __name__ == "__main__":
    application = tornado.web.Application(
        handlers=[
            (r"/", IndexHandler),
            (r"/me", MeHandler),
            (r"/blob", BlogHandler),
        ],
        template_path=os.path.join(os.path.dirname(__file__), "view")
    )
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
