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
def home(request):
    # Create a dictionary called 'context' to pass data to the template.
    context = {
        # Pass the 'posts' list to the template under the key 'posts'.
        'posts': posts
    }
    # Render the 'home.html' template and pass the 'context' dictionary.
    # The 'request' object is necessary for rendering.
    # The 'EncryptNotes/home.html' string specifies the template file's path.
    return render(request, 'EncryptNotes/home.html', context)

# Define the view function for the about page.
def about(request):
    # Render the 'about.html' template and pass a dictionary with the title.
    # The 'request' object is necessary for rendering.
    # The 'EncryptNotes/about.html' string specifies the template file's path.
    # {'title': 'About'} is a dictionary that passes the string "About" to the template with the key "title".
    return render(request, 'EncryptNotes/about.html', {'title': 'About'})