non_url_safe = ['"', '#', '$', '%', '&', '+',
                    ',', '/', ':', ';', '=', '?',
                    '@', '[', '\\', ']', '^', '`',
                    '{', '|', '}', '~', "'"]

def slugify(text):
    non_safe = [character for character in text if character in non_url_safe]
    if non_safe:
        for i in non_safe:
            text = text.replace(i, '')
    text = u'-'.join(text.split())
    return text

text = input("Enter the text to slugify >>> ")
slug = slugify(text)
print("Slugified text:   ",slug)