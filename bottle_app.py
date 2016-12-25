
#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /assignment3/
#####################################################################

from bottle import route, run, default_app, debug, request

def Rondo(num): # This is a rounding function I made, it round 6.6 ro 7 and 5.2 to 5
    if (num - int(num) >= 0.5):
        return int(num) + 1
    else:
        return int(num)

musics = [{ 'name': 'Smells Like Teen Spirit',
            'year': 1991,
            'album': 'Nevermind',
            'band': 'Nirvana',
            'genre': 'Grunge',
            'rating': 5.0,
            'votes': 1},

          { 'name': 'Welcome to the Jungle',
            'year': 1987,
            'album': 'Appetite for Destruction',
            'band': "Guns N' Roses",
            'genre': 'Hard Rock',
            'rating': 5.0,
            'votes': 1}
          ] # This is the list for holding the musics
            # User can add to this list in runtime

allowedUsers = [
                {'username': "VahitOglu", 'password': "polimer"},
                {'username': "CansınBaba",'password': "csgo123"},
                {'username': "OmerZade",  'password': "htmlcss"}
                ] # This is the list of users who can edit the website
                  # This is changable in the program but cannot be reached
                  # from the website. Can be made into a fixed list in the future.

def htmlify(title, content, style):
    page = """<!DOCTYPE html>
        <html>
        <head>
        <meta charset="utf-8" />
        <title>""" + title + """</title>""" + style + """
            </head>
            <body>
            """ + content + """
                </body>
                </html>"""
    return page
# Damien's htmlify function, I added the 'style' parameter, for CSS use the below
# function that I made for easy CSS editing.


def CSS(): # This is where all styles will be, for clean coding please prevent
           # using inline styling as much as you can
    css = """<style>

        table.music td,th{
        border: groove 2px black;
        padding: 15px;}

        table.music tr{
        border-style: groove;}

        table.music{
        border-collapse: collapse;
        border-style: groove;}

        table.add td{
        padding: 0 15px 0 0;
        align = "center";}

        table.music{
        border-collapse: collapse;
        }

        table.music td, th{
        border: solid 2px black;
        padding: 15px;
        align = "center";}

        a.button {
        border: solid 2px black;
        border-radius: 5px;
        text-decoration: none;
        font-weight: bold;
        background-color: #22AABB;
        color: #555511;
        padding: 0 5px 0 5px;}

        th.rate{
        color: red;
        }

        td.rater{
        font-size: 10px;
        font-weight: bold;
        }
        </style>"""

    return css # You know CSS element.{something} means affect the elements of that class
               # If there is something like {element}.{class} {element2} then this means
               # affect the element2's under element.class

def a3_index(): # This is our index page
    indexCont = '<form method = "post" action = "/rate_submit/">\n'
    indexCont += '<table class = "music">\n'

    # If you want to use forms with tables you put the form in one cell or put the
    # whole table in a form, otherwise it is not valid. This is what I did.

    indexCont += "<tr>\n"
    indexCont += '<th>Name</th><th>Year</th><th>Album</th><th>Band</th><th>Genre</th><th class="rate">Very Bad</th><th class="rate">Bad</th><th class="rate">Meh</th><th class="rate">Good</th><th class="rate">Very Good!</th>\n'
    indexCont += "</tr>\n"
    # These are the headers of the table.

    i = 0
    for music in musics:
        indexCont += "<tr>\n"
        indexCont += "<td>" + music['name'] + "</td>\n"
        indexCont += "<td>" + str(music['year']) + "</td>\n"
        indexCont += "<td>" + music['album'] + "</td>\n"
        indexCont += "<td>" + music['band'] + "</td>\n"
        indexCont += "<td>" + music['genre'] + "</td>\n"
        indexCont += '<td> <input type="radio" name="rate" value="' + str(i) + '-1"> </td>\n'
        indexCont += '<td> <input type="radio" name="rate" value="' + str(i) + '-2"> </td>\n'
        indexCont += '<td> <input type="radio" name="rate" value="' + str(i) + '-3"> </td>\n'
        indexCont += '<td> <input type="radio" name="rate" value="' + str(i) + '-4"> </td>\n'
        indexCont += '<td> <input type="radio" name="rate" value="' + str(i) + '-5"> </td>\n'
        indexCont += "</tr>\n"
        i += 1
    # This for loop prints the songs in the musics list row by row
    # i here helps to mark what song is selected if it is the first song and
    # 'Very good!' is selected 'rate' will return 0-5 so I will understand
    # the first song is selected and got a rating of 5

    indexCont += "</table>\n"
    indexCont += """<table class = "button">
        <tr>
        <td><a href = "/add_page/" class = "button">Add a song!</a></td>
        <td><a href = "/rating_list/" class = "button">See the ratings</a></td>
        <td>Username: <input type = "text" name = "username" value = ""></td>
        <td>Password: <input type = "password" name = "password" value = ""></td>
        <td><input type="submit" value="Rate"></td>
        </tr>
        </table>
        </form>\n"""
    # This is the ending of our index page, it contains our buttons and user info

    return htmlify("My lovely website", indexCont, CSS())

def add_page():
    addPageContent = """<form method = "post" action = "/add_submit/">
        <table class = "add">
        <tr><td>Name:</td><td><input type = "text" name = "name" value = ""></td></tr>
        <tr><td>Year:</td><td><input type = "number" name = "year" value = ""></td></tr>
        <tr><td>Album:</td><td><input type = "text" name = "album" value = ""></td></tr>
        <tr><td>Band:</td><td><input type = "text" name = "band" value = ""></td></tr>
        <tr><td>Genre:</td><td><input type = "text" name = "genre" value = ""></td></tr>
        <tr>
        <td>Username: <input type = "text" name = "username" value = ""></td>
        <td>Password: <input type = "password" name = "password" value = ""></td>
        </tr>
        <tr><td><input type = "submit" value = "Add"></td><td><a href = "/assignment3/" class = "button">Return to the list</a></td></tr>
        </table>
        </form>
        """
    return htmlify("Add a song!", addPageContent, CSS())
# add_page is pretty straight forward, it creates forms to get song information
# then when the submit button is clicked it submits the innformation to /add_submit/

route ('/add_page/', 'GET', add_page)

def add_submit(): # This is the song adding page
    musicData = request.POST # The information from the add_page comes as a POST

    global allowedUsers # As I want to use this list I say I'm using the global list

    username = str(musicData['username'])
    password = str(musicData['password'])
    # This is the information I got from the add_page, I will use it to check if
    # user is valid or not

    validUser = False # Starts as false

    for user in allowedUsers:
        if (user['username'] == username and user['password'] == password):
            validUser = True # If any of that 3 users are the input to
                             # username and password boxes then we make validUser True

    if not validUser: # If the user is not valid, give an error page
        userError = "<h1>Your user information is wrong! Please try again.</h1>\n"
        userError += """<table>
                <tr>
                <td><a href = "/add_page/" class = "button">Try Again</a></td>
                <td><a href = "/assignment3/" class = "button">Return to the list</a></td>
                </tr>
                </table>"""
        return htmlify("There was an error :(", userError, CSS())

    # I checked the user information from the start so the other operations are
    # not made for nothing, if user is not valid these operations below will not be operated

    name = str(musicData['name'])
    year = int(musicData['year'])
    album = str(musicData['album'])
    band = str(musicData['band'])
    genre = str(musicData['genre'])
    # These are the information from the add_page, I get these from the text boxes

    global musics
    musics = musics + [{'name': name, 'year': year, 'album': album, 'band': band, 'genre': genre, 'rating': -1, 'votes': 0}]
    # I want to add a song to the musics list so I show I'm using the global to python
    # then as you see I am adding a song to the musics, this is the proper way to do it
    # I know the rect parantheses may seem odd but it is valid.

    addSubmitContent = """
        <h2>The song below has been added to the list</h2>
        <table class = "music">
        <tr><th>Name:</th><td>""" + name + """</td></tr>
        <tr><th>Year:</th><td>""" + str(year) + """</td></tr>
        <tr><th>Album:</th><td>""" + album + """</td></tr>
        <tr><th>Band:</th><td>""" + band + """</td></tr>
        <tr><th>Genre</th><td>""" + genre + """</td></tr>
        <tr><td colspan = "2"><a href = "/assignment3/" class = "button">Return to the list</a></td></tr>
        </table>"""
    return htmlify("Song successfully added!", addSubmitContent, CSS())
    # After all those operations a webpage is shown to tell the user he/she
    # successfully added the song

route ('/add_submit/', 'POST', add_submit)

def rate_submit():

    global musics
    global allowedUsers

    ratingData = request.POST

    isValid = False
    for user in allowedUsers:
        if ratingData['username'] == user['username'] and ratingData['password'] == user['password']:
            isValid = True

    if not isValid:
        userError = "<h1>Your user information is wrong! Please try again.</h1>\n"
        userError += """<table>
            <tr>
            <td><a href = "/assignment3/" class = "button">Return to the list</a></td>
            </tr>
            </table>"""
        return htmlify("There was an error :(", userError, CSS())

    # Above operations are just as same as the add_submit page

    rawRating = str(ratingData['rate']).split("-")
    # 'rate' is the name I give to radioboxes in the main page. When one of them
    # is checked and the rate button is clicked I get the value of it in a format of
    # {SongNumber}-{SongRating} so if the value is 5-9 6th(YES 6) song of the list is rated 9
    songNum = int(rawRating[0])
    # I splitted the value of radio so the first part is song number
    rating = int(rawRating[1])
    # and the second part is the rating
    votes = musics[songNum]['votes']
    # votes is an attribute of musics which counts how many votes have been given to the song
    musics[songNum]['rating'] = (musics[songNum]['rating'] * votes + rating) / (votes + 1)
    # This is pretty basic math, the average rating is 3 and I have 30 votes used so
    # if I want to add a new vote I multiply 3 * 30 then add my new rating then
    # then divide to 31 to get my new rating, and I assing my new rating
    musics[songNum]['votes'] += 1 # A vote is used so I increment votes

    name = str(musics[songNum]['name'])
    year = int(musics[songNum]['year'])
    album = str(musics[songNum]['album'])
    band = str(musics[songNum]['band'])
    genre = str(musics[songNum]['genre'])

    # This is different from the add_submit, I know the songs list number so using that
    # I get my song attributes from the global list musics using the songNum

    rateSubmitContent = """
        <h2>You have rated the song below</h2>
        <table class = "music">
        <tr><th>Name:</th><td>""" + name + """</td></tr>
        <tr><th>Year:</th><td>""" + str(year) + """</td></tr>
        <tr><th>Album:</th><td>""" + album + """</td></tr>
        <tr><th>Band:</th><td>""" + band + """</td></tr>
        <tr><th>Genre</th><td>""" + genre + """</td></tr>
        <tr><td colspan = "2"><a href = "/assignment3/" class = "button">Return to the list</a></td></tr>
        </table>"""
    return htmlify("You rated a song", rateSubmitContent, CSS())
    # Just as in the add_submit page I show what song is rated after all the operations.

route ('/rate_submit/', 'POST', rate_submit)

def rating_list(): # This is the page where all ratings are seen

    global musics

    ratingListContent = '<table class = "music">\n'
    ratingListContent += "<tr><th>Name</th><th>Bar</th><th>Rating</th></tr>"
    # Created the table and the headers
    for song in musics: # This for is printing songs in the list
        ratingListContent += "<tr>\n"
        ratingListContent += '<td>' + song['name'] + '</td>\n'
        ratingListContent += '<td class = "rater">'
        # Above code prints the name of the song to first cell
        for i in range(100):
            if i < Rondo((song['rating'] / 5) * 100):
                ratingListContent += "&#x25A0;" # Black Box - Unicde
            else:
                ratingListContent += "&#x25A1;" # White Box - Unicode
        # This for loops creates the rating bars, it makes the rating into %
        # then prints black boxes until the % is reached then prints white boxes
        ratingListContent += '</td>\n'
        ratingListContent += '<td>' + str("{0:.2f}".format(round(song['rating'],2))) + ' / <b>5</b></td>\n'
        # This code above prints the rating in the 3rd cell but it rounds 4.3262523 to 4.33
        ratingListContent += "</tr>\n"
    ratingListContent += '<tr>\n'
    ratingListContent += '<td colspan = "3"><a href = "/assignment3/" class = "button">Return to the list</a></td>\n'
    ratingListContent += '</tr>\n'
    ratingListContent += "</table>"
    return htmlify("Ratings", ratingListContent, CSS())
    # Lastly buttons are printed and the rating list is done
route ('/rating_list/', 'GET', rating_list)

def website_index():
    return htmlify('My lovely homepage',
                   """
                       <p><a href="/assignment1/">Click for my assignment 1.</a></p>
                       <p><a href="/assignment2/">Click for my assignment 2.</a></p>
                       <p><a href="/assignment3/">Click for my assignment 3.</a></p>
                       """, '')

route('/assignment3/', 'GET', a3_index)
route('/', 'GET', website_index)

#####################################################################
### Don't alter the below code.
### It allows this website to be hosted on PythonAnywhere
### OR run on your computer.
#####################################################################

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on PythonAnywhere
application = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
    run()

