from easysnmp import Session
from time import strftime
import time


class SnmpOperations:
    def __init__(self, host_name):
        self.hostname = host_name
        self.session = Session(hostname=self.hostname, community='public', version=3, timeout=10, retries=1, security_level='auth_with_privacy', security_username='CorinexComm', privacy_protocol='DES', privacy_password='9cd64013a8705146', auth_protocol='MD5', auth_password='2fa62fe8225bbd40')

    def config_upgrade_activate(self, device_type, action_type, filename, filesize, filemd5, ftpAddr, ftpType, ftpUser, ftpPass, ftpPort, mac):
        task_id = (strftime("%M%Y%H%S", time.gmtime()))
        if device_type == 'proxy' and action_type == 'config':
            mystring = ftpType + ' ' + ftpAddr + ' ' + ftpPort + ' ' + ftpUser + ' ' + ftpPass + ' ' + 'null {\"CMD\":[{\"TSK\":{\"ID\":' + task_id +',\"TGT\":[],\"ACT\":{\"NAME\":\"CONFIG\",\"PRIO\":100,\"EXP\":\"2100-12-24T18:53:44+00:00\",\"SET\":{\"ID\":\"' + filename + '\",\"SZ\":' + filesize +',\"SIG\":\"' + filemd5+ '\",\"DST\":0,\"EDT\":\"2016-06-24T16:53:44+00:00\",\"CM\":0}}}}]}'
            if self.session.set('1.3.6.1.4.1.6232.8.1.3.1.0', str(mystring), 's'):
                return mystring
            else:
                return "SNMPSET FAILURE!"
            #return str(self.session.set('1.3.6.1.4.1.6232.8.1.3.1.0', str(mystring), 's'))
        elif device_type == 'bpl' and action_type == 'config':
            mystring = ftpType + ' ' + ftpAddr + ' ' + ftpPort + ' ' + ftpUser + ' ' + ftpPass + ' ' + 'null {\"CMD\":[{\"TSK\":{\"ID\":' + task_id +',\"TGT\":[{\"DEV_ID\":\"' + mac + '\"}],\"ACT\":{\"NAME\":\"CONFIG\",\"PRIO\":100,\"EXP\":\"2100-12-24T18:53:44+00:00\",\"SET\":{\"ID\":\"' + filename + '\",\"SZ\":' + filesize +',\"SIG\":\"' + filemd5+ '\",\"DST\":1,\"EDT\":\"2016-06-24T16:53:44+00:00\",\"CM\":0}}}}]}'
            if self.session.set('1.3.6.1.4.1.6232.8.1.3.1.0', str(mystring), 's'):
                return mystring
            else:
                return "SNMPSET FAILURE!"
            #return self.session.set('1.3.6.1.4.1.6232.8.1.3.1.0', str(mystring), 's')
        elif device_type == 'proxy' and action_type == 'upgrade':
            mystring = ftpType + ' ' + ftpAddr + ' ' + ftpPort + ' ' + ftpUser + ' ' + ftpPass + ' ' + 'null {\"CMD\":[{\"TSK\":{\"ID\":' + task_id +',\"TGT\":[],\"ACT\":{\"NAME\":\"UPGRADE\",\"PRIO\":100,\"EXP\":\"2100-12-24T18:53:44+00:00\",\"SET\":{\"ID\":\"' + filename + '\",\"SZ\":' + filesize +',\"SIG\":\"' + filemd5+ '\",\"DST\":0,\"EDT\":\"2016-06-24T16:53:44+00:00\",\"CM\":0}}}}]}'
            if self.session.set('1.3.6.1.4.1.6232.8.1.3.1.0', str(mystring), 's'):
                return mystring
            else:
                return "SNMPSET FAILURE!"
            #return self.session.set('1.3.6.1.4.1.6232.8.1.3.1.0', str(mystring), 's')
        elif device_type == 'bpl' and action_type == 'upgrade':
            mystring = ftpType + ' ' + ftpAddr + ' ' + ftpPort + ' ' + ftpUser + ' ' + ftpPass + ' ' + 'null {\"CMD\":[{\"TSK\":{\"ID\":' + task_id +',\"TGT\":[{\"DEV_ID\":\"' + mac + '\"}],\"ACT\":{\"NAME\":\"UPGRADE\",\"PRIO\":100,\"EXP\":\"2100-12-24T18:53:44+00:00\",\"SET\":{\"ID\":\"' + filename + '\",\"SZ\":' + filesize +',\"SIG\":\"' + filemd5+ '\",\"DST\":1,\"EDT\":\"2016-06-24T16:53:44+00:00\",\"CM\":0}}}}]}'
            if self.session.set('1.3.6.1.4.1.6232.8.1.3.1.0', str(mystring), 's'):
                return mystring
            else:
                return "SNMPSET FAILURE!"
            #return self.session.set('1.3.6.1.4.1.6232.8.1.3.1.0', str(mystring), 's')
        elif device_type == 'proxy' and action_type == 'activate':
            mystring = ftpType + ' ' + ftpAddr + ' ' + ftpPort + ' ' + ftpUser + ' ' + ftpPass + ' ' + 'null {\"CMD\":[{\"TSK\":{\"ID\":' + task_id + ',\"TGT\":[],\"ACT\":{\"NAME\":\"ACTIVATE\",\"PRIO\":100,\"EXP\":\"2100-12-24T18:53:44+00:00\",\"SET\":{\"ID\":\"' + filename + '\",\"SZ\":' + filesize + ',\"SIG\":\"' + filemd5 + '\",\"DST\":0,\"EDT\":\"2016-06-24T16:53:44+00:00\",\"CM\":0}}}}]}'
            if self.session.set('1.3.6.1.4.1.6232.8.1.3.1.0', str(mystring), 's'):
                return mystring
            else:
                return "SNMPSET FAILURE!"
            #return self.session.set('1.3.6.1.4.1.6232.8.1.3.1.0', str(mystring), 's')
        elif device_type == 'bpl' and action_type == 'activate':
            mystring = ftpType + ' ' + ftpAddr + ' ' + ftpPort + ' ' + ftpUser + ' ' + ftpPass + ' ' + 'null {\"CMD\":[{\"TSK\":{\"ID\":' + task_id + ',\"TGT\":[{\"DEV_ID\":\"' + mac + '\"}],\"ACT\":{\"NAME\":\"ACTIVATE\",\"PRIO\":100,\"EXP\":\"2100-12-24T18:53:44+00:00\",\"SET\":{\"ID\":\"' + filename + '\",\"SZ\":' + filesize + ',\"SIG\":\"' + filemd5 + '\",\"DST\":1,\"EDT\":\"2016-06-24T16:53:44+00:00\",\"CM\":0}}}}]}'
            if self.session.set('1.3.6.1.4.1.6232.8.1.3.1.0', str(mystring), 's'):
                return mystring
            else:
                return "SNMPSET FAILURE!"
            #return self.session.set('1.3.6.1.4.1.6232.8.1.3.1.0', str(mystring), 's')
        else:
            return 'Please select choose valid option (config/upgrade/activate)'

    def snmpget(self, oid):
        return str(self.session.get(oid))

    def snmpset(self, oid, value, settype):
        if settype == 'integer':
            return self.session.set(oid, value, 'i')
        elif settype == 'string':
            return self.session.set(oid, value, 's')
        else:
            return 'Please select correct set type (integer/string)'
