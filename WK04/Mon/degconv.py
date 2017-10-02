import os
import tornado.ioloop
import tornado.web
import tornado.log

from jinja2 import \
  Environment, PackageLoader, select_autoescape


PORT = int(os.environ.get('PORT', '8888'))

ENV = Environment(
  loader=PackageLoader('app', 'templates'),
  autoescape=select_autoescape(['html', 'xml'])
)

class TemplateHandler(tornado.web.RequestHandler):
  def render_template (self, tpl, context):
    template = ENV.get_template(tpl)
    self.write(template.render(**context))

class FormHandler(TemplateHandler):
  def post (self):
    celsius = float(self.get_body_argument('celsius', ''))
    fahrenheit = celsius * 1.8 + 32

    self.set_header(
      'Cache-Control',
      'no-store, no-cache, must-revalidate, max-age=0')
    self.render_template("degconv.html", {"celsius": celsius, 'fahrenheit': fahrenheit})

  def get(self):
    self.set_header(
      'Cache-Control',
      'no-store, no-cache, must-revalidate, max-age=0')
    self.render_template("degconv.html", {})

def make_app():
    return tornado.web.Application([
        (r"/", FormHandler),
    ], autoreload=True)

if __name__ == "__main__":
    tornado.log.enable_pretty_logging()
    app = make_app()
    app.listen(PORT, print('Server started on localhost:' + str(PORT)))
    tornado.ioloop.IOLoop.current().start()
