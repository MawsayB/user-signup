from flask import Flask, request, redirect, render_template
import cgi 
import os

app = Flask (__name__)
app.config['DEBUG'] = True

@app.route('/signup')
def display_signup_form():
    return render_template('homepage.html', username='', username_error='', 
    password='', password_error='', ver_password='', 
    ver_password_error ='', email='', email_error='')

@app.route('/signup', methods=['POST'])
def validate_signup():
    username = request.form['username']
    password = request.form['password']
    ver_password = request.form['ver_password']
    email = request.form['email']

    username_error=''
    password_error=''
    ver_password_error=''
    email_error=''

    if len(username) == 0:
        username_error = 'Please enter a username.'
    if len(username) >= 1 and len(username) < 3 or len(username) > 20:
        username_error = 'Your username should be 3-20 characters in length. Please try again.'
    if username.find(' ') >= 1:
        username_error = 'Please remove space(s).' 

    if len(password) == 0:
        password_error = 'Please enter a password.'
    if len(password) >= 1 and len(password) < 3 or len(password) > 20:
        password_error = 'Please re-enter a password that is 3-20 characters long.'
    if password.find(' ') >= 1:
        password_error = 'Please remove space(s).'

    if len(ver_password) == 0:
        ver_password_error = 'Please verify your password.'
    if ver_password != ver_password.replace(ver_password, password):
            ver_password_error = 'Passwords do not match.'

    if len(email) != 0:
        if len(email) <3 or len(email) >20:
            email_error = 'Please double-check your email address. Email should be 3-20 characters in length.'
        if '@' not in email or ' ' in email or '.' not in email:
            email_error = 'Check format for @ symbol, period, and no spaces.' 
        
    if not username_error and not password_error and not ver_password_error and not email_error:
        return render_template('welcome.html', username=username)

    else:
        return template.render(username=username, username_error=username_error, password='', 
        password_error=password_error, ver_password='', 
        ver_password_error=ver_password_error, email=email, email_error=email_error)       

app.run()