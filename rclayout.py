rclayout = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>RC & chill</title>
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>
	<!--<link rel="stylesheet" href="~/lib/bootstrap/dist/css/bootstrap.min.css" />
    <link rel="stylesheet" href="~/css/site.css" />-->
</head>
<body>
    <header>
        <nav class="navbar navbar-expand-sm navbar-toggleable-sm navbar-light bg-white border-bottom box-shadow mb-3">
            <div class="container">
                <a class="navbar-brand" href="/rcindex/">Rc & chill</a>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target=".navbar-collapse" aria-controls="navbarSupportedContent"
                        aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="navbar-collapse collapse d-sm-inline-flex flex-sm-row-reverse">
                    <ul class="navbar-nav flex-grow-1">
                        <li class="nav-item">
                            <a class="nav-link text-dark" href="/rc/">Question finder</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link text-dark" href="https://docs.google.com/spreadsheets/d/1p6w_7xN6rwiS7xESHD_QX32YzlfqkDeEFJRCdFVxxUs/edit?usp=sharing">Matriz</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    </header>
    <div class="container" id="main">
"""

rcfooter = """
    </div>

    <footer class="border-top footer text-muted">
        <div class="container">
				2020 -  EST Setúbal
        </div>
    </footer>
</body>
</html>
"""

rc_question_bar = """
    <form action="/rcInputKey/" method="post">
    <div class ="d-flex"><div>
    <input type="checkbox" id="fper" name="fper" checked>
    <label for="fper">Pesquisar nas Pergunta</label><br>
    </div> <div class="ml-2" style="border-left:2px solid black;height: 20px"></div> <div class="pl-2">
    <input type="checkbox" id="fques" name="fques" checked>
    <label for="fques">Pesquisar nas Respostas</label><br>
    </div></div>
    <label for="fname">Segmento a procurar:</label>
    <input type="text" id="fname" name="fname"><br>
    <button name="forwardBtn" class="btn btn-info" type="submit">Submeter</button>
    </form><br>
    """

rc_submeter_form = """
    <form action="/rcSubmit/" method="post">
            <div class="text-danger"></div>
            <div class="form-group">
                <label for="id" class="control-label">ID(vazio se desconhecido)</label>
                <input type="text" id="id" name="id" class="form-control" />
                <span class="text-danger"></span>
            </div>
            <div class="form-group">
                <label for="Pergunta" class="control-label">Pergunta</label>
                <input type="text" id="Pergunta" class="form-control" />
                <span class="text-danger"></span>
            </div>
            <div class="form-group">
                <label for="urlimg" class="control-label">Url da Imagem</label>
                <input type="text" id="urlimg" class="form-control" />
                <span class="text-danger"></span>
            </div>
            <div class="form-group">
                <label for="pres" class="control-label">Possiveis respostas (Por ordem)</label>
                <input type="text" id="pres" class="form-control" />
                <span class="text-danger"></span>
            </div>
            <div class="form-group">
                <label for="rcor" class="control-label">Respostas corretas</label>
                <input type="text" id="rcor" class="form-control" />
                <span class="text-danger"></span>
            </div>
            <div class="form-group">
                <input type="submit" value="Submeter" class="btn btn-primary" />
            </div>
        </form>

"""


def get_submeter_form():
    return rc_submeter_form


def get_question_bar():
    return rc_question_bar


def getlayout():
    return rclayout


def getfooter():
    return rcfooter