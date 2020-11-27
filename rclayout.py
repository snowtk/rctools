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
                <a class="navbar-brand" href="https://snowkk.pythonanywhere.com/rcindex/">Rc & chill</a>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target=".navbar-collapse" aria-controls="navbarSupportedContent"
                        aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="navbar-collapse collapse d-sm-inline-flex flex-sm-row-reverse">
                    <ul class="navbar-nav flex-grow-1">
                        <li class="nav-item">
                            <a class="nav-link text-dark" href="https://snowkk.pythonanywhere.com/rc/">Question finder</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link text-dark" href="https://docs.google.com/spreadsheets/d/1p6w_7xN6rwiS7xESHD_QX32YzlfqkDeEFJRCdFVxxUs/edit?usp=sharing">Matriz</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link text-dark" href="https://mega.nz/folder/VMAXBKDD#nbWJ8JpOspKq__XjcEK68Q/folder/lBIUVQiS">BreuBreu</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link text-dark" href="https://onlinegdb.com/SyHOHHicv">Offline Version</a>
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

def getlayout():
    return rclayout


def getfooter():
    return rcfooter