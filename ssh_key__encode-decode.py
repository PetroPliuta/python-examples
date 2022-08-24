### key to string
import json

with open('original') as orig, open('encoded', 'w') as enc:
    text = orig.read()
    json_=json.dumps(text)
    enc.write(json_)

### urlencode
import urllib.parse

with open('encoded') as enc, open('urlencoded','w') as urlencoded:
    text=enc.read()
    urlencoded.write(urllib.parse.quote_plus(text))

### urldecode
import urllib.parse
with open('urlencoded') as urlencoded, open('urldecoded','w') as urldecoded:
    text = urlencoded.read()
    urldecoded.write(urllib.parse.unquote_plus(text))

### string to key
import json
with open('urldecoded') as urldecoded, open('decoded','w+') as decoded:
    decoded.write(json.load(urldecoded))
