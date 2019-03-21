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



Update Password (or any other field)
-----
Method: PUT
URL: /Api/User/{ID}

.. code-block:: javascript
    :caption: API PUT Body

    {"password":"abcd1234"}

Note: Only the user has permission to reset their own password.


Create User
-----
Method: POST
URL: /Api/User

**Required:**

- `email` (string) - You must provide an email (for account verification email)
- `phone` (string) - Phone is not technically required, but one must be provide for successful password resets.

.. code-block:: javascript
    :caption: API Post Body

    {
        "email":"foo@bar.com",
        "phone":"1112223333"
    }

NOTE: when the user is created, the system will send a verification email for the user to click a link to verify the email and also set a password.


**Other Fields:**
-facebookId, googleId, twitterId: these are IDs obtained by doing single-signon verification with these users approving your app and being given a login id by Facebook, Google, Twitter, etc.

.. code-block:: javascript
    :caption: API Post Body

    {
        "email":"foo@bar.com",
        "phone":"1112223333",
        "password":"Abcd1234",
        "username":"foobarly",
        "facebookId":null,
        "googleId":null,
        "twitterId":null,
        "settings": {
            "privateLegalName": "Mr. Foobert Barly"
        },
        "profile": {
            "publicName":"The Boss",
            "position":null
            "birthday":277171200,
            "gender":2,
            "relationshipStatus":null,
            "ageGroup":4,
            "zip":"44444",
            "mailLists":[{"id":100}],
            "meta":[],
            "units":null,
            "timezone":null,
            "lat":null,
            "lng":null,
            "tracking":[],
            "tosAccepted":[],
            "device":[],
            "ip":null,
            "id":4260,
            "dates":[{"type":"date","name":"Hired","value":"1234567890"}],
            "phones":[{"type":"phone","name":"Mobile","value":"9251231234"}],
            "emails":[{"type":"email","value":"foo@bar.com","name":"Work"}],
            "locations":[{"type":"location","name":"Office","value":"100 HQ Drive"}],
            "urls":[{"type":"url","name":"Website","value":"https://sitetheory.io"}],
            "socialUrls":[{"type":"social","name":"Instagram","value":"instagram.com/testing"}],
        }
    }



Get Roles
---------
Method: GET
URL: /Api/Role

Find the role ID you want and add to a User.



Add User to Role
----------------
Method: PUT
URL: /Api/User/1
NOTE: You must be signed in to edit a user, and have permissions to edit this user and assign this user to site roles.

.. code-block:: javascript
    :caption: API Post Body

    {
        "Role": 214
    }




Update Password
---------------
Method: PUT
URL: /Api/User/1
NOTE: You must be signed in to edit your user.

.. code-block:: javascript
    :caption: API Post Body

    {
        "password":"xxxyyyzzz3"
    }


Update User Info
----------------
Method: PUT
URL: /Api/User/1
NOTE: You must be signed in to edit your user.

.. code-block:: javascript
    :caption: API Post Body

    {
        "settings": {
            "privateLegalName":"Mr. Foobert Barly"
        },
        "profile": {
            "phones":[{"type":"phone","name":"Mobile","value":"1112223333"}]
        }
    }



Utilities
=========

Login
-----
Method: POST
URL: /Api/Login

.. code-block:: javascript
    :caption: API POST Body

    {"email":"foo@bar.com","password":"abcd1234"}


Logout
------
URL: /Api/Login?options[action]=logout

Just go to this URL to logout.


Request Password Reset
----------------------
URL: /Api/Login?options[action]=requestPassword

.. code-block:: javascript
    :caption: API POST Body

    {"email":"foo@bar.com","phone":"1234567890"}


NOTE: if you want to suppress email because your app prefers to handle the verification process itself, then you can pass in "disableEmail": true. This will cause the User account to become unverified (locked) to preventing logins. This also creates a "proposal" for the user, with a token that must be sent to the Verify Account API request in order to verify and unlock the account. So if you do this, you will need to handle verification manually by calling the "Request Proposal" API to get the

.. code-block:: javascript
    :caption: API POST Body

    {
        "email":"foo@bar.com",
        "phone":"1234567890",
        "disableEmail": true
    }


Request Proposal
----------------
URL: /Api/Login?options[action]=requestVerifyProposal

From an authenticated User account that has "dev" (64) permissions for a site, you can request a proposal for a specific user. This is used if your app needs to handle verification internally, i.e. send a custom verification email or handle verification in some other way.

**@SECURITY**: This MUST ONLY be run from a secure server (not in the app) which is able to send an verification email to the user. If you do not protect this authentication token, anyone can use it to hack a User account by sending a Verify request with this token, which will sign them in and allow them to reset a password (or change any user data).

You would send the request for a UserId, which can be found by calling the /Api/User?q={email} to lookup a user account by their email.

.. code-block:: javascript
    :caption: API POST Body

    {"userId": 1}


Verify Account
--------------
URL: /Api/Login?options[action]=verify
The token will have been returned in the Body of the "Request Password Reset" call (and also sent to the user via email).
If your app prefers to handle this, you can send this token to the API to verify. If this token is valid, it will
verify the account and log the user in.

**@SECURITY**:  the user will be signed in, and can make requests to change data (e.g. update password) through the normal /Api/User controller.

.. code-block:: javascript
    :caption: API POST Body

    {
	    "token": "5cee063a533467d244d1be7c56238bb93807de602f3aa06ea1352a20d1a86b61"
    }
