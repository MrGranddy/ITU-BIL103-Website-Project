from bottle import route, run, default_app, debug, request

# Songs
# This is the list for holding the musics
# User can add to this list in runtime
songs = [
    {'name': 'Smells Like Teen Spirit',
     'year': 1991,
     'album': 'Nevermind',
     'band': 'Nirvana', 'genre': 'Grunge',
     'rating': 5.0,
     'votes': 1},

    {'name': 'Welcome to the Jungle',
     'year': 1987,
     'album': 'Appetite for Destruction',
     'band': "Guns N' Roses",
     'genre': 'Hard Rock',
     'rating': 5.0,
     'votes': 1},

    {'name': 'Uptown Funk',
     'year': 2005,
     'album': 'Uptown Funk',
     'band': "Mark Ranson",
     'genre': 'Pop',
     'rating': 5.0,
     'votes': 1},

    {'name': 'We Will Rock You',
     'year': 1977,
     'album': 'News of the World',
     'band': "Queen",
     'genre': 'Rock',
     'rating': 5.0,
     'votes': 1},

    {'name': 'Smoke On The Water',
     'year': 1972,
     'album': 'Machine Head',
     'band': "Deep Purple",
     'genre': 'Metal',
     'rating': 5.0,
     'votes': 1},

    {'name': 'Hit the Road Jack',
     'year': 2004,
     'album': 'Hit the Road Jack',
     'band': "Ray Charles",
     'genre': 'Blues',
     'rating': 5.0,
     'votes': 1},

    {'name': ' He Walked on Water',
     'year': 1989,
     'album': "No Holdin' Back",
     'band': "Randy Travis",
     'genre': 'Country',
     'rating': 5.0,
     'votes': 1},

    {'name': 'Forever in Love',
     'year': 1992,
     'album': 'Breathless',
     'band': "Kenny G",
     'genre': 'Jazz',
     'rating': 5.0,
     'votes': 1}]

# allowed users
# This is the list of users who can edit the website
# This is changable in the program but cannot be reached
# from the website. Can be made into a fixed list in the future.
allowedUsers = [
    {'username': "VahitOglu", 'password': "polimer"},
    {'username': "tnycnsn", 'password': "tnycnsn"},
    {'username': "OmerZade", 'password': "htmlcss"}
]

posted_comments = []


def rondo(num):  # A fake word coming from round
    # This is a rounding function I made, it round 6.6 ro 7 and 5.2 to 5
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)


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


def CSS():  # This is where all styles will be, for clean coding please prevent
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
            border-style: groove;
        }

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
            padding: 0 5px 0 5px;
        }

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


# Returns a general error page
def general_error():
    content = '<h2 class = "error">There was an error with your submission, please try again.</h2>\n'
    content += '<a href = "/assignment3/" class = "button">Return to the list</a>\n'
    return htmlify("Error!", content, CSS())


# Returns none if user is valid, returns error page otherwise
def validate_user(username, password):
    global allowedUsers  # As I want to use this list I say I'm using the global list

    valid_user = False  # Starts as false

    for user in allowedUsers:
        if user['username'] == username and user['password'] == password:
            valid_user = True

    # If any of that 3 users are the input to
    # username and password boxes then we make validUser True

    if not valid_user:  # If the user is not valid, give an error page
        user_error = '<h1>Your user information is wrong! Please try again.</h1>\n'
        user_error += '<table>\n'
        user_error += '<tr>\n'
        user_error += '<td><a href = "/assignment3/" class = "button">Return to the list</a></td>\n'
        user_error += '</tr>\n'
        user_error += '</table>\n'
        return htmlify("There was an error :(", user_error, CSS())
    return None


def a3_index():  # This is our index page
    index_content = '<form method = "post" action = "/rate_submit/">\n'
    index_content += '<table class = "music">\n'

    # If you want to use forms with tables you put the form in one cell or put the
    # whole table in a form, otherwise it is not valid. This is what I did.

    index_content += '<tr>\n'
    index_content += '<th>Name</th>\n'
    index_content += '<th>Year</th>\n'
    index_content += '<th>Album</th>\n'
    index_content += '<th>Band</th>\n'
    index_content += '<th>Genre</th>\n'
    index_content += '<th class="rate">Very Bad</th>\n'
    index_content += '<th class="rate">Bad</th>\n'
    index_content += '<th class="rate">Meh</th>\n'
    index_content += '<th class="rate">Good</th>\n'
    index_content += '<th class="rate">Very Good!</th>\n'
    index_content += '</tr>\n'
    # These are the headers of the table.

    i = 0
    for music in songs:
        index_content += '<tr>\n'
        index_content += '<td>' + music['name'] + '</td>\n'
        index_content += '<td>' + str(music['year']) + '</td>\n'
        index_content += '<td>' + music['album'] + '</td>\n'
        index_content += '<td>' + music['band'] + '</td>\n'
        index_content += '<td>' + music['genre'] + '</td>\n'
        index_content += '<td> <input type="radio" name="rate" value="' + str(i) + '-1"> </td>\n'
        index_content += '<td> <input type="radio" name="rate" value="' + str(i) + '-2"> </td>\n'
        index_content += '<td> <input type="radio" name="rate" value="' + str(i) + '-3"> </td>\n'
        index_content += '<td> <input type="radio" name="rate" value="' + str(i) + '-4"> </td>\n'
        index_content += '<td> <input type="radio" name="rate" value="' + str(i) + '-5"> </td>\n'
        index_content += '</tr>\n'
        i += 1
    # This for loop prints the songs in the musics list row by row
    # i here helps to mark what song is selected if it is the first song and
    # 'Very good!' is selected 'rate' will return 0-5 so I will understand
    # the first song is selected and got a rating of 5

    index_content += '</table>\n'
    index_content += '<table class = "but">\n'
    index_content += '<tr>\n'
    index_content += '<td><a href = "/add_page/" class = "button">Add a song!</a></td>\n'
    index_content += '<td><a href = "/rating_list/" class = "button">See the ratings</a></td>\n'
    index_content += '<td><a href = "/comments/" class = "button">Add a comment</a></td>\n'
    index_content += '<td><a href = "/comment_list/" class = "button">See the comments</a></td>\n'
    index_content += '<td><a href = "/filter_category/" class = "button">Do You need a Filter?</a></td>\n'
    index_content += '</tr>\n'
    index_content += '</table>\n'
    index_content += '<table class="inlog">\n'
    index_content += '<tr>\n'
    index_content += '<td>Username: <input type = "text" name = "username" value = ""></td>\n'
    index_content += '<td>Password: <input type = "password" name = "password" value = ""></td>\n'
    index_content += '<td><input type="submit" value="Rate"></td>\n'
    index_content += '</tr>\n'
    index_content += '</table></form>\n'

    if len(songs) is not 0:
        index_content += '<form method = "get" action = "/delete_item/">\n'
        index_content += '<table>\n'
        index_content += '<tr>\n'
        index_content += '<td>Delete an item: </td>\n'
        index_content += '<td><select name="delete">\n'
        i = 0
        for song in songs:
            index_content += '<option value="' + str(i) + '">' + song['name'] + '</option>\n'
            i += 1
        index_content += '</select>\n</td>\n'
        index_content += '<td><input type = "submit" value = "Delete"></td>\n'
        index_content += '</table>\n'
        index_content += '</form>\n'

    # This is the ending of our index page, it contains our buttons and user info

    return htmlify("My lovely website", index_content, CSS())


def add_page():
    add_page_content = '<form method = "post" action = "/add_submit/">\n'
    add_page_content += '<table class = "add">\n'
    add_page_content += '<tr><td>Name:</td><td><input type = "text" name = "name" value = ""></td></tr>\n'
    add_page_content += '<tr><td>Year:</td><td><input type = "number" name = "year" value = ""></td></tr>\n'
    add_page_content += '<tr><td>Album:</td><td><input type = "text" name = "album" value = ""></td></tr>\n'
    add_page_content += '<tr><td>Band:</td><td><input type = "text" name = "band" value = ""></td></tr>\n'
    add_page_content += '<tr><td>Genre:</td><td><input type = "text" name = "genre" value = ""></td></tr></table>\n'
    add_page_content += '<table>\n'
    add_page_content += '<tr>\n'
    add_page_content += '<td>Username: <input type = "text" name = "username" value = ""></td>\n'
    add_page_content += '<td>Password: <input type = "password" name = "password" value = ""></td>\n'
    add_page_content += '<td><input type = "submit" value = "Add" class="button"></td>\n'
    add_page_content += '</tr>\n'
    add_page_content += '<tr>\n'
    add_page_content += '<td colspan="3"><a href = "/assignment3/" class = "button">Return to the list</a></td>\n'
    add_page_content += '</tr>\n'
    add_page_content += '</table>\n'
    add_page_content += '</form>\n'
    return htmlify("Add a song!", add_page_content, CSS())


# add_page is pretty straight forward, it creates forms to get song information
# then when the submit button is clicked it submits the innformation to /add_submit/

route('/add_page/', 'GET', add_page)


def add_submit():  # This is the song adding page
    music_data = request.POST
    # The information from the add_page comes as a POST

    checker = validate_user(str(music_data['username']), str(music_data['password']))
    if checker is not None:
        return checker

    # I checked the user information from the start so the other operations are
    # not made for nothing, if user is not valid these operations below will not be operated

    name = str(music_data['name'])

    if name == "":
        return general_error()

    year = int(music_data['year'])

    if year < 0 or year > 2017:
        return general_error()

    album = str(music_data['album'])

    if album == "":
        return general_error()

    band = str(music_data['band'])

    if band == "":
        return general_error()

    genre = str(music_data['genre'])

    if genre == "":
        return general_error()
    # These are the information from the add_page, I get these from the text boxes

    global songs
    songs += [
        {'name': name,
         'year': year,
         'album': album,
         'band': band,
         'genre': genre,
         'rating': -1,
         'votes': 0}]

    # I want to add a song to the musics list so I show I'm using the global to python
    # then as you see I am adding a song to the musics, this is the proper way to do it
    # I know the rect parantheses may seem odd but it is valid.

    add_submit_content = """
        <h2>The song below has been added to the list</h2>
        <table class = "music">
        <tr><th>Name:</th><td>""" + name + """</td></tr>
        <tr><th>Year:</th><td>""" + str(year) + """</td></tr>
        <tr><th>Album:</th><td>""" + album + """</td></tr>
        <tr><th>Band:</th><td>""" + band + """</td></tr>
        <tr><th>Genre</th><td>""" + genre + """</td></tr>
        <tr><td colspan = "2"><a href = "/assignment3/" class = "button">Return to the list</a></td></tr>
        </table>"""
    return htmlify("Song successfully added!", add_submit_content, CSS())
    # After all those operations a webpage is shown to tell the user he/she
    # successfully added the song


route('/add_submit/', 'POST', add_submit)


def rate_submit():
    global songs
    global allowedUsers

    ratingData = request.POST

    checker = validate_user(str(ratingData['username']), str(ratingData['password']))
    if checker is not None:
        return checker

    # Above operations are just as same as the add_submit page
    if not 'rate' in ratingData:
        return general_error()

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
    songs[songNum]['votes'] += 1  # A vote is used so I increment votes

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


route('/rate_submit/', 'POST', rate_submit)


def rating_list():  # This is the page where all ratings are seen

    global songs

    ratingListContent = '<table class = "music">\n'
    ratingListContent += "<tr><th>Name</th><th>Bar</th><th>Rating</th></tr>"
    # Created the table and the headers
    for song in songs:  # This for is printing songs in the list
        ratingListContent += "<tr>\n"
        ratingListContent += '<td>' + song['name'] + '</td>\n'
        ratingListContent += '<td class = "rater">'
        # Above code prints the name of the song to first cell
        for i in range(100):
            if i < rondo((song['rating'] / 5) * 100):
                ratingListContent += "&#x25A0;"  # Black Box - Unicde
            else:
                ratingListContent += "&#x25A1;"  # White Box - Unicode
        # This for loops creates the rating bars, it makes the rating into %
        # then prints black boxes until the % is reached then prints white boxes
        ratingListContent += '</td>\n'
        ratingListContent += '<td>' + str("{0:.2f}".format(round(song['rating'], 2))) + ' / <b>5</b></td>\n'
        # This code above prints the rating in the 3rd cell but it rounds 4.3262523 to 4.33
        ratingListContent += "</tr>\n"
    ratingListContent += '<tr>\n'
    ratingListContent += '<td colspan = "3"><a href = "/assignment3/" class = "button">Return to the list</a></td>\n'
    ratingListContent += '</tr>\n'
    ratingListContent += "</table>"
    return htmlify("Ratings", ratingListContent, CSS())
    # Lastly buttons are printed and the rating list is done


route('/rating_list/', 'GET', rating_list)


def comments():  # Valid HTML
    # Defining a function to make users able to leave comments.
    html = """<h2>Leave a comment to us!</h2>
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

    return htmlify("Comments", html, CSS())  # Returning htmlified content.


route('/comments/', 'GET', comments)  # Routing...


def comment_sent():  # Valid HTML
    # Defining a function to get data with post method.
    global posted_comments
    # Making variables global to access them in another function.
    comment_data = request.POST
    # Data is reached.
    posted_comments += [{'name': comment_data['nick'],
                         'comment': comment_data['comment']}]
    # Data is saved.
    comment_sent_content = '<h1>Your comment successfully sent!</h1>\n'
    comment_sent_content += '<table>\n'
    comment_sent_content += '<tr>\n'
    comment_sent_content += '<td><a href="/comment_list/" class = "button">Click to see other comments</a></td>\n'
    comment_sent_content += '<td><a href="/assignment3/" class = "button">Click to go to the main page</a></td>\n'
    comment_sent_content += '</tr>\n'
    comment_sent_content += '</table>\n'
    # Information and links to Home Page and Comment List.
    return htmlify("Comment Sent!", comment_sent_content, CSS())  # Returning htmlified content.


route('/comment_sent/', 'POST', comment_sent)  # Routing...


def comment_list():
    global posted_comments

    # Defining a function to list all comments and names.
    comment_content = '<table class = "music">\n'
    comment_content += '<tr>\n'
    comment_content += '<th>Name/Nickname</th>\n'
    comment_content += '<th>Comment</th>\n'
    comment_content += '</tr>\n'

    # A table element is created.
    for comment in posted_comments:
        comment_content += '<tr>\n'
        comment_content += '<td>' + comment['name'] + '</td>\n'
        comment_content += '<td>' + comment['comment'] + '</td>\n'
        comment_content += '</tr>\n'

    comment_content += '</table>\n'
    # Adding comments and names as table data.
    comment_content += """<table><tr>
    <td><a href="/assignment3/" class = "button">Click to go to the main page</a></td>
    <td><a href="/comments/" class = "button">Click to add a comment</a></td></tr></table>"""
    # End of html content, with a closing tag and two links, one goes to Home Page and one goes to comment adding page.

    return htmlify("Comment List", comment_content, CSS())  # Returning htmlified content.


route('/comment_list/', 'GET', comment_list)  # Routing...


def filter_category():
    global songs
    genres = []
    filter_content = '<h3>You can choose below categories for filter:</h3>\n'
    filter_content += '<form method="post" action="/filter_results/" id="comment">\n'
    filter_content += '<table>\n'
    for song in songs:
        if song['genre'].title() not in genres:
            genres += song['genre'].title()
            filter_content += '<tr><td><input type="checkbox" name="' + song['genre'].title() + '" value="' + \
                              song['genre'].title() + '"></td><td>' + song['genre'].title() + '</td></tr>\n'

    filter_content += '<tr><td><input type="submit" value="Filter Song Categories" ' \
                      'class="button"></td>\n'
    filter_content += '<td><a href = "/assignment3/ class = "button">Return to the list</a></td></tr>\n'
    filter_content += '</table>\n'
    filter_content += '</form>\n'
    return htmlify("Filter", filter_content, CSS())  # Returning htmlified content.


route('/filter_category/', 'GET', filter_category)  # Routing...


def filter_results():
    global songs
    selected_genre = request.POST
    filter_content = '<table class="music">\n'
    filter_content += '<tr>\n'
    filter_content += '<th>Name</th>\n'
    filter_content += '<th>Year</th>\n'
    filter_content += '<th>Album</th>\n'
    filter_content += '<th>Band</th>\n'
    filter_content += '<th>Genre</th>\n'
    filter_content += '</tr>\n'

    for filter_genre in selected_genre:
        for song in songs:
            genre = song['genre']
            if filter_genre == genre:
                filter_content += "<tr>\n"
                filter_content += "<td>" + song['name'] + "</td>\n"
                filter_content += "<td>" + str(song['year']) + "</td>\n"
                filter_content += "<td>" + song['album'] + "</td>\n"
                filter_content += "<td>" + song['band'] + "</td>\n"
                filter_content += "<td>" + song['genre'] + "</td>\n"
                filter_content += "</tr>\n"
    filter_content += '</table>\n'
    filter_content += '<a href = "/assignment3/" class = "button">Click to go to the main page</a>\n'
    return htmlify("Results", filter_content, CSS())


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
