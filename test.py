import sys
import os
import json
import requests

def register(user_data):
    headers = {"Content-Type":"application/json"}
    response = requests.post('http://127.0.0.1:5000/register',headers=headers,data=json.dumps(user_data))
    if response.status_code == 200:
        print("REGISTER: SUCCESS")
    else:
        print("REGISTER: FAILURE")
        print(response.text)

def submit_job(job_data,filename):
    files = {'job_files':open(filename,'rb')}
    response = requests.post('http://127.0.0.1:5000/post_job',files=files,data=job_data)

if __name__ == "__main__":

    user_data = {'username':'abc','password':'abc','account_id':123}

    job_data = {'username':'abc',
                'password':'abc',
                'account_id':123,
                'est_hours':0.5,
                'payout':1.2}

    #register(user_data)
    submit_job(job_data,'learning.tar.gz')
