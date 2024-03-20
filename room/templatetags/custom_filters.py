from django import template

register = template.Library()

@register.filter
def image_extension(filename):
    valid_extensions = ['jpg', 'jpeg', 'png', 'gif', 'bmp']
    file_extension = filename.split('.')[-1].lower()
    # print(file_extension)
    # print(file_extension in valid_extensions)
    return file_extension in valid_extensions