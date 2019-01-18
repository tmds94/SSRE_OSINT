import os


print("SSRE 2018/19 OSINT v1.1 for Unix Systems only\n")

print ("Installing the necessary software... \n")

os.system("which python3.7")

os.system("sudo apt-get install python3.7")
os.system("curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py")
os.system("python3.7 get-pip.py")
os.system("apt-get install wkhtmltopdf")
os.system("pip install imgkit")
os.system("pip install pdfkit")

print ("\nSoftware installed with success! You can now run SSRE_OSINT!\n" )