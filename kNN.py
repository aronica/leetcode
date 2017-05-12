from numpy import *
import os
__author__ = 'fafu'


from xml.etree import ElementTree
#

class ConfigCmdExecutor(object):
    def __init__(self):
        pass

    def execute(self,cmd_data):
        root = ElementTree.fromstring(cmd_data)
        cmd_list = []
        exit_first = False
        callhome = False
        Exit = False
        cmd = "Default"
        idx = 0
        node_lst = root.find('{http://www.cisco.com/nxos:1.0}exec-command').findall('{http://www.cisco.com/nxos:1.0}cmd')
        for item in node_lst:
            if idx == 0 and item.text != "configure terminal":
                idx = 1
                continue
            if not exit_first and item.text == "exit":
                exit_first = True
            elif exit_first and item.text == "callhome" and not callhome:
                callhome = True
            elif exit_first and callhome:
                cmd_content = item.text
                if cmd_content.find("periodic-inventory notification frequency")!=-1:
                    os.popen('clish -w "privileged-view" -c "'+cmd_content+'"').read()
                    cmd = "periodic-inventory notification frequency"
            elif exit_first and callhome and item.text.find("destination-profile nms compress-message")==0:
                break
        return cmd


def main():
    parser = ConfigCmdExecutor()
    # parser.parse_cmd_template_adapter()
    cmd = """<?xml version="1.0" encoding="UTF-8"?>
<nf:rpc message-id="963" xmlns:nf="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns="http://www.cisco.com/nxos:1.0">
<exec-command>
<cmd>configure terminal</cmd>
<cmd>callhome</cmd>
<cmd>alert-group inventory user-def-cmd show environment power</cmd><cmd>alert-group inventory user-def-cmd show gps location</cmd><cmd>alert-group inventory user-def-cmd show interface</cmd><cmd>alert-group inventory user-def-cmd show environment temperature</cmd><cmd>alert-group inventory user-def-cmd show door</cmd><cmd>alert-group inventory user-def-cmd show system uptime</cmd><cmd>exit</cmd><cmd>callhome</cmd><cmd>periodic-inventory notification frequency 350</cmd><cmd>exit</cmd><cmd>backup-battery un-inhibit discharge</cmd><cmd>callhome</cmd><cmd>destination-profile nms compress-message</cmd><cmd>exit</cmd><cmd>end</cmd></exec-command></nf:rpc>
    """
    parser.execute(cmd)

if __name__ == '__main__':
    main()
