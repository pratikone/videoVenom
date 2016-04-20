import threading
import vimeo
import webbrowser
import oauth2Server


caller = None

def requestOAuth() :
  oauth2Server.callback = processResoponse
  
  t = threading.Thread(target=oauth2Server.run, args = ())
  t.start()

  v = vimeo.VimeoClient(
      key="3baa464c8b42baf01019bacfef971e9e939a42c0",
      secret="8vNFwEfVmT+nu6okpSmzkFXuUTvjJPyUTIySqyEPYlbQsr+C2OAPhY+uunbY3RE0P9tFVrwxpKbznbErzpcuue6UMhTdn70bJKQVl4OAgHFGif2pVq/aspdxE/5neJjJ")

  vimeo_authorization_url = v.auth_url(['public', 'private','upload'], 'http://localhost:8081','')
  webbrowser.open(vimeo_authorization_url)

def processResoponse(CODE_FROM_URL) :
  """This section completes the authentication for the user."""
  v = vimeo.VimeoClient(
          key="3baa464c8b42baf01019bacfef971e9e939a42c0",
          secret="8vNFwEfVmT+nu6okpSmzkFXuUTvjJPyUTIySqyEPYlbQsr+C2OAPhY+uunbY3RE0P9tFVrwxpKbznbErzpcuue6UMhTdn70bJKQVl4OAgHFGif2pVq/aspdxE/5neJjJ")
  # You should retrieve the "code" from the URL string Vimeo redirected to.  Here that's named CODE_FROM_URL
  try:
      token, user, scope = v.exchange_code(CODE_FROM_URL, 'http://localhost:8081')
      print token
      print scope
  except vimeo.auth.GrantFailed:
      print "tokening failed"

  print caller
  caller.vimeoObj = v
  
  # Store

def upload(vimeoObj, VidLocation, titleVid, description, tag) :
  video_uri = vimeoObj.upload(VidLocation)
  vimeoObj.patch(video_uri, data={'name': titleVid, 'description': description })


if __name__ == "__main__":
  caller = "ABC"
  requestOAuth()