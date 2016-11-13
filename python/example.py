from sdk import OpenMoticsApi, OpenMoticsCloudApi, traceback


# Test code for the gateway api.
api = OpenMoticsApi("user", "pass", "localhost:8443", False)
print api.get_output_status()


# Test code for the cloud api.
api = OpenMoticsCloudApi("user", "pass")

def callback(msg):
    print msg

try:
    print api.msg_loop([ OpenMoticsCloudApi.MSG_OUTPUT_CHANGE ], callback)
except Exception as e:
    traceback.print_exc()
    #print "%s" % e.getMessage()


