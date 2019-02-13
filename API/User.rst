####
User
####


Overview
========

To see all fields that you have access to read and edit, do a generic call to the API.

SECURITY: All API calls should be to the HTTPS (SSL enabled) version of the URL (so you do not send information in plain text).



API
===
/Api/User


Examples
========

Login
-----
Method: POST
URL: /Api/Login

.. code-block:: javascript
    :caption: Body

    {"email":"foo@bar.com","password":"abcd1234"}


Update Password (or any other field)
-----
Method: PUT
URL: /Api/User/{ID}

.. code-block:: javascript
    :caption: Body

    {"password":"abcd1234"}

Note: Only the user has permission to reset their own password.

