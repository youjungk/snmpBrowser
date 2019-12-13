
#    def config_upgrade_activate(self, device_type, action_type, filename, filesize, filemd5, ftpAddr, ftpType, ftpUser, ftpPass, ftpPort, mac):


class SnmpParam:

    def __init__(self, deviceType, actionType, fileName, fileSize, fileMd5, ftpAddr, ftpType, ftpUser, ftpPass, ftpPort, mac_addr):
        self.device_type = deviceType
        self.action_type = actionType
        self.file_name = fileName
        self.file_size = fileSize
        self.file_md5 = fileMd5
        self.ftp_addr = ftpAddr
        self.ftp_user = ftpUser
        self.ftp_type = ftpType
        self.ftp_pass = ftpPass
        self.ftp_port = ftpPort
        self.mac = mac_addr

    def set_params(self, deviceType, actionType, fileName, fileSize, fileMd5, ftpAddr, ftpType, ftpUser, ftpPass, ftpPort, mac_addr):
        self.device_type = deviceType
        self.action_type = actionType
        self.file_name = fileName
        self.file_size = fileSize
        self.file_md5 = fileMd5
        self.ftp_addr = ftpAddr
        self.ftp_user = ftpUser
        self.ftp_type = ftpType
        self.ftp_pass = ftpPass
        self.ftp_port = ftpPort
        self.mac = mac_addr

    def print_params(self):
        print(self.device_type + ", " + self.action_type + ", " + self.file_name + ", " + self.file_size + ", " + self.file_md5 + ", " + self.ftp_addr + ", " + self.ftp_type + ", " + self.ftp_user + ", " + self.ftp_pass + ", " + self.ftp_port + ", " + self.mac)


    def param_is_empty(self):
        if self.device_type == '' or self.action_type == '' or self.file_name=='' or self.file_size=='' or self.file_md5=='' or self.ftp_addr=='' or self.ftp_user=='' or self.ftp_type=='' or self.ftp_pass=='' or self.ftp_port =='' or self.ftp_port =='':
            return True
        else:
            return False
