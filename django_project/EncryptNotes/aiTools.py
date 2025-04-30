from google.cloud import language_v1

AUTH_KEY = "winter-rider-457017-i2-28a007db513f.json"

#Categorizes a note based on its content
#content: the string of the content of the note to categorize
#returns: the string of the name of the category of the note
def categorize_note(content):
    client = language_v1.LanguageServiceClient.from_service_account_json(KEY_PATH)
    document = language_v1.Document(
        content=content,
        type_=language_v1.Document.Type.PLAIN_TEXT
    )
    response = client.classify_text(request={"document": document})
    if response.categories:
        return response.categories[0].name
    else:
        return "Uncategorized"