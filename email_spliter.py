# Locate spcific index position
from unittest.mock import DEFAULT

from pygments.lexer import default

email='code@gmail.com'
# print(email.index('@'))

# Print whats in front of @ which is user name
print(email[0:email.index('@')])
# If you dont have 0 then default is from 0
print(email[:email.index('@')])
# DEFAULT to the end
print(email[email.index('@') + 1:])