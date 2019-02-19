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
    :caption: API POST Body

    {"email":"foo@bar.com","password":"abcd1234"}


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

-`email` (string) - You must provide an email (for account verification email)
-`profile.phones` (array with object values) - You must provide a phone for password resets.

.. code-block:: javascript
    :caption: API Post Body

    {
        "email":"foo@bar.com",
        "profile": {
            "phones":[{"type":"phone","name":"Mobile","value":"9251231234"}]
        }
    }



**Other Fields:**
-facebookId, googleId, twitterId: these are IDs obtained by doing single-signon verification with these users approving your app and being given a login id by Facebook, Google, Twitter, etc.

.. code-block:: javascript
    :caption: API Post Body

    {
        "email":"foo@bar.com",
        "username":"chadwick",
        "facebookId":"",
        "googleId":"",
        "twitterId":null,
        "profile": {
            "publicName":"The Boss",
            "position":null
            "birthday":277171200,
            "gender":2,
            "relationshipStatus":null,
            "ageGroup":4,
            "zip":"44444",
            "mailLists":[],
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
            "dates":[{"type":"date","name":"Mobile","value":"9251231234"}],
            "phones":[{"type":"phone","name":"Mobile","value":"9251231234"}],
            "emails":[{"type":"email","value":"foo@bar.com","name":"Work"}],
            "locations":[{"type":"location","name":"Office","value":"100 HQ Drive"}],
            "urls":[{"type":"url","name":"Website","value":"https://sitetheory.io"}],
            "socialUrls":[{"type":"social","name":"Instagram","value":"instagram.com/testing"}],
        }
    }



Update User
-----
Method: PUT
URL: /Api/User/1

.. code-block:: javascript
    :caption: API Post Body

    {
        "email":"foo@bar.com",
        "profile": {
            "phones":[{"type":"phone","name":"Mobile","value":"1112223333"}]
        }
    }

