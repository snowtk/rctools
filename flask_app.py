
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, abort
from flask_cors import CORS,cross_origin
import cabula
import rclayout
import git
import sys
app = Flask(__name__)
CORS(app)

dicto = cabula.get_dict()

killswitch = False
#teste2

@app.route('/update_server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('./mysite/.git')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400

#?b=alex
@app.route('/')
@cross_origin()
def hello_world():
    global killswitch
    if killswitch == False:
        if request.args.get('q') == 'ksskk':
            killswitch = True
            return "Gone"
        else:
            return get_from_dict(request.args.get('q'))
    else:
        if request.args.get('q') == "nksskk":
            killswitch = False
            return "Active"
        abort(404)
        return ''

@app.route('/js/')
def getjs():
    global killswitch
    if killswitch == True:
        abort(404)
        return ""
    else:
        return """var getHTML = function ( url, callback ) {
    	if ( !window.XMLHttpRequest ) return;
    	var xhr = new XMLHttpRequest();
    	xhr.onload = function() {
    		callback( this.responseText );
    	};
    	xhr.open( 'GET', url );
    	xhr.responseType = 'text';
    	xhr.send();
        };
        var q = function (question){
        		getHTML("https://snowkk.pythonanywhere.com/?q=" + question, console.log)
        }"""

def pretty_print_question(string, key, value):
    toprint = """"""
    toprint += "<hr /><div><dl class=\"row\">"
    ImageValue = key[:2]
    if key[2].isdigit() and int(key[1]) <= 2:
        if int(key[1]) == 1:
            ImageValue += key[2]
        elif int(key[1]) == 2 and int(key[2]) < 2:
            ImageValue += key[2]
    toprint += "<dt class=\"col-sm-2\">ID(2008) </dt> <dd class=\"col-sm-10\"><h6>" + ImageValue + "</h6></dd>"
    toprint += "<dt class=\"col-sm-2\">Pergunta </dt> <dd class=\"col-sm-10\"><h6>" + key[
                                                                                      len(ImageValue):] + "</h6></dd>"
    toprint += "<dt class=\"col-sm-2\"> Imagem </dt> <dd class=\"col-sm-10\"><img src=\"/static/images/" + ImageValue + "-2008.gif" + "\" alt=\"" + ImageValue + "\"></dd>"
    toprint += "<dt class=\"col-sm-2\">Opções Corretas </dt> <dd class=\"col-sm-10\">" + ', '.join(
        [x.upper() for x in value['cor']]) + "</dd>"
    toprint += "<dt class=\"col-sm-2\">Possiveis Opções </dt><dd class=\"col-sm-10\">"
    i = 0
    for v in value['quest']:
        i += 1
        toprint += "<br>R" + str(i) + "(" + v.strip() + ")"
    toprint += "</dd></dl></div>"
    return toprint;

def get_from_dict(string, per=True,ques=False):
    toprint = """"""
    added = []
    if per:
        for key, value in dicto.items():
                if (string.lower() if string is not None else "") in key.lower():
                    added.append(key.lower())
                    toprint += pretty_print_question(string,key,value)
    if ques:
        for key, value in dicto.items():
            add = False
            for v in value['quest']:
                if (string.lower() if string is not None else "") in v.lower():
                    add = True
            if add and key.lower() not in added:
                added.append(key.lower())
                toprint += pretty_print_question(string,key,value)
    return toprint

@app.route('/rcindex/')
def rcindex():
    global killswitch
    if killswitch == True:
        abort(404)
        return ""
    return rclayout.getlayout() + "<img src=\"https://www.portalgsti.com.br/media/uploads/marcomascarenhas/rede-de-computadores.jpg\">" + rclayout.getfooter()


@app.route('/rc/')
def pedrokey():
    global killswitch
    if killswitch == True:
        abort(404)
        return "This should not be returned"
    return rclayout.getlayout() + rclayout.get_question_bar() +rclayout.getfooter()

@app.route("/rcInputKey/", methods=['POST'])
def move_forward():
    print(request.form)
    name = request.form['fname']
    ques = "fper" in request.form
    res = "fques" in request.form
    global killswitch
    if killswitch == False:
        if name == "ksskk":
            killswitch = True
            return "Gone"
        else:
            return rclayout.getlayout() + rclayout.get_question_bar() + get_from_dict(name,ques,res) + rclayout.getfooter()
    else:
        if name == "nksskk":
            killswitch = False
            return 'Active'
        else:
            abort(404)
            return "Nothing here"

