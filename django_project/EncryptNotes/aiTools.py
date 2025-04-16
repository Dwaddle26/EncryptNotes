from google.cloud import language_v1

def categorize_note(content):
    client = language_v1.LanguageServiceClient()
    document = language_v1.Document(
        content=content,
        type_=language_v1.Document.Type.PLAIN_TEXT
    )
    response = client.classify_text(request={"document": document})
    if response.categories:
        return response.categories[0].name
    else:
        return "Uncategorized"