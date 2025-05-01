from google.cloud import language_v1
from django.conf import settings
from django.utils.html import strip_tags

AUTH_KEY = settings.GOOGLE_KEY

#Categorizes a note based on its content
#content: the string of the content of the note to categorize
#returns: the string of the name of the category of the note
def categorize_note(content):
    client = language_v1.LanguageServiceClient.from_service_account_json(AUTH_KEY)
    cleanContent = strip_tags(content)
    shortContent = cleanContent.strip()
    
    #Prevent uneccessary API calls
    if len(cleanContent.split()) < 20:
        print(cleanContent.split())
        return "Uncategorized"
        
        
    document = language_v1.Document(
        content=cleanContent,
        type_=language_v1.Document.Type.PLAIN_TEXT
    )
    response = client.classify_text(request={"document": document})
    if response.categories:
        print("Category Detected:", response.categories[0].name) #debugging output
        return response.categories[0].name
    else:
        print("No category detected.") #Debugging output
        return "Uncategorized"