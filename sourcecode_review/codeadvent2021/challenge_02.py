import os

from django.http import HttpResponse

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def get_image(request):
    filename = request.POST['img']
    file_path = os.path.join(BASE_DIR, "uploads", filename)
    if file_path.find(".") != -1:
        return HttpResponse("Failed!")
    else:
        with open(file_path) as f:
            return HttpResponse(f.read(), content_type='image/png')

"""
# Link
https://twitter.com/SonarSource/status/1466437008520192000/photo/1

# Issues
Arbitrary file read - os.path.join() can take an absolute file path (e.g., /etc/passwd) from the 'img' parameter as the filename. The official Python document (https://docs.python.org/3/library/os.path.html?highlight=thrown%20away#os.path.join) stated that if os.path.join() sees an absolute file path, it will ignore any previous values.

For example, 
```
>>> import os
>>> os.path.join('/bigb0ss', '/etc/passwd')
'/etc/passwd'
```

# Mitigation
- Sanitize the user supplied filename not to contain special characters like "/" 
"""