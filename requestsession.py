
# Source - https://stackoverflow.com/a/18560516
# Posted by Nickl
# Retrieved 2025-12-27, License - CC BY-SA 3.0

# importing the libs
from http import cookies
import os

# setting the cookies
C = cookies.SimpleCookie()
C["cookie1"] = "some_text"
C["cookie2"] = "another_text"
print(C.output())

