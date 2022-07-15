import subprocess
import sys
from flask import Flask, render_template, request, redirect, url_for
import os
import sqlite3
from werkzeug.utils import secure_filename
danhsach = []
domainName = []
danhsachGroup = []
danhsachUser = []
danhsachUserInOu = []
output = subprocess.run('dsquery ou', stdout=subprocess.PIPE, shell=True)
danhsach.append(output.stdout.decode('UTF-8'))
outputgroup = subprocess.run('dsquery group', stdout=subprocess.PIPE, shell=True)
danhsachGroup.append(outputgroup.stdout.decode('UTF-8'))
outputUser = subprocess.run('dsquery user', stdout=subprocess.PIPE, shell=True)
danhsachUser.append(outputUser.stdout.decode('UTF-8'))
folderShare = []


def tach(tach):
    name = tach.split('\r\n')
    nameOu = name.remove('')
    return name


def tachName(name):
    name = name.split('=')
    return name


 # Database
print("Table created successfully")
with sqlite3.connect("database.db") as con:
    con.execute('CREATE TABLE IF NOT EXISTS ouTable (ouname TEXT)')
    for x in danhsach:
        for y in tach(x):
            cur = con.cursor()
            values = tachName(y)[1].split(',')[0]
            cur.execute('INSERT INTO ouTable VALUES (?)', [values])
            con.commit()

    con.execute('CREATE TABLE IF NOT EXISTS groupTable (groupname TEXT)')
    for x in danhsachGroup:
        for y in tach(x):
            cur = con.cursor()
            values = tachName(y)[1].split(',')[0]
            cur.execute('INSERT INTO groupTable VALUES (?)', [values])
            con.commit()
    
    con.execute('CREATE TABLE IF NOT EXISTS userTable (userName TEXT)')
    for x in danhsachUser:
        for y in tach(x):
            cur = con.cursor()
            values = tachName(y)[1].split(',')[0]
            cur.execute('INSERT INTO userTable VALUES (?)', [values])
            con.commit()


def tachDomain(name):
    name = name.split('.')
    return name


 # OU
def addOu(nameOU):
    for x in domainName:
        addOu = "dsadd ou " + chr(34) + "ou="+nameOU+",dc=" +tachDomain(x)[0]+",dc=" +tachDomain(x)[1]+chr(34)
        print(addOu)
        os.system(addOu)
        createFolder(nameOU)
def deleteOU(nameOU):
    for x in domainName:
        delOU = "dsrm "+chr(34)+"ou="+nameOU+",dc="+tachDomain(x)[0]+",dc="+tachDomain(x)[1]+chr(34)+" -noprompt -subtree"
        print(delOU)
        os.system(delOU)


 #Group
def addGroup(nameGroup,nameOu):
    for x in domainName:
        addgroup = "dsadd group "+ chr(34) +"cn="+nameGroup+",ou="+nameOu+",dc="+tachDomain(x)[0]+",dc="+tachDomain(x)[1]+chr(34)
        print(addgroup)
    os.system(addgroup)
def addGroupscope(nameGroup,nameOu,scope):  
    if scope == 'l':
        for x in domainName:
            addgroup = "dsadd group "+ chr(34) +"cn="+nameGroup+",ou="+nameOu+",dc="+tachDomain(x)[0]+",dc="+tachDomain(x)[1]+chr(34)+" -scope "+scope
            print(addgroup)
    elif scope == 'g':
        for x in domainName:
            addgroup = "dsadd group "+ chr(34) +"cn="+nameGroup+",ou="+nameOu+",dc="+tachDomain(x)[0]+",dc="+tachDomain(x)[1]+chr(34)+" -scope "+scope
            print(addgroup)
    elif scope == 'u':
        for x in domainName:
            addgroup = "dsadd group "+ chr(34) +"cn="+nameGroup+",ou="+nameOu+",dc="+tachDomain(x)[0]+",dc="+tachDomain(x)[1]+chr(34)+" -scope "+scope
            print(addgroup)
    os.system(addgroup)

def deleteGroup(nameGroup,nameOu):
    for x in domainName:
        deleteGroup= "dsrm "+chr(34)+"cn="+nameGroup+",ou="+nameOu+",dc="+tachDomain(x)[0]+",dc="+tachDomain(x)[1]+chr(34)+" ﻿import subprocess
import sys
from flask import Flask, render_template, request, redirect, url_for
import os
import sqlite3
from werkzeug.utils import secure_filename
danhsach = []
domainName = []
danhsachGroup = []
danhsachUser = []
danhsachUserInOu = []
output = subprocess.run('dsquery ou', stdout=subprocess.PIPE, shell=True)
danhsach.append(output.stdout.decode('UTF-8'))
outputgroup = subprocess.run('dsquery group', stdout=subprocess.PIPE, shell=True)
danhsachGroup.append(outputgroup.stdout.decode('UTF-8'))
outputUser = subprocess.run('dsquery user', stdout=subprocess.PIPE, shell=True)
danhsachUser.append(outputUser.stdout.decode('UTF-8'))
folderShare = []


def tach(tach):
    name = tach.split('\r\n')
    nameOu = name.remove('')
    return name


def tachName(name):
    name = name.split('=')
    return name


 # Database
print("Table created successfully")
with sqlite3.connect("database.db") as con:
    con.execute('CREATE TABLE IF NOT EXISTS ouTable (ouname TEXT)')
    for x in danhsach:
        for y in tach(x):
            cur = con.cursor()
            values = tachName(y)[1].split(',')[0]
            cur.execute('INSERT INTO ouTable VALUES (?)', [values])
            con.commit()

    con.execute('CREATE TABLE IF NOT EXISTS groupTable (groupname TEXT)')
    for x in danhsachGroup:
        for y in tach(x):
            cur = con.cursor()
            values = tachName(y)[1].split(',')[0]
            cur.execute('INSERT INTO groupTable VALUES (?)', [values])
            con.commit()
    
    con.execute('CREATE TABLE IF NOT EXISTS userTable (userName TEXT)')
    for x in danhsachUser:
        for y in tach(x):
            cur = con.cursor()
            values = tachName(y)[1].split(',')[0]
            cur.execute('INSERT INTO userTable VALUES (?)', [values])
            con.commit()


def tachDomain(name):
    name = name.split('.')
    return name


 # OU
def addOu(nameOU):
    for x in domainName:
        addOu = "dsadd ou " + chr(34) + "ou="+nameOU+",dc=" +tachDomain(x)[0]+",dc=" +tachDomain(x)[1]+chr(34)
        print(addOu)
        os.system(addOu)
        createFolder(nameOU)
def deleteOU(nameOU):
    for x in domainName:
        delOU = "dsrm "+chr(34)+"ou="+nameOU+",dc="+tachDomain(x)[0]+",dc="+tachDomain(x)[1]+chr(34)+" -noprompt -subtree"
        print(delOU)
        os.system(delOU)


 #Group
def addGroup(nameGroup,nameOu):
    for x in domainName:
        addgroup = "dsadd group "+ chr(34) +"cn="+nameGroup+",ou="+nameOu+",dc="+tachDomain(x)[0]+",dc="+tachDomain(x)[1]+chr(34)
        print(addgroup)
    os.system(addgroup)
def addGroupscope(nameGroup,nameOu,scope):  
    if scope == 'l':
        for x in domainName:
            addgroup = "dsadd group "+ chr(34) +"cn="+nameGroup+",ou="+nameOu+",dc="+tachDomain(x)[0]+",dc="+tachDomain(x)[1]+chr(34)+" -scope "+scope
            print(addgroup)
    elif scope == 'g':
        for x in domainName:
            addgroup = "dsadd group "+ chr(34) +"cn="+nameGroup+",ou="+nameOu+",dc="+tachDomain(x)[0]+",dc="+tachDomain(x)[1]+chr(34)+" -scope "+scope
            print(addgroup)
    elif scope == 'u':
        for x in domainName:
            addgroup = "dsadd group "+ chr(34) +"cn="+nameGroup+",ou="+nameOu+",dc="+tachDomain(x)[0]+",dc="+tachDomain(x)[1]+chr(34)+" -scope "+scope
            print(addgroup)
    os.system(addgroup)

def deleteGroup(nameGroup,nameOu):
    for x in domainName:
        deleteGroup= "dsrm "+chr(34)+"cn="+nameGroup+",ou="+nameOu+",dc="+tachDomain(x)[0]+",dc="+tachDomain(x)[1]+chr(34)+" -noprompt -subtree"
        print(deleteGroup)
    os.system(deleteGroup)


 #Folder
def createFolder(nameOu):
    create = "cd C:\\ & mkdir "+nameOu
    os.system(create)
    share = "net share "+nameOu+"=C:\\"+nameOu
    print(share)
    os.system(share)
            
 #User
def addUser(nameUser,nameGroup,nameOu,passwd,active):
    if active == 'yes':
            for x in domainName:
                add = "dsadd user "+ chr(34) +"cn="+nameUser+",dc="+tachDomain(x)[0]+",dc="+tachDomain(x)[1]+chr(34)+" -pwd "+passwd+" -disabled yes -memberof "+chr(34)+"cn="+nameGroup+",ou="+nameOu+",dc="+tachDomain(x)[0]+",dc="+tachDomain(x)[1]
                print(add)
    elif active == 'no':
        for x in domainName:
            add = "dsadd user "+ chr(34) +"cn="+nameUser+",dc="+tachDomain(x)[0]+",dc="+tachDomain(x)[1]+chr(34)+" -pwd "+passwd+" -disabled no -memberof "+chr(34)+"cn="+nameGroup+",ou="+nameOu+",dc="+tachDomain(x)[0]+",dc="+tachDomain(x)[1]
            print(add)
    os.system(add)
    createFolder = "cd C:\\"+nameOu+" & mkdir "+nameUser+chr(34)
    per = "icacls "+chr(34)+"C:\\"+nameOu+"\\"+nameUser+chr(34)+" /grant "+nameUser+":F /T"
    per1 = "icacls C:\\"+nameOu+"\\"+nameUser+" /inheritance:r"
    per2 = "icacls C:\\"+nameOu+"\\"+nameUser+" /grant Administrators:(OI)(CI)F /T"
    try:
        os.system(createFolder)
        os.system(per)
        os.system(per1)
        os.system(per2)
    except:
        pass

def addUserOu(nameUser,nameOu,passwd):
    for x in domainName:
        add = "dsadd user "+ chr(34) +"cn="+nameUser+",ou="+nameOu+",dc="+tachDomain(x)[0]+",dc="+tachDomain(x)[1]+chr(34)+" -pwd "+passwd+" -disabled no"
    os.system(add)
    createFolder = "cd C:\\"+nameOu+" & mkdir "+nameUser+chr(34)
    per = "icacls "+chr(34)+"C:\\"+nameOu+"\\"+nameUser+chr(34)+" /grant "+nameUser+":F /T"
    per1 = "icacls C:\\"+nameOu+"\\"+nameUser+" /inheritance:r"
    per2 = "icacls C:\\"+nameOu+"\\"+nameUser+" /grant Administrators:(OI)(CI)F /T"
    try:
        os.system(createFolder)
        os.system(per)
        os.system(per1)
        os.system(per2)
    except:
        pass

def deleteUser(nameUser):
    for x in domainName:
        delete = "dsrm -noprompt "+ chr(34)+"cn="+nameUser+",dc="+tachDomain(x)[0]+",dc="+tachDomain(x)[1]+chr(34)
        print(delete)
    os.system(delete)
 #Flask



def changeOu(ouOld,ouNew,user):
    for x in domainName:
        changeOu = "dsmove "+ chr(34)+"cn="+user+",ou="+ouOld+",dc="+tachDomain(x)[0]+",dc="+tachDomain(x)[1]+chr(34)+ " -newparent ou="+ouNew+",dc="+tachDomain(x)[0]+",dc="+tachDomain(x)[1]
        print(changeOu)
        os.system(changeOu)
    
app = Flask(__name__)
app.add_url_rule('/photos/<path:filename>', endpoint='photos', view_func=app.send_static_file)
app.config["DEBUG"] = True

@app.route('/login', methods=['POST'])
def login():
    domain = request.form['domainName']
    ip = request.form['ip']
    domainName.append(domain)
    folderShare.append(ip)
    print(folderShare)
    print(domainName)
    return render_template('index.html')


@app.route('/index.html', methods=['GET', 'POST'])
def show_index():
    return render_template('index.html')


@app.route('/', methods=['GET'])
def show_login():
    return render_template('login.html')


@app.route('/qlou.html', methods=['GET'])
def show_qlou():
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from ouTable")
    rows = []
    for row in cur:
        if row not in rows:
            rows.append(row)
    cur.execute("select * from groupTable")
    rowsGroup = []
    for rowG in cur:
        if rowG not in rowsGroup:
            rowsGroup.append(rowG)
    cur.execute("select * from userTable")
    rowsUser = []
    for rowG in cur:
        if rowG not in rowsUser:
            rowsUser.append(rowG)
    return render_template('qlou.html', ou=rows,group=rowsGroup,user=rowsUser)


@app.route('/share.html', methods=['GET'])
def share():
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from ouTable")
    rows = []
    for row in cur:
        if row not in rows:
            rows.append(row)
    cur.execute("select * from userTable")
    rowsUser = []
    for rowG in cur:
        if rowG not in rowsUser:
            rowsUser.append(rowG)
    return render_template('share.html', ou=rows,user=rowsUser)


@app.route('/install.html', methods=['GET'])
def install():
    return render_template('install.html')

@app.route('/share', methods=['POST'])
def upload_file():
    if 'shareOnly' in request.form:
        fullPath = request.files.getlist('file')
        nameOu = request.form['opOuname']
        nameUser = request.form['opUser']
        for files in fullPath:
            files.save(os.path.join("C:\\"+nameOu+"\\"+nameUser, files.filename))
    elif 'shareAll' in request.form:
        fullPath = request.files.getlist('file')
        nameOu = request.form['opOuname']
        for x in domainName:
            output = subprocess.run("dsquery user "+chr(34)+"ou="+nameOu+",dc="+tachDomain(x)[0]+",dc="+tachDomain(x)[1]+chr(34), stdout=subprocess.PIPE, shell=True)
            danhsachUserInOu.append(output.stdout.decode('UTF-8'))
        for x in danhsachUserInOu:
            for y in tach(x):
                for files in fullPath:
                    userName = tachName(y)[1].split(',')[0]
                    files.save(os.path.join("C:\\"+nameOu+"\\"+userName, files.filename))
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from ouTable")
    rows = []
    for row in cur:
        if row not in rows:
            rows.append(row)
    cur.execute("select * from userTable")
    rowsUser = []
    for rowG in cur:
        if rowG not in rowsUser:
            rowsUser.append(rowG)
    return render_template('share.html', ou=rows,user=rowsUser)
       


 # PowerShell
@app.route('/IIS', methods=['GET','POST'])
def IIS():
    if request.method == 'POST':
        if 'IIS' in request.form:
            subprocess.run(["powershell", "C:\\Users\\Administrator\\Desktop\\Test\\install\\InstalllS.ps1"], shell=True)
            with open('C:\\Users\\Administrator\\Desktop\\Test\\install\\InstalllS.ps1', 'r') as f:
                while(True):
                    line = f.readline()
                    if r'''Write-Output("Installed Successfully")''' in line:
                        return r'''<script>alert('Cài đặt Thành công')</script>'''
    if request.method == 'GET':
        return render_template('install.html')
@app.route('/FTP', methods=['GET','POST'])
def FTP():
    if request.method == 'POST':
        if 'FTP' in request.form:
            subprocess.run(["powershell", "C:\\Users\\Administrator\\Desktop\\Test\\install\\InstallFTP.ps1"], shell=True)
            with open('C:\\Users\\Administrator\\Desktop\\Test\\install\\InstallFTP.ps1', 'r') as f:
                while(True):
                    line = f.readline()
                    if r'''Write-Output("Installed Successfully")''' in line:
                        return r'''<script>alert('Cài đặt Thành công')</script>'''
    if request.method == 'GET':
        return render_template('install.html')
@app.route('/Telnet', methods=['GET','POST'])
def Telnet():
    if request.method == 'POST':
        if 'Telnet' in request.form:
            subprocess.run(["powershell", "C:\\Users\\Administrator\\Desktop\\Test\\install\\InstallTelnet.ps1"], shell=True)
            with open('C:\\Users\\Administrator\\Desktop\\Test\\install\\InstallTelnet.ps1', 'r') as f:
                while(True):
                    line = f.readline()
                    if r'''Write-Output("Installed Successfully")''' in line:
                        return r'''<script>alert('Cài đặt Thành công')</script>'''
    if request.method == 'GET':
        return render_template('install.html')

@app.route('/add', methods=['POST'])
def ou():
    if 'addOu' in request.form:
        ouname = request.form['ouname'] 
        check = request.form.get('checkOu') 
        print(check)
        if check == 'Yes': 
            for x in domainName:
                text2 = r'''New-ADOrganizationalUnit -Name "'''+ouname+r'''" -Path "DC='''+tachDomain(x)[0]+r''',DC='''+tachDomain(x)[1]+r'''"'''
                with open('wirtePS.ps1', 'w') as f:
                    f.write(text2)
            subprocess.run(["powershell", "C:\\Users\\Administrator\\Desktop\\Test\\wirtePS.ps1"], shell=True)
            createFolder(ouname)
            with sqlite3.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO ouTable (ouname) VALUES (?)", [ouname])
                con.commit()
            cur.execute("select * from ouTable")
            rows = []
            for row in cur:
                if row not in rows:
                    rows.append(row)
            cur.execute("select * from groupTable")
            rowsGroup = []
            for rowG in cur:
                if rowG not in rowsGroup:
                    rowsGroup.append(rowG)
            cur.execute("select * from userTable")
            rowsUser = []
            for rowG in cur:
                if rowG not in rowsUser:
                    rowsUser.append(rowG)
            return render_template('qlou.html', ou=rows,group=rowsGroup,user=rowsUser)
        else:
            addOu(ouname)
            with sqlite3.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO ouTable (ouname) VALUES (?)", [ouname])
                con.commit()
            cur.execute("select * from ouTable")
            rows = []
            for row in cur:
                if row not in rows:
                    rows.append(row)
            cur.execute("select * from groupTable")
            rowsGroup = []
            for rowG in cur:
                if rowG not in rowsGroup:
                    rowsGroup.append(rowG)
            cur.execute("select * from userTable")
            rowsUser = []
            for rowG in cur:
                if rowG not in rowsUser:
                    rowsUser.append(rowG)
            return render_template('qlou.html', ou=rows,group=rowsGroup,user=rowsUser)
        return render_template('qlou.html')
    elif 'deleteOu' in request.form:
        ouname = request.form['opOuname']
        with sqlite3.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("DELETE from ouTable where ouname=?", [ouname])
            con.commit()
        deleteOU(ouname)
        cur.execute("select * from ouTable")
        rows = []
        for row in cur:
            if row not in rows:
                rows.append(row)
        cur.execute("select * from groupTable")
        rowsGroup = []
        for rowG in cur:
            if rowG not in rowsGroup:
                rowsGroup.append(rowG)
        cur.execute("select * from userTable")
        rowsUser = []
        for rowG in cur:
            if rowG not in rowsUser:
                rowsUser.append(rowG)
        return render_template('qlou.html', ou=rows,group=rowsGroup,user=rowsUser)
    elif 'addGroup' in request.form:
        groupName = request.form['groupname']
        ouname = request.form['opOuname']
        scope = request.form.get('option')
        if scope == 'l' or scope == 'g' or scope == 'u':
            addGroupscope(groupName,ouname,scope)
            with sqlite3.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO groupTable (groupName) VALUES (?)", [groupName])
                con.commit()
            cur.execute("select * from groupTable")
            rowsGroup = []
            for row in cur:
                if row not in rowsGroup:
                    rowsGroup.append(row)
            cur.execute("select * from ouTable")
            rows = []
            for rowG in cur:
                if rowG not in rows:
                    rows.append(rowG)
            cur.execute("select * from userTable")
            rowsUser = []
            for rowG in cur:
                if rowG not in rowsUser:
                    rowsUser.append(rowG)
            return render_template('qlou.html', ou=rows,group=rowsGroup,user=rowsUser)
        else:
            addGroup(groupName,ouname)
            with sqlite3.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO groupTable (groupName) VALUES (?)", [groupName])
                con.commit()
            cur.execute("select * from groupTable")
            rowsGroup = []
            for row in cur:
                if row not in rowsGroup:
                    rowsGroup.append(row)
            cur.execute("select * from ouTable")
            rows = []
            for rowG in cur:
                if rowG not in rows:
                    rows.append(rowG)
            cur.execute("select * from userTable")
            rowsUser = []
            for rowG in cur:
                if rowG not in rowsUser:
                    rowsUser.append(rowG)
            return render_template('qlou.html', ou=rows,group=rowsGroup,user=rowsUser)
    elif 'deleteGroup' in request.form:
        groupName = request.form['opGroup']
        ouname = request.form['opOuname']
        with sqlite3.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("DELETE from groupTable where groupName=?", [groupName])
            con.commit()
        deleteGroup(groupName,ouname)
        cur.execute("select * from groupTable")
        rowsGroup = []
        for row in cur:
            if row not in rowsGroup:
                rowsGroup.append(row)
        cur.execute("select * from ouTable")
        rows = []
        for rowG in cur:
            if rowG not in rows:
                rows.append(rowG)
        cur.execute("select * from userTable")
        rowsUser = []
        for rowG in cur:
            if rowG not in rowsUser:
                rowsUser.append(rowG)
        return render_template('qlou.html', ou=rows,group=rowsGroup,user=rowsUser)
    elif 'addUser' in request.form:
        groupName = request.form['opGroup']
        ouname = request.form['opOuname']
        userName = request.form['username']
        passwd = request.form['password']
        active = request.form['disabledAccount']
        if groupName != 'Chọn Group':
            addUser(userName,groupName,ouname,passwd,active)
            with sqlite3.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO userTable (userName) VALUES (?)", [userName])
                con.commit()
            cur.execute("select * from userTable")
            rowsUser = []
            for row in cur:
                if row not in rowsUser:
                    rowsUser.append(row)
            cur.execute("select * from ouTable")
            rows = []
            for rowG in cur:
                if rowG not in rows:
                    rows.append(rowG)
            cur.execute("select * from groupTable")
            rowsGroup = []
            for rowG in cur:
                if rowG not in rowsGroup:
                    rowsGroup.append(rowG)
            return render_template('qlou.html', ou=rows,group=rowsGroup,user=rowsUser)
        elif groupName == 'Chọn Group':
            addUserOu(userName,ouname,passwd)
            with sqlite3.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO userTable (userName) VALUES (?)", [userName])
                con.commit()
            cur.execute("select * from userTable")
            rowsUser = []
            for row in cur:
                if row not in rowsUser:
                    rowsUser.append(row)
            cur.execute("select * from ouTable")
            rows = []
            for rowG in cur:
                if rowG not in rows:
                    rows.append(rowG)
            cur.execute("select * from groupTable")
            rowsGroup = []
            for rowG in cur:
                if rowG not in rowsGroup:
                    rowsGroup.append(rowG)
            return render_template('qlou.html', ou=rows,group=rowsGroup,user=rowsUser)

    elif 'deleteUser' in request.form:
        userName = request.form['opUser']
        with sqlite3.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("DELETE from userTable where userName=?", [userName])
            con.commit()
        deleteUser(userName)
        cur.execute("select * from userTable")
        rowsUser = []
        for row in cur:
            if row not in rowsUser:
                rowsUser.append(row)
        cur.execute("select * from ouTable")
        rows = []
        for rowG in cur:
            if rowG not in rows:
                rows.append(rowG)
        cur.execute("select * from groupTable")
        rowsGroup = []
        for rowG in cur:
            if rowG not in rowsGroup:
                rowsGroup.append(rowG)
        return render_template('qlou.html', ou=rows,group=rowsGroup,user=rowsUser)
    elif 'changeOu' in request.form:
        ouOld = request.form['opOuOld']
        ouNew = request.form['opOuNew']
        user = request.form['opUserChange']
        changeOu(ouOld,ouNew,user)
        con = sqlite3.connect("database.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("select * from ouTable")
        rows = []
        for row in cur:
            if row not in rows:
                rows.append(row)
        cur.execute("select * from groupTable")
        rowsGroup = []
        for rowG in cur:
            if rowG not in rowsGroup:
                rowsGroup.append(rowG)
        cur.execute("select * from userTable")
        rowsUser = []
        for rowG in cur:
            if rowG not in rowsUser:
                rowsUser.append(rowG)
        return render_template('qlou.html', ou=rows,group=rowsGroup,user=rowsUser)

 #check thang domain
@app.route('/check', methods=['POST'])
def check():
    if 'checkDomain' in request.form:
        os.system("systeminfo | findstr /B "+chr(34) +
                  "Domain" + chr(34)+"> check.txt")
        check = open("check.txt", "r")
        while(True):
            line = check.readline()
            if 'WORKGROUP' in line:
                return render_template('index.html', check = 'Máy của bạn chưa thăng domain')
            else:
                return render_template('index.html', check = 'Máy của bạn đã thăng domain')
    if "thangDomain" in request.form:
        text2 = r'''[DCInstall]
            New forest promotion
            ReplicaOrNewDomain=Domain
            NewDomain=Forest                    
            NewDomainDNSName=''' +domainName[0]+ r'''
            ForestLevel=3
            DomainNetbiosName=qtm
            DomainLevel=3
            InstallDNS=Yes
            ConfirmGc=Yes
            CreateDNSDelegation=No
            DatabasePath="C:\Windows\NTDS"
            LogPath="C:\Windows\NTDS"
            SYSVOLPath="C:\Windows\SYSVOL"
            SafeModeAdminPassword=P@ssw0rd
            Run-time flags (optional)
            RebootOnCompletion=Yes
            '''
        text = r'''
            $regkey = test-path hklm:\software\FTCAD
            if ($regkey -eq $true) {exit}
            else {
            # Turn Off Windows Firewall
            netsh advfirewall set allprofiles state off
            # Set Winrm trust for remote powershell
            Set-Item wsman:\localhost\client\trustedhosts * -Force
            # Install ADDS prerequisites
            Add-WindowsFeature RSAT-AD-Tools
            Add-WindowsFeature -Name "ad-domain-services" -IncludeAllSubFeature -IncludeManagementTools
            Add-WindowsFeature -Name "dns" -IncludeAllSubFeature -IncludeManagementTools
            Add-WindowsFeature -Name "gpmc" -IncludeAllSubFeature -IncludeManagementTools
            REG ADD HKLM\Software\FTCAD /v Data /t Reg_SZ /d "Installed"
            # Windows PowerShell script for AD DS Deployment
            
            $domainname = "''' +domainName[0]+ r'''"
            $netbiosName = "QTM"
            $safemodepassword = "P@ssw0rd" | ConvertTo-SecureString -AsPlainText -Force
            Import-Module ADDSDeployment
            Install-ADDSForest `
            -CreateDnsDelegation:$false `
            -DatabasePath "C:\Windows\NTDS" `
            -DomainMode "7" `
            -DomainName $domainname `
            -DomainNetbiosName $netbiosName `
            -ForestMode "7" `
            -InstallDns:$True `
            -LogPath "C:\Windows\NTDS" `
            -NoRebootOnCompletion:$false `
            -SafeModeAdministratorPassword $safemodepassword `
            -SysvolPath "C:\Windows\SYSVOL" `
            -Force:$true}
            # POWERSHELL TO EXECUTE ON REMOTE SERVER ENDS HERE

            # Domain promotion

            $exe = 'C:\Windows\System32\dcpromo.exe /unattend:'
            $varDir = $PSScriptRoot
            $var = '\dcinstall.txt'
            $cmd = $exe + $varDir + $var

            Invoke-expression $cmd

            '''

        with open('dcinstall.txt', 'w') as f:
                f.write(text2)
        with open('Install-DC.ps1', 'w') as f:
                f.write(text)
       
        subprocess.run(["powershell", "C:\\Users\\Administrator\\Desktop\\Test\\Install-DC.ps1"], shell=True)
        return render_template('index.html')

app.run(host="0.0.0.0", port=5000)
    

