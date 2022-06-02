from urllib import request

# RESPONSE CODES
#
# 200 : OK
#
# 400 : BAD REQUEST
# 403 : FORBIDDEN
# 404 : NOT FOUND
#  .........


"""
resp.code : gives the response code
resp.peek() : Look at small part of the response 
resp.read() : it returns bytes object you need to decode to use as text
resp.isclosed() : you can see do u have still connection with the server

"""

"""
NOTICE !!! : Once you read the response python closes the connection 

"""
resp = request.urlopen("https://www.wikipedia.org")
data = resp.read()
html = data.decode("UTF-8")
print(resp.peek())