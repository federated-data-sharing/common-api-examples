import requests
import os
import json
import time
import logging
 
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s", datefmt='%Y-%m-%d %H:%M')

DEBUG=False
  
# Define the main loop we need to execute for each node
def task_automate(reference, endpoint, task, zip_processor):
    # Step 1 - setup headers
    headers = { 'Authorization': f'Bearer {os.environ["FDS_API_TOKEN"]}',
                'Content-Type': 'application/json'}
    # Step 2 - Post the task
    # /tasks
    logging.info(f'{reference} - Posting task: {endpoint}')
    r = requests.post(f'{endpoint}/tasks', headers=headers, data=json.dumps(task))
    if DEBUG:
        print(r.status_code)
        
    if r.status_code != 200:
        logging.error(f'{reference} - Failed to post task to endpoint: {endpoint}')
        print(r.text)
        return None
    
    response_json = r.json()
    if DEBUG:
        print(response_json)
    if 'message' in response_json:
        logging.error(f"{reference} - Failure Message received: {response_json['message']}")
        return None   
    
    # get the ID for the task from the response
    task_id = response_json['data']['id']
    status = response_json['data']['status']
    logging.info(f'{reference} - Task ID: {task_id}/Status: {status}')

    headers = { 'Authorization': f'Bearer {os.environ["FDS_API_TOKEN"]}'}
    # Step 3 - if running, check status periodically
    while status == 'Running':
        # Wait 5 seconds before retrying
        time.sleep(5)
        r = requests.get(f'{endpoint}/tasks/{task_id}', headers=headers)
        if DEBUG:
            print(r.status_code)
            print(r.text)
        
        if r.status_code != 200:
            print(f'{reference} - Failed to get task status from endpoint: {endpoint}')
            return None

        response_json = r.json()
        status = response_json['status']
        logging.info(f'{reference} - Task ID: {task_id}/Status: {status}')

    
    # Step 4 - if complete, return results; if not return empty list
    if status == 'complete':
        logging.info(f'{reference} - Complete: Task ID: {task_id}/Status: {status}')
        
        output_file = f'./output/{task_id}.zip'
        logging.info(f'{reference} - Downloading to file: {output_file}')
        
        r = requests.get(f'{endpoint}/tasks/{task_id}/result', headers=headers)
        if r.status_code != 200:
            logging.error(f'{reference} - Failed to get task output: {task_id}')
            return None

        with open(output_file, 'wb') as fh:
            for chunk in r.iter_content(chunk_size=1024*1024):
                fh.write(chunk)
        logging.info(f'{reference} - Downloaded: {output_file}')
        
        
        return (reference, zip_processor(output_file))
    else:
        logging.error(f'{reference} - Failed: Task ID: {task_id}/Status: {status}')
        return None