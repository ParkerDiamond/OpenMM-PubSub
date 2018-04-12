import httplib2
import json
import time
import datetime

if __name__ == '__main__':

    httplib2.debuglevel     = 0
    http                    = httplib2.Http()
    content_type_header     = "application/json"

    url = "http://127.0.0.1:5000/register"

    data = {    'username':         "bioinformatics",
                'password':         "isverydope",
           }

    headers = {'Content-Type': content_type_header}
    print ("Posting %s" % data)

    for i in range(5):
        response, content = http.request( url,
                                          'POST',
                                          json.dumps(data),
                                          headers=headers)
        print (response)
        print (content)
        time.sleep(3)
