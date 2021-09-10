import jwt

priv = b'-----BEGIN RSA PRIVATE KEY-----\nMIICXwIBAAKBgQDirM9ptLf7sdpQQFJ7EI7+j1jRJ79YF04Gj90YrqBi7wU0TzM0\nNCC/T9SLK/KI9taf+AEVOMdIdH1E8/7xRAhxQIwzcEeYtgnb6NOJN0tlvplw5Za0\niNvVbmWshRZzHRyivgexQfg7QKShGwIKhPkWsuGYELc8/dvBpIBfGGcjmwIDAQAB\nAoGBAI/TFFu+1go2pA3NckgxjnmInNNBBBCx4MkbGS9jBdMgU84H/rY96RVaYsLX\nZLFw5Wdk5dMATrnzZ9SLeJS/FRcNIuxDip6INPyNx9HyyKcMp+K8E38d4BXRpDMf\nxvZz6g9IrwUkU43nASztcVVbJHJfWIOw4zDjEn9X39WaSHVBAkEA9Fg2mOk9QieU\nvb6P5yzpIskbje7WXP2FwcjrAXG929GLenpmkoOb3ee3p2Df7f8+bUiMPWfX9hEd\nzI9ADLaK4QJBAO1808gZ/YnXJ6lVlJXDJukCQlHJjFH7L7sHySRhGoWVK03t/zfz\nO6F28f4u2zTpmFIjmErsPd5CJQ6fIL59GfsCQQDTGzvglPM2KthZr0DJLIYoZbSG\nxikyol9j8+EGmGy+dKabJRFl2ItcB40m8Y3HJFWdOabgjs2JbXRffgyKb1RBAkEA\nzuVr/60c4+RMikqjeuGcWWz9aBFlrNpfl9pNkuMB3xS4uFi6evztm1prsp0RngRQ\nDmcyOzubHrGTZSyeszV71wJBALsgFoeieVHqbvI+AMIu8W+gq9wqpeUyzs+AaX0I\n8c1bayhxaNkRkXjx1A6Y3DpHqtf3pjeDH8gDNs+zflAIJK0=\n-----END RSA PRIVATE KEY-----\n'

with open('./public.pub', 'rb') as f:
   PUBLIC_KEY = f.read()


# print(priv.decode('utf-8'))
encoded = jwt.encode({'username': 'admin', 'admin': 'True'}, key=PUBLIC_KEY)
print(encoded)