#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /assignment3/
#####################################################################

from bottle import route, run, default_app, debug, request
from datetime import date

#A fake word coming from round
def Rondo(num): # This is a rounding function I made, it round 6.6 ro 7 and 5.2 to 5
    if (num - int(num) >= 0.5):
        return int(num) + 1
    else:
        return int(num)
#Songs
songs = [{ 'name': 'Smells Like Teen Spirit',
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
            'votes': 1},

          { 'name': 'Uptown Funk',
            'year': 2005,
            'album': 'Uptown Funk',
            'band': "Mark Ranson",
            'genre': 'Pop',
            'rating': 5.0,
            'votes': 1},
            
          { 'name': 'We Will Rock You',
            'year': 1977,
            'album': 'News of the World',
            'band': "Queen",
            'genre': 'Rock',
            'rating': 5.0,
            'votes': 1},
          
          { 'name': 'Smoke On The Water',
            'year': 1972,
            'album': 'Machine Head',
            'band': "Deep Purple",
            'genre': 'Metal',
            'rating': 5.0,
            'votes': 1},
          
          { 'name': 'Hit the Road Jack',
            'year': 2004,
            'album': 'Hit the Road Jack',
            'band': "Ray Charles",
            'genre': 'Blues',
            'rating': 5.0,
            'votes': 1},
          
          { 'name': ' He Walked on Water',
            'year': 1989,
            'album': "No Holdin' Back",
            'band': "Randy Travis",
            'genre': 'Country',
            'rating': 5.0,
            'votes': 1},
          
          { 'name': 'Forever in Love',
            'year': 1992,
            'album': 'Breathless',
            'band': "Kenny G",
            'genre': 'Jazz',
            'rating': 5.0,
            'votes': 1}         

          ] # This is the list for holding the musics
            # User can add to this list in runtime

#allowed users
allowedUsers = [
                {'username': "VahitOglu", 'password': "polimer"},
                {'username': "tnycnsn",'password': "tnycnsn"},
                {'username': "OmerZade",  'password': "htmlcss"}
                ] # This is the list of users who can edit the website
                  # This is changable in the program but cannot be reached
                  # from the website. Can be made into a fixed list in the future.

posted_comments=[]
# Variable posted_comments i defined. posted_comments will hold comments and users.

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
        body{
        background-color: #0099CC;
        }
        input{
        background-color: #AAEEFF;
        }
        textarea{
        background-color: #AAEEFF;
        }
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
        }
        table.music{
        border-collapse: collapse;
        width: 100%;
        height: 100%;
        }
        table.music td, th{
        background-color: #77EEEE;
        border: solid 2px black;
        padding: 15px;
        text-align: center;
        }
    
        table.comment td, th{
        border: solid 2px black;
        padding: 15px;
        text-align: center;
        }
        
        table.but{
        float: left;
        padding: 0 30px 0 0;
        }
        
        table.but td{
        padding: 5px;
        }
        
        table.inlog{
        float: right;
        }
        .button {
        border: solid 2px black;
        font-size: 20px;
        font-family: arial;
        border-radius: 5px;
        text-decoration: none;
        font-weight: bold;
        background-color: #2299AA;
        color: #225522;
        padding: 0 5px 0 5px;}
        th.rate{
        color: red;
        }
        td.rater{
        font-size: 10px;
        font-weight: bold;
        text-align: center;
        }
        
        .fleft{
        float: left;
        }
        </style>"""
    return css
               # You know CSS element.{something} means affect the elements of that class
               # If there is something like {element}.{class} {element2} then this means
               # affect the element2's under element.class

def generalError():
    content = '<h2 class = "error">There was an error with your submission, please try again.</h2>\n'
    content += '<a href = "/assignment3/" class = "button">Return to the list</a>'
    return htmlify("Error!", content, CSS())

def ValidateUser(username, password):

    global allowedUsers # As I want to use this list I say I'm using the global list

    validUser = False # Starts as false

    for user in allowedUsers:
        if (user['username'] == username and user['password'] == password):
            validUser = True
    # If any of that 3 users are the input to
    # username and password boxes then we make validUser True

    if not validUser: # If the user is not valid, give an error page
        userError = "<h1>Your user information is wrong! Please try again.</h1>\n"
        userError += """<table>
            <tr>
            <td><a href = "/assignment3/" class = "button">Return to the list</a></td>
            </tr>
            </table>"""
        return htmlify("There was an error :(", userError, CSS())
    return None


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
    for music in songs:
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
    indexCont += """
		<table class = "but">
			<tr>
				<td><a href = "/add_page/" class = "button">Add a song!</a></td>
				<td><a href = "/rating_list/" class = "button">See the ratings</a></td>
				<td><a href = "/comments/" class = "button">Add a comment</a></td>
				<td><a href = "/comment_list/" class = "button">See the comments</a></td>
				<td><a href = "/filter_category/" class = "button">Do You need a Filter?</a></td>
			</tr>
        </table>
        <table class="inlog">
			<tr>
				<td>Username: <input type = "text" name = "username" value = ""></td>
				<td>Password: <input type = "password" name = "password" value = ""></td>
				<td><input type="submit" value="Rate"></td>
			</tr>
        </table></form>"""

    if len(songs) is not 0:
        indexCont += """
                <form method = "get" action = "/delete_item/">
                <table>
                <tr>
                <td>Delete an item: </td>
                    <td><select name="delete">"""
        i = 0
        for song in songs:
            indexCont += '<option value="' + str(i) + '">' + song['name'] + '</option>\n'
            i += 1
        indexCont += "</select>\n</td>"
        indexCont += '<td><input type = "submit" value = "Delete"></td>'
        indexCont += "</table>"
        indexCont += "</form>"

    # This is the ending of our index page, it contains our buttons and user info

    return htmlify("My lovely website", indexCont, CSS())

def add_page():
    addPageContent = """<form method = "post" action = "/add_submit/">
        <table class = "add">
        <tr><td>Name:</td><td><input type = "text" name = "name" value = ""></td></tr>
        <tr><td>Year:</td><td><input type = "number" name = "year" value = ""></td></tr>
        <tr><td>Album:</td><td><input type = "text" name = "album" value = ""></td></tr>
        <tr><td>Band:</td><td><input type = "text" name = "band" value = ""></td></tr>
        <tr><td>Genre:</td><td><input type = "text" name = "genre" value = ""></td></tr></table>
        <table>
        <tr>
        <td>Username: <input type = "text" name = "username" value = ""></td>
        <td>Password: <input type = "password" name = "password" value = ""></td>
        <td><input type = "submit" value = "Add" class="button"></td>
        </tr>
        <tr>
        <td colspan="3"><a href = "/assignment3/" class = "button">Return to the list</a></td>
        </tr>
        </table>
        </form>
        """
    return htmlify("Add a song!", addPageContent, CSS())
# add_page is pretty straight forward, it creates forms to get song information
# then when the submit button is clicked it submits the innformation to /add_submit/

route ('/add_page/', 'GET', add_page)

def add_submit(): # This is the song adding page
    musicData = request.POST
    # The information from the add_page comes as a POST

    checker = ValidateUser(str(musicData['username']), str(musicData['password']))
    if checker is not None:
        return checker

    # I checked the user information from the start so the other operations are
    # not made for nothing, if user is not valid these operations below will not be operated

    name = str(musicData['name'])

    if name == "":
        return generalError()

    year = int(musicData['year'])

    if year < 0 or year > 2017:
        return generalError()

    album = str(musicData['album'])

    if album == "":
        return generalError()

    band = str(musicData['band'])

    if band == "":
        return generalError()

    genre = str(musicData['genre'])

    if genre == "":
        return generalError()
    # These are the information from the add_page, I get these from the text boxes

    global songs
    songs = songs + [{'name': name, 'year': year, 'album': album, 'band': band, 'genre': genre, 'rating': -1, 'votes': 0}]
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

    global songs
    global allowedUsers

    ratingData = request.POST

    checker = ValidateUser(str(ratingData['username']), str(ratingData['password']))
    if checker is not None:
        return checker

    # Above operations are just as same as the add_submit page
    if not 'rate' in ratingData:
        return generalError()

    rawRating = str(ratingData['rate']).split("-")
    # 'rate' is the name I give to radioboxes in the main page. When one of them
    # is checked and the rate button is clicked I get the value of it in a format of
    # {SongNumber}-{SongRating} so if the value is 5-9 6th(YES 6) song of the list is rated 9
    songNum = int(rawRating[0])
    # I splitted the value of radio so the first part is song number
    rating = int(rawRating[1])
    # and the second part is the rating
    votes = songs[songNum]['votes']
    # votes is an attribute of songs which counts how many votes have been given to the song
    songs[songNum]['rating'] = (songs[songNum]['rating'] * votes + rating) / (votes + 1)
    # This is pretty basic math, the average rating is 3 and I have 30 votes used so
    # if I want to add a new vote I multiply 3 * 30 then add my new rating then
    # then divide to 31 to get my new rating, and I assing my new rating
    songs[songNum]['votes'] += 1 # A vote is used so I increment votes

    name = str(songs[songNum]['name'])
    year = int(songs[songNum]['year'])
    album = str(songs[songNum]['album'])
    band = str(songs[songNum]['band'])
    genre = str(songs[songNum]['genre'])

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
        <tr><td><a href = "/rating_list/" class = "button">See the ratings</a></td>
        <td><a href = "/assignment3/" class = "button">Return to the list</a></td></tr>
        </table>"""
    return htmlify("You rated a song", rateSubmitContent, CSS())
    # Just as in the add_submit page I show what song is rated after all the operations.

route ('/rate_submit/', 'POST', rate_submit)

def rating_list(): # This is the page where all ratings are seen

    global songs

    ratingListContent = '<table class = "music">\n'
    ratingListContent += "<tr><th>Name</th><th>Bar</th><th>Rating</th></tr>"
    # Created the table and the headers
    for song in songs: # This for is printing songs in the list
        ratingListContent += "<tr>\n"
        ratingListContent += '<td>' + song['name'] + '</td>\n'
        ratingListContent += '<td class = "rater">'
        # Above code prints the name of the song to first cell
        for i in range(100):
            if i < Rondo((song['rating'] / 5) * 100):
                ratingListContent += "&#x25A0;" # Black Box - Unicde
            else:
                ratingListContent += "&#x25A1;" # White Box - Unicode
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

def comments(): #Valid HTML
    # Defining a function to make users able to leave comments.
    html="""<h2>Leave a comment to us!</h2>
    <form method="post" action="/comment_sent/" id="comment">
    <table>
    <tr><td>Name:</td></tr>
    <tr><td><input type="text" name="nick" size="67"></td></tr>
    <tr><td>Comment:</td></tr>
    <tr><td><textarea name="comment" form="comment" rows="7" cols="65"></textarea></td></tr>
    </table>
    <table class = "but">
    <tr>
    <td><input type="submit" value="Send your comment" class="button"></td>
    <td><a href="/comment_list/" class = "button">Click to see other comments!</a></td>
    <td><a href = "/assignment3/" class = "button">Click to return to the list</a></td></tr>
    </table>
    </form>
    """
    # <textarea> element creates a text area which provides us to take text inputs with no character boundaries.
    # <form> and <textarea> elements are associated with id="comment" and form="comment" attributes and values.(line 382 and 385)
    # Data is taken with post method. A link is given to see the other comments.
    
    return htmlify("Comments", html, CSS()) # Returning htmlified content.

route ('/comments/', 'GET', comments) # Routing...

def comment_sent(): #Valid HTML
    # Defining a function to get data with post method.
    global posted_comments
    # Making variables global to access them in another function.
    commentdata = request.POST
    # Data is reached.
    posted_comments.append({'name': str(commentdata['nick']), 'comment': str(commentdata['comment'])})
    # Data is saved.
    html="""<h1>Your comment successfully sent!</h1>
    <table><tr>
    <td><a href="/comment_list/" class = "button">Click to see other comments</a></td>
    <td><a href="/assignment3/" class = "button">Click to go to the main page</a></td></tr></table>
    """
    # Information and links to Home Page and Comment List.
    return htmlify("Comment Sent!", html, CSS()) # Returning htmlified content.

route ('/comment_sent/', 'POST', comment_sent) # Routing...

def comment_list():

    global posted_comments

    # Defining a function to list all comments and names.
    html="""
    <table class = "music">
    <tr>
    <th>Name/Nickname</th>
    <th>Comment</th>
    </tr>
    """
    # A table element is created.
    for comment in posted_comments:
        html+="""<tr>
        <td>""" + comment['name'] + """</td>
        <td>""" + comment['comment'] + """</td>
        </tr></table>"""
    # Adding comments and names as table data.
    html+="""<table><tr>
    <td><a href="/assignment3/" class = "button">Click to go to the main page</a></td>
    <td><a href="/comments/" class = "button">Click to add a comment</a></td></tr></table>"""
    # End of html content, with a closing tag and two links, one goes to Home Page and one goes to comment adding page.

    return htmlify("Comment List", html, CSS()) # Returning htmlified content.

route('/comment_list/', 'GET', comment_list) # Routing...


def filter_category():
    # Defining a function to make users able to leave comments.
    html="""<h3>You can choose below categories for filter:</h3>
    <form method="post" action="/filter_results/" id="comment">
    <table>
	<tr><td><input type="checkbox" name="Pop" value="Pop"></td><td>Pop</td></tr>
	<tr><td><input type="checkbox" name="Rock" value="Rock"></td><td>Rock</td></tr>
	<tr><td><input type="checkbox" name="Hard Rock" value="Hard Rock"></td><td>Hard Rock</td></tr>
	<tr><td><input type="checkbox" name="Metal" value="Metal"></td><td>Metal</td></tr>
	<tr><td><input type="checkbox" name="Blues" value="Blues"></td><td>Blues</td></tr>
	<tr><td><input type="checkbox" name="Country" value="Country"></td><td>Country</td></tr>
	<tr><td><input type="checkbox" name="Jazz" value="Jazz"></td><td>Jazz</td></tr>
	<tr><td><input type="checkbox" name="Grunge" value="Grunge"></td><td>Grunge</td></tr>
    <tr><td colspan = "2"><input type="submit" value="Filter Song Categories" class="button"></td></tr>
    </table>
    </form>
    """

    return htmlify("filter", html, CSS()) # Returning htmlified content.

route ('/filter_category/', 'GET', filter_category) # Routing...

def filter_results():
	global songs
	selectedGenre = request.POST
	html = """<table class="music">\n
	<tr><th>Name</th><th>Year</th><th>Album</th><th>Band</th><th>Genre</th></tr>\n"""
	for g in selectedGenre:
		for s in songs:
			a = s['genre']
			if g == a:
				html += "<tr>\n"
				html += "<td>" + s['name'] + "</td>\n"
				html += "<td>" + str(s['year']) + "</td>\n"
				html += "<td>" + s['album'] + "</td>\n"
				html += "<td>" + s['band'] + "</td>\n"
				html += "<td>" + s['genre'] + "</td>\n"
				html += "</tr>\n"
	html += "</table>"
	html += '<a href = "/assignment3/" class = "button">Click to go to the main page</a>'
	
	return htmlify("Results", html, CSS())
     
route('/filter_results/', 'POST', filter_results)

def delete_item():
    global songs

    delete = request.GET['delete']

    name = songs[int(delete)]['name']
    year = songs[int(delete)]['year']
    album = songs[int(delete)]['album']
    band = songs[int(delete)]['band']
    genre = songs[int(delete)]['genre']

    del songs[int(delete)]

    delete_content = """
        <h2>You have deleted the song below</h2>
        <table class = "music">
        <tr><th>Name:</th><td>""" + name + """</td></tr>
        <tr><th>Year:</th><td>""" + str(year) + """</td></tr>
        <tr><th>Album:</th><td>""" + album + """</td></tr>
        <tr><th>Band:</th><td>""" + band + """</td></tr>
        <tr><th>Genre</th><td>""" + genre + """</td></tr>
        <tr><td colspan = "2"><a href = "/assignment3/" class = "button">Return to the list</a></td></tr>
        </table>"""
    return htmlify("You've deleted a song!", delete_content, CSS())

route('/delete_item/', 'GET', delete_item)


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
