import subprocess
email = 'sankalp123427@gmail.com'
subject = 'hello'
message = 'hello world'
subprocess.run(["python", "email_test.py",email, subject, message])
