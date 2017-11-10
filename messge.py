#coding=utf-8
import pycurl
import json
from urllib import urlencode

Authorization = ''

def change():
    global Authorization
    Authorization = '717ce1b0-0d2d-4498-91b6-79e2cae33e3c'


def upload(filename):
    header = ['Content-Type: multipart/form-data',
            'Accept:*/*',
            'Authorization:Bearer '+ Authorization
            ]
    pc = pycurl.Curl()
    url='https://openapi.saicmotor.com/services/cloud/sds/v1.0.0/upload?fileName=test&applicationName=ICE'
    pc.setopt(pycurl.POST, 1)
    pc.setopt(pycurl.URL, url)
    pc.setopt(pycurl.HTTPHEADER,header)
    pc.setopt(pycurl.HTTPPOST, [('upfile', (pc.FORM_FILE, filename) ) ])

    pc.perform()
    response_code = pc.getinfo(pycurl.RESPONSE_CODE)
    print response_code
    pc.close()

#def headData():


def msg():

    import md5
    import random

    m1 = md5.new();
    roll = random.randint(0, 1000000)
    m1.update(str(roll) + "o1rdfiui6p7reat6")
    key = m1.hexdigest()

    print roll
    print key

    header=['Content-Type: application/json',
            "Accept: application/json",
            "X-SMS-SEED:"+str(roll),
            "X-SMS-SIGN:"+key,
            "Authorization: Bearer "+Authorization
        ]
    '''
    content = {
      'content': 'test_string',
       'dest_id': '15201751803',
         'market': 'false',
           'delivery_report': 'true',
              'signature_id': '0'
    }
    '''

    content = '[{ "content": "HELLO_WORLD", "dest_id": "15201751803",    "market": false,      "delivery_report": true,  "signature_id": 0    }]'
    
    c = pycurl.Curl()
    url='https://openapi.saicmotor.com/opensaic/cloud/sms/v1.0.0/msg/98'
    #postfields = json.dumps(content)

    c.setopt(c.URL, url)
    c.setopt(c.HTTPHEADER, header)
    #c.setopt(c.HEADERFUNCTION,headData)
    c.setopt(c.POSTFIELDS,content)
    #pc.setopt(pc.HTTPPOST, [('upfile', (pc.FORM_FILE, content) ) ])
#    c.setopt(c.HTTPPUT, content)
    c.setopt(c.CUSTOMREQUEST,"PUT")
    print c.getinfo(c.HTTP_CODE)
    c.perform()
    c.close()

if __name__ == '__main__':
    #file = '/home/guan/Desktop/hackfdu/word.txt'
    change()
    #upload(file)
    msg()
