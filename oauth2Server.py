#!/usr/bin/env python
 
import BaseHTTPServer


callback = None
# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
 
  
  # GET
  def do_GET(self):
        # Send response status code
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()
 
        # Send message back to client
        message = "Hello world!"
        # Write content as utf-8 data
        print message
        print self.path
        print "self.path %s" %self.path
        CODE_FROM_URL = self.path.split('=')[1]
        print "CODE FROM URL %s" %CODE_FROM_URL
        callback( CODE_FROM_URL )
        return



def run():
  
  print 'starting server...'
 
  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('127.0.0.1', 8081)
  httpd = BaseHTTPServer.HTTPServer(server_address, testHTTPServer_RequestHandler)
  # httpd.setCallback( videoVimeo.processResoponse )
  print 'running server... for 1 response only'
  httpd.handle_request()
  print "exit from the server"
  
  return

if __name__ == '__main__':
    run()
