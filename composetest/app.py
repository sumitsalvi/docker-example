import time

from flask import Flask
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core.context import Context

app = Flask(__name__) 

@app.route('/') 
def hello_world():
    xray_func() 
    return 'Hello World'

def xray_func():
    # xray_recorder.configure(
    #     sampling=True,
    #     context_missing='LOG_ERROR',
    #     daemon_address='0.0.0.0:2000',
    #     # plugins=('ec2_plugin'),
    #     service='my-app',
    #     context=Context()
    # )
    # Start a segment
    segment = xray_recorder.begin_segment('segment_name')
    # Start a subsegment
    subsegment = xray_recorder.begin_subsegment('subsegment_name')
    print("Hello here...")
    # Add metadata or annotation here if necessary
    segment.put_metadata('key', dict, 'namespace')
    subsegment.put_annotation('key', 'value')
    xray_recorder.end_subsegment()

    # Close the segment
    xray_recorder.end_segment()
  
if __name__ == '__main__':
    xray_func()
    