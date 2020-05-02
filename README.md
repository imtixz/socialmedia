# socialmedia
A django project with an account management app. It can be used like a basic social media template. 

Installation:
1. Clone or download the code.
2. Go to social > settings.py and change a few thing:
 a. Generate and enter a secret key in string format
 b. Go to the bottom of the settings.py and enter your gmail id and password (this is for sending emails when someone resets their password. Note that you will have to turn on access from unsafe apps in your gmail account's settings.

Features:
1. User Registration.
2. User Login and Logout.
3. Individual User Profile (with their usernames on the link)
4. Ability to edit user profiles.
5. A password reset functionality that sends an email to the user through the gmail account that you provide.

Credits:
The entire django project is very similar to the django tutorial by Corey Schafer on Youtube. There are slight modifications in this project. But you can learn most of what I did here if you follow his tutorial.
