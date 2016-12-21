
#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /assignment3/
#####################################################################

from bottle import route, run, default_app, debug

def htmlify(title, content):
    page = """<!DOCTYPE html>
              <html>
                  <head>
                      <title>""" + title + """</title>
                      <meta charset="utf-8" />
                  </head>
                  <body>
                      """ + content + """
                  </body>
              </html>"""
    return page

def a3_index():
    return htmlify("My lovely website","This is going to be an awesome website, when it is finished.")

def website_index():
    return htmlify('My lovely homepage',
                   """
                   <!-- p><a href="/assignment1/">Click for my assignment 1.</a></p -->
                   <!-- p><a href="/assignment2/">Click for my assignment 2.</a></p -->
                   <p><a href="/assignment3/">Click for my assignment 3.</a></p>
                   """)

route('/assignment3/', 'GET', a3_index)
route('/', 'GET', website_index)

#####################################################################
### Don't alter the below code.
### It allows this website to be hosted on PythonAnywhere
### OR run on your computer.
#####################################################################

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on PythonAnywhere
application = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
  run()

