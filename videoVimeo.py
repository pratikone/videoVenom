import vimeo

v = vimeo.VimeoClient(
    key="3baa464c8b42baf01019bacfef971e9e939a42c0",
    secret="8vNFwEfVmT+nu6okpSmzkFXuUTvjJPyUTIySqyEPYlbQsr+C2OAPhY+uunbY3RE0P9tFVrwxpKbznbErzpcuue6UMhTdn70bJKQVl4OAgHFGif2pVq/aspdxE/5neJjJ")

vimeo_authorization_url = v.auth_url(['public', 'private','upload'], 'https://api.vimeo.com/oauth/authorize','')

try:
    token, user, scope = v.exchange_code(vimeo_authorization_url, 'https://api.vimeo.com/oauth/access_token')
    print scope
except vimeo.auth.GrantFailed:
    # Handle the failure to get a token from the provided code and redirect.
    print token

video_uri = v.upload('C:\Python27\codes\/vide_mani\/new_video_kind175.mp4')


#v.upload_picture('/videos/12345', 'C:\Python27\codes\vide_mani\a.jpg', activate=True)