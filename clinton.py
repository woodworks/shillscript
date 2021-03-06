import sys, os
import smtplib
from email.mime.text import MIMEText
import email.utils
from email_server import CustomSMTPServer
import subprocess

class MonicaLewinsky:

    prompted = []
    lastCmd = ""

    def __init__(self):
        self.prompted = []

    def processCommand(self, cmd):
        if("teleprompter prompt" in cmd):
            self.prompted.append("")
            for x in range(19,len(cmd)):
                self.prompted[-1] += list(cmd)[x]
        if("hillary read from teleprompter" in cmd):
            print(self.prompted[0])
            self.prompted.remove(self.prompted[0])
        if("hillary repeat" in cmd and "hillary repeat" not in self.lastCmd):
            self.processCommand(self.lastCmd)
        if("**email " in cmd):
            message = ""
            for x in range(6,list(cmd).index("$")):
                message = message + list(cmd)[x]
            msg = MIMEText(message)
            msg['To'] = email.utils.formataddr(('Recipient', cmd[list(cmd).index("$")+2:list(cmd).index("#")-1] ))
            msg['From'] = email.utils.formataddr(('Author','shillary.clinton@secretaryofstate.gov'))
            msg['Subject'] = cmd[list(cmd).index("#")+2:len(list(cmd))]
            server = smtplib.SMTP('127.0.0.1',1025)
            server.set_debuglevel(True)
            try:
                server.sendmail('shillary.clinton@secretaryofstate.gov',[cmd[list(cmd).index("$")+2:list(cmd).index("#")-1]], msg.as_string())
            finally:
                server.quit()
        self.lastCmd = cmd

def main():
    print("[+] Welcome to the Clinton Campaign")
    print()
    print()
    filename = sys.argv[1]
    if(".benghazi" not in filename):
        print("Filenames must end in .benghazi")
        exit()
    f=open(filename,'r')
    MadameSecretary = MonicaLewinsky()
    lineNum = 0
    for line in f.readlines():
        if(lineNum == 0):
            if("I will make history as the first female president" not in line):
                print("You forgot to declare yourself")
                exit()
        else:
            MadameSecretary.processCommand(line)
        lineNum = lineNum + 1
    f.close()
    f=open(filename, 'w')
    f.write('')
    f.close()
    print("[+] Finished running. Accidentally deleted everything.")
    print()
    print("Sorry folks, I\'ve got to split and rig a primary. I\'m hip! Vote for me kids.")

if __name__ == "__main__":
    main()