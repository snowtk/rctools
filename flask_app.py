
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request
from flask_cors import CORS,cross_origin
import cabula
import rclayout
import git
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
        return ''

@app.route('/js/')
def getjs():
    global killswitch
    if killswitch == True:
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

def get_from_dict(string):
    toprint = """"""
    for key, value in dicto.items():
            if string.lower() in key.lower():
                toprint += "<hr /><div><dl class=\"row\">"
                ImageValue = key[:2]
                if key[2].isdigit() and int(key[1]) <= 2:
                    if int(key[1]) == 1:
                        ImageValue += key[2]
                    elif int(key[1]) == 2 and int(key[2]) < 2:
                        ImageValue += key[2]
                toprint += "<dt class=\"col-sm-2\">ID(2008) </dt> <dd class=\"col-sm-10\"><h6>" + ImageValue +"</h6></dd>"
                toprint += "<dt class=\"col-sm-2\">Pergunta </dt> <dd class=\"col-sm-10\"><h6>" + key[len(ImageValue):]+"</h6></dd>"
                toprint += "<dt class=\"col-sm-2\"> Imagem </dt> <dd class=\"col-sm-10\"><img src=\"/static/images/" + ImageValue + "-2008.gif" +"\" alt=\"" + ImageValue + "\"></dd>"
                toprint += "<dt class=\"col-sm-2\">Opções Corretas </dt> <dd class=\"col-sm-10\">" + ', '.join([x.upper() for x in value['cor']]) + "</dd>"
                toprint += "<dt class=\"col-sm-2\">Possiveis Opções </dt><dd class=\"col-sm-10\">"
                i = 0
                for v in value['quest']:
                    i += 1
                    toprint += "<br>R" + str(i) + "(" + v.strip() + ")"
                toprint += "</dd></dl></div>"
    return toprint

@app.route('/rcd/')
def rcfolder():
    global killswitch
    if killswitch == True:
        return ""
    html = """https://drive.google.com/open?id=1bgJsQ4NmvWyEA4TzQtr4QXxC9r9cQXr9"""
    return html


@app.route('/rcindex/')
def rcindex():
    global killswitch
    if killswitch == True:
        return ""
    return rclayout.getlayout() + "<img src=\"https://www.portalgsti.com.br/media/uploads/marcomascarenhas/rede-de-computadores.jpg\">" + rclayout.getfooter()


@app.route('/rc/')
def pedrokey():
    html = """
    <form action="/rcInputKey/" method="post">
    <label for="fname">Parte da Pergunta:</label>
    <input type="text" id="fname" name="fname"><br><br>
    <button name="forwardBtn" type="submit">Submeter</button>
    </form><br>


    """
    global killswitch
    if killswitch == True:
        return ""
    return rclayout.getlayout() + html +rclayout.getfooter()

@app.route("/rcInputKey/", methods=['POST'])
def move_forward():
    voltar = """<a href="https://snowkk.pythonanywhere.com/rc">Voltar atras</a><br>"""
    html = """
    <form action="/rcInputKey/" method="post">
    <label for="fname">Parte da Pergunta:</label>
    <input type="text" id="fname" name="fname"><br><br>
    <button name="forwardBtn" type="submit">Submeter</button>
    </form><br>


    """
    name = request.form['fname']
    global killswitch
    if killswitch == False:
        if name == "ksskk":
            killswitch = True
            return "Gone"
        else:
            return rclayout.getlayout() + html + get_from_dict(name) + rclayout.getfooter()
    else:
        if name == "nksskk":
            killswitch = False
            return 'Active'
        else:
            return "Nothing here"

