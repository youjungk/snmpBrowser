#!/usr/bin/env python3.5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
import sys
import snmpparam
import snmpoperations


class SnmpApp(QMainWindow):
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        QMainWindow.__init__(self)
        self.setMinimumSize(QSize(800, 800))
        self.setWindowTitle("SNMP Tools")
        self.main_label_1 = QLabel('MENU', self)
        self.main_label_1.resize(50,50)
        self.main_label_1.move(30,0)
        self.main_label_2 = QLabel('OUTPUT', self)
        self.main_label_2.resize(60,50)
        self.main_label_2.move(260,0)
        self.main_label_3 = QLabel("SNMPGET ACTIONS", self)
        self.main_label_3.resize(150, 50)
        self.main_label_3.move(260, 300)
        self.main_label_4 = QLabel("OID", self)
        self.main_label_4.resize(50,50)
        self.main_label_4.move(260, 550)

        self.main_button_1 = QPushButton('Configuration', self)
        self.main_button_1.resize(200, 130)
        self.main_button_1.move(30, 50)
        self.main_button_2 = QPushButton('Upgrade', self)
        self.main_button_2.resize(200, 130)
        self.main_button_2.move(30, 200)
        self.main_button_3 = QPushButton('Topology Tree retrieval', self)
        self.main_button_3.resize(200, 130)
        self.main_button_3.move(30, 350)
        self.main_button_4 = QPushButton('Topology Profile retrieval', self)
        self.main_button_4.resize(200, 130)
        self.main_button_4.move(30, 500)
        self.main_button_5 = QPushButton('Set Actions', self)
        self.main_button_5.resize(200, 130)
        self.main_button_5.move(30, 650)
        self.main_button_6 = QPushButton('FULL SEND', self)
        self.main_button_6.resize(150, 30)
        self.main_button_6.move(260, 660)
        self.main_button_1.clicked.connect(self.getACfile)

        self.main_outputbox_1 = QTextEdit(self)
        self.main_outputbox_1.move (260,50)
        self.main_outputbox_1.resize(510, 250)

        self.main_selectable_list = QListWidget(self)
        self.main_selectable_list.move(260, 350)
        self.main_selectable_list.resize(510, 200)
        self.main_selectable_list.addItem("Quality Profile Retrieval")
        self.main_selectable_list.addItem("Logging Profile Retrieval")
        self.main_selectable_list.addItem("SSH Key Retrieval")
        self.main_selectable_list.addItem("")
        self.main_selectable_list.itemDoubleClicked.connect(self.itemclicked)

        self.main_lineedit = QLineEdit(self)
        self.main_lineedit.move(260, 600)
        self.main_lineedit.resize(510, 50)
        self.main_lineedit.textChanged.connect(self.oidtextchanged)

        # CLICK ACTIONS
        self.main_button_2.clicked.connect(self.getACfile)
        self.main_button_3.clicked.connect(self.topologytreebuttonclicked)
        self.main_button_4.clicked.connect(self.topologyprofilebuttonclicked)
        self.main_button_5.clicked.connect(self.setbuttonclicked)
        self.main_button_6.clicked.connect(self.getbuttonclicked)

        self.oid = ''

        # temporary variables
        self.deviceType=''
        self.actionType=''
        self.filename = ''
        self.filesize = ''
        self.filemd5 = ''
        self.ftpAddr = ''
        self.ftpType = ''
        self.ftpUser = ''
        self.ftpPass = ''
        self.ftpPort = ''
        self.mac = ''

        # SNMPSET ACTIONS
        self.oid = ''
        self.setType= ''
        self.setStringorInt =''

        self.SNMPParam = snmpparam.SnmpParam(self.deviceType, self.actionType, self.filename, self.filesize, self.filemd5, self.ftpAddr, self.ftpType, self.ftpUser, self.ftpPass, self.ftpPort, self.mac, self.oid, self.setType, self.setStringorInt)
        self.SNMPOperation = snmpoperations.SnmpOperations('10.10.100.1')

    # for item list
    def itemclicked(self, item):
        if "Quality" in item.text():
            self.main_outputbox_1.setText(self.SNMPOperation.snmpget("1.3.6.1.4.1.6232.8.1.3.5.0"))
            QMessageBox.information(self, "SNMPGet", item.text())
        elif "Logging" in item.text():
            self.main_outputbox_1.setText(self.SNMPOperation.snmpget("1.3.6.1.4.1.6232.8.1.3.6.0"))
            QMessageBox.information(self, "SNMPGet", item.text())
        elif "SSH" in item.text():
            self.main_outputbox_1.setText(self.SNMPOperation.snmpget("1.3.6.1.4.1.6232.8.1.3.8.0"))
            QMessageBox.information(self, "SNMPGet", item.text())
        else:
            QMessageBox.information(self, "SNMPGet", "Invalid Options")

    def topologytreebuttonclicked(self):
        self.main_outputbox_1.setText(self.SNMPOperation.snmpget("1.3.6.1.4.1.6232.8.1.1.1.0"))

    def topologyprofilebuttonclicked(self):
        self.main_outputbox_1.setText(self.SNMPOperation.snmpget("1.3.6.1.4.1.6232.8.1.3.4.0"))

    def getbuttonclicked(self):
        print(self.main_lineedit.text())
        self.main_outputbox_1.setText(self.SNMPOperation.snmpget(self.main_lineedit.text()))

    def setbuttonclicked(self):
        e = QDialog(self)
        # OID
        oid = QLineEdit("Enter oid", e)
        oid.move(0,0)
        oid.resize(200, 30)
        oid.selectAll()
        oid.textChanged.connect(self.textChanged_oid)

        # SET Type
        setType = QLineEdit("Enter set type (string/int): ", e)
        setType.move(0, 40)
        setType.resize(200, 30)
        setType.selectAll()
        setType.textChanged.connect(self.textChanged_setType)

        # SET Value
        setValue = QLineEdit("Enter set value: ", e)
        setValue.move(0, 80)
        setValue.resize(200, 30)
        setValue.selectAll()
        setValue.textChanged.connect(self.textChanged_setStringorInt)

        e.setMinimumSize(QSize(200, 150))
        e.setWindowTitle('OID')

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, e)
        buttons.move(30, 120)
        buttons.accepted.connect(e.accept)
        buttons.rejected.connect(e.reject)

        result = e.exec()

        if result == True:
            self.SNMPParam.oid = self.oid
            self.SNMPParam.set_type = self.setType
            self.SNMPParam.set_value = self.setStringorInt
            self.SNMPOperation.snmpset(self.SNMPParam.oid, self.SNMPParam.set_type, self.SNMPParam.set_value)


    def getACfile (self):
        d = QDialog(self)
        # DEVICE TYPE
        if self.SNMPParam.device_type == '':
            device_type = QLineEdit("Enter device type (Proxy/BPL)", d)
        else:
            device_type = QLineEdit(self.SNMPParam.device_type, d)
        device_type.move(0,0)
        device_type.resize(350, 25)
        device_type.selectAll()
        device_type.textChanged.connect(self.textChanged_deviceType)

        # ACTION TYPE
        if self.SNMPParam.action_type == '':
            action_type = QLineEdit("Enter action type (config/upgrade)", d)
        else:
            action_type = QLineEdit(self.SNMPParam.action_type, d)
        action_type.move(0, 50)
        action_type.resize(350, 25)
        action_type.selectAll()
        action_type.textChanged.connect(self.textChanged_actionType)

        # FILE NAME
        if self.SNMPParam.file_name == '':
            filename = QLineEdit("Enter file name", d)
        else:
            filename = QLineEdit(self.SNMPParam.file_name, d)
        filename.move(0, 100)
        filename.resize(350, 25)
        filename.selectAll()
        filename.textChanged.connect(self.textChanged_filename)

        # FILE SIZE
        if self.SNMPParam.file_size == '':
            filesize = QLineEdit("Enter file size", d)
        else:
            filesize = QLineEdit(self.SNMPParam.file_size, d)
        filesize.move(0, 150)
        filesize.resize(350, 25)
        filesize.selectAll()
        filesize.textChanged.connect(self.textChanged_filesize)

        # FILEMD5
        if self.SNMPParam.file_md5 == '':
            filemd5 = QLineEdit("Enter file md5", d)
        else:
            filemd5 = QLineEdit(self.SNMPParam.file_md5, d)
        filemd5.move(0, 200)
        filemd5.resize(350, 25)
        filemd5.selectAll()
        filemd5.textChanged.connect(self.textChanged_filemd5)

        # FTPADDR
        if self.SNMPParam.ftp_addr == '':
            ftpaddr = QLineEdit("Enter ftp address", d)
        else:
            ftpaddr = QLineEdit(self.SNMPParam.ftp_addr, d)
        ftpaddr.move(0, 250)
        ftpaddr.resize(350, 25)
        ftpaddr.selectAll()
        ftpaddr.textChanged.connect(self.textChanged_ftpAddr)

        #FTPTYPE
        if self.SNMPParam.ftp_type=='':
            ftpType = QLineEdit("Enter ftp type", d)
        else:
            ftpType = QLineEdit(self.SNMPParam.ftp_type, d)
        ftpType.move(0, 300)
        ftpType.resize(350, 25)
        ftpType.selectAll()
        ftpType.textChanged.connect(self.textChanged_ftpType)

        # FTPUSER
        if self.SNMPParam.ftp_user == '':
            ftpUser = QLineEdit("Enter ftp user", d)
        else:
            ftpUser = QLineEdit(self.SNMPParam.ftp_user, d)
        ftpUser.move(0, 350)
        ftpUser.resize(350, 25)
        ftpUser.selectAll()
        ftpUser.textChanged.connect(self.textChanged_ftpUser)

        # FTPPASS
        if self.SNMPParam.ftp_pass == '':
            ftpPass = QLineEdit("Enter ftp pass", d)
        else:
            ftpPass = QLineEdit(self.SNMPParam.ftp_pass, d)
        ftpPass.move(0, 400)
        ftpPass.resize(350, 25)
        ftpPass.selectAll()
        ftpPass.textChanged.connect(self.textChanged_ftpPass)

        # FTPPORT
        if self.SNMPParam.ftp_port == '':
            ftpPort = QLineEdit("Enter ftp port", d)
        else:
            ftpPort = QLineEdit(self.SNMPParam.ftp_port, d)
        ftpPort.move(0, 450)
        ftpPort.resize(350, 25)
        ftpPort.selectAll()
        ftpPort.textChanged.connect(self.textChanged_ftpPort)

        # MAC
        if self.SNMPParam.mac == '':
            mac = QLineEdit("Enter mac", d)
        else:
            mac = QLineEdit(self.SNMPParam.mac, d)
        mac.move(0, 500)
        mac.resize(350, 25)
        mac.selectAll()
        mac.textChanged.connect(self.textChanged_mac)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, d)
        buttons.move(175, 550)
        buttons.accepted.connect(d.accept)
        buttons.rejected.connect(d.reject)
        #d.label.setText(d.dialog.comboBox.currentText())

        d.setMinimumSize(QSize(350, 550))
        d.setWindowTitle('AC file')

        result = d.exec()

        if result == True:
            #print("b: " + b)
            self.SNMPParam.set_params(self.deviceType, self.actionType, self.filename, self.filesize, self.filemd5, self.ftpAddr, self.ftpType, self.ftpUser, self.ftpPass, self.ftpPort, self.mac, self.oid, self.setType, self.setStringorInt)
            self.SNMPParam.print_params()
            self.sendConfUpgJob()
            print("OK")

        return result == QDialog.Accepted

    def sendConfUpgJob(self):
        #def config_upgrade_activate(self, device_type, action_type, filename, filesize, filemd5, ftpAddr, ftpType, ftpUser, ftpPass, ftpPort, mac):
        if self.SNMPParam.param_is_empty() == False:
            self.main_outputbox_1.setText(self.SNMPOperation.config_upgrade_activate(self.SNMPParam.device_type, self.SNMPParam.action_type, self.SNMPParam.file_name, self.SNMPParam.file_size, self.SNMPParam.file_md5, self.SNMPParam.ftp_addr, self.SNMPParam.ftp_type, self.SNMPParam.ftp_user, self.SNMPParam.ftp_pass, self.SNMPParam.ftp_port, self.SNMPParam.mac))
        else:
            msg = QMessageBox()
            msg.setWindowTitle("SNMP Parameters missing")
            msg.setText("Make sure every parameter is filled in!")
            x = msg.exec()

        print('fullsend')

    def onclick(self):
        self.main_outputbox_1.setText("button\nbutton\nbutton")

    def oidtextchanged(self, text):
        self.oid = text

    def textChanged_deviceType(self, text):
        self.deviceType=text

    def textChanged_actionType(self, text):
        self.actionType=text

    def textChanged_filename(self, text):
        self.filename=text

    def textChanged_filesize(self, text):
        self.filesize=text

    def textChanged_filemd5(self, text):
        self.filemd5=text

    def textChanged_ftpAddr(self, text):
        self.ftpAddr=text

    def textChanged_ftpType(self, text):
        self.ftpType=text

    def textChanged_ftpUser(self, text):
        self.ftpUser=text

    def textChanged_ftpPass(self, text):
        self.ftpPass=text

    def textChanged_ftpPort(self, text):
        self.ftpPort=text

    def textChanged_mac(self, text):
        self.mac=text

    def textChanged_oid(self, text):
        self.mac=text

    def textChanged_setType(self, text):
        self.setType = text

    def textChanged_setStringorInt(self, text):
        self.setStringorInt = text

    def appexec(self):
        self.app.exec_()


test = SnmpApp()
#test.create_main_menu()
test.show()
sys.exit(test.appexec())
