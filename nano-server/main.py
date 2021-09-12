from flask import Flask
from flask import Flask, render_template, request
from flask import Markup

app = Flask(__name__)

#A function
import os
#def runCode(command) :
  #result = os.popen(command).readlines()
  #print (result)


#Determines the entry point, / means root of the website

#New route - go to /cakes to view
@app.route('/', methods=['post', 'get'])


            
def login():
    #Initialise some variables
    directory = '/app/savefile/';
    result = os.popen("ls "+directory).readlines()
    result = ''.join(result)
    result = result.replace("\n","<br>")
    result = Markup(result)
    message = result
    fileCode = "";
    defaultValue = "Add Ansible file content here"
    fileCode = defaultValue
    if request.method == 'POST':
        username = request.form.get('username')  # access the data inside 
        password = request.form.get('password')
        fileNameInput = request.form.get('fileNameInput')
        fileCode = defaultValue
        if username == 'root' and password == 'pass':
            message = "Hidden stuff unlocked - boss mode activated. You are one clever coder, that's for sure!"
            fileCode = defaultValue
        else:
            directory = 'Terminal:'
            message = "Wrong username or password"
            result = os.popen(username).readlines()
            result = ''.join(result)
            result = result.replace("\n","<br>")
            result = Markup(result)
            #strResult = result
            #message = '>>> ' + strResult 
            message = result
            fileCode 
            if password != "No code":
              fileCode = password
            else:
              fileCode = "No code" 
            if(username == 'open') :
                fileNameInputdir = "/app/savefile/" + fileNameInput
                file = open(fileNameInputdir, 'r') 
                fileCode = file.read()
                file.close()
                message = '>>> '
            elif (username == 'save') :
                fileNameInputdir = "/app/savefile/" + fileNameInput 
                f = open(fileNameInputdir, 'w')
                message = fileNameInput
                f.write(password)
                f.close()
                message = '>>> '
            elif (username == 'ls') :
              fileNameInputdir = "/app/savefile/"
              cmd = "ls " + fileNameInputdir
              result = os.popen(cmd).readlines()
              result = ''.join(result)
              result = result.replace("\n","<br>")
              value = Markup(result)
              message = value
            elif (username == 'pwd') :
              fileNameInputdir = "/app/savefile/"
              value = Markup(fileNameInputdir)
              message = value
                    
 
    return render_template('index.html', message=message, fileCode=fileCode, directory=directory)  


#Runs the webserver and the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
