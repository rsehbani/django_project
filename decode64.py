

import base64

encoded_data = b"e30:1vZc5m:C_O9bPpo0Bz8gez-2O3_7reKfE75rFOqPd1RjZef3UY"
# Calculate the correct padding length and add it
# This formula always yields 0, 1, or 2, which b64decode handles correctly
# because the default validate=False truncates extra padding
padded_data = encoded_data + b'=' * ((4 - len(encoded_data) % 4) % 4)

decoded_data = base64.b64decode(padded_data)
print(decoded_data)

print('---------------------------------------')
"""

encoded_data = b"eyJ2aXNpdCI6Mn0:1vZ4Jo:2aaipybo1eVWb3p4BKHuUO6EhW59kt8KLpcNFnvNxa4"
# Calculate the correct padding length and add it
# This formula always yields 0, 1, or 2, which b64decode handles correctly
# because the default validate=False truncates extra padding
padded_data = encoded_data + b'=' * ((4 - len(encoded_data) % 4) % 4)

decoded_data = base64.b64decode(padded_data)
print(decoded_data)

print('---------------------------------------')

encoded_data = b"eyJ2aXNpdCI6MX0:1vZbR9:wlVQxl1J7LwhzyDvNMyJ76G5q1y1EZJg12HMzXO95T0"
# Calculate the correct padding length and add it
# This formula always yields 0, 1, or 2, which b64decode handles correctly
# because the default validate=False truncates extra padding
padded_data = encoded_data + b'=' * ((4 - len(encoded_data) % 4) % 4)

decoded_data = base64.b64decode(padded_data)
print(decoded_data) """