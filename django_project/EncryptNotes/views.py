from django.shortcuts import render

# Define a list of dictionaries representing blog posts.
posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Blue',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 30, 2018'
    }
]

# Define the view function for the home page.
def login(request):
    # Render the 'account.html' template and pass the 'context' dictionary.
    # The 'request' object is necessary for rendering.
    # The 'EncryptNotes/account.html' string specifies the template file's path.
    return render(request, 'EncryptNotes/account.html')

# Define the view function for the about page.
def mainpage(request):
    # Render the 'mainpage.html' template and pass a dictionary with the title.
    # The 'request' object is necessary for rendering.
    # The 'EncryptNotes/mainpage.html' string specifies the template file's path.
    # {'title': 'Main'} is a dictionary that passes the string "Main" to the template with the key "title".
    return render(request, 'EncryptNotes/mainpage.html', {'title': 'Main'})

# Define the view function for the note taking page.
def notes(request):
    # Render the 'notepage.html' template and pass a dictionary with the title.
    # The 'request' object is necessary for rendering.
    # The 'EncryptNotes/about.html' string specifies the template file's path.
    # {'title': 'About'} is a dictionary that passes the string "About" to the template with the key "title".
    return render(request, 'EncryptNotes/notepage.html', {'title': 'Notes'})
