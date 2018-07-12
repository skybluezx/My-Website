#
# WEB入口
#

import os.path

import tornado.ioloop

from control.index import *


if __name__ == "__main__":
    application = tornado.web.Application(
        handlers=[(r"/", IndexHandler), ],
        template_path=os.path.join(os.path.dirname(__file__), "templates")
    )
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
