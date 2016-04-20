import threading
import vimeo
import webbrowser
import oauth2Server


caller = None
KEY="3baa464c8b42baf01019bacfef971e9e939a42c0"
SECRET="8vNFwEfVmT+nu6okpSmzkFXuUTvjJPyUTIySqyEPYlbQsr+C2OAPhY+uunbY3RE0P9tFVrwxpKbznbErzpcuue6UMhTdn70bJKQVl4OAgHFGif2pVq/aspdxE/5neJjJ"
def requestOAuth() :
  oauth2Server.callback = processResoponse
  
  t = threading.Thread(target=oauth2Server.run, args = ())
  t.start()

  v = vimeo.VimeoClient(
      key=KEY,
      secret=SECRET)

  vimeo_authorization_url = v.auth_url(['public', 'private','upload'], 'http://localhost:8081','')
  webbrowser.open(vimeo_authorization_url)

def processResoponse(CODE_FROM_URL) :
  """This section completes the authentication for the user."""
  v = vimeo.VimeoClient(
          key=KEY,
          secret=SECRET)
  # You should retrieve the "code" from the URL string Vimeo redirected to.  Here that's named CODE_FROM_URL
  try:
      token, user, scope = v.exchange_code(CODE_FROM_URL, 'http://localhost:8081')
      print token
      print scope
  except vimeo.auth.GrantFailed:
      print "tokening failed"

  print caller
  caller.vimeoObj = token
  
  # Store

def upload(vimeoObj, VidLocation, titleVid, description, tag) :
    v = vimeo.VimeoClient(token=vimeoObj,
          key=KEY,
          secret=SECRET)
    video_uri = v.upload(VidLocation)
    v.patch(video_uri, data={'name': titleVid, 'description': description })


if __name__ == "__main__":
  caller = "ABC"
  requestOAuth()