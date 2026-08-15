import requests
import base64

access_token="24.ac7c8355f902d5c776dde974d55de4dd.2592000.1663656989.282335-27099465"

def face_register(file1path,user_id):
    f = open(file1path,'rb')
    image = base64.b64encode(f.read())
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/update"
    params = {'image':image, 'image_type':'BASE64','group_id':'vip','user_id':user_id,'quality_control':'LOW'}
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print (response.json())

face_register('Jane.png', 'Jane')
