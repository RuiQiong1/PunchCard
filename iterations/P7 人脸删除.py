import json
import requests

access_token="24.ac7c8355f902d5c776dde974d55de4dd.2592000.1663656989.282335-27099465"
del_msg=''  #删除显示信息
user_id='Jane'  #要删除的用户id

# 人脸删除函数
def face_delete(user_idx, face_token):
    request_url = "	https://aip.baidubce.com/rest/2.0/face/v3/faceset/face/delete"

    params = json.dumps({"user_id": user_idx, "group_id": "vip", "face_token": face_token})
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, data=params, headers=headers).json()
    if response['error_code'] == 0:
        del_msg = "删除成功"
    else:
        del_msg = response['error_msg']
    print(del_msg)


# 获取用户的face_token
request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/face/getlist"
params = json.dumps({"user_id": user_id, "group_id": "vip"})
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/json'}
response = requests.post(request_url, data=params, headers=headers).json()
if response['error_msg'] == 'SUCCESS':
    for i in response['result']['face_list']:
        face_token = i['face_token']
        face_delete(user_id, face_token)
else:
    del_msg = response['error_msg']
    print(response['error_msg'])
