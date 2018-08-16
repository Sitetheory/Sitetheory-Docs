########
Overview
########

Our Standards are carefully established to provide a decrease in faux pas while increasing legibility, maintainability, and scalability.

Symfony Framework
=================

Symfony is an MVC framework we utilize to maintain optimal abstract logic.  The internal application kernel maintains requests, responses, and configurations, then sends this information off to a Controller for business logic.  Any common routines utilize dependency injection for optimal usage.  With that in mind, we utilize controllers, services, and bundles based on particular feature sets to maintain a modular design.  The only bundle that we have dependence on, at this time, is the CoreBundle.  This may change down the road as more of these pieces get fragmented out.

Doctrine ORM
============

You may ask yourself, what is an ORM?  For that I say, an Object Relational Manager is a system that maintains object persistence without directly querying and storing each property and their constraints separately.  They also allow the use of multiple querying languages to handle said persistence.

Release Cycles
==============

We use `Semantic Versioning`_ to determine when and how to set version numbers.

Sitetheory API
==============

Everything in the API is handled from a payload, which can sometimes contain an outer object, we call the Convoy.  The Convoy may contain a `route` and/or `meta`, which will cause the payload to become nested a level deeper.  For example, this would look like so:

.. code-block:: json
    {
        "route": {
            "controller": "User"
        },
        "meta": {
            "method": "get",
            "status": [
                {
                    "code": "SUCCESS",
                    "message": "Successfully executed request."
                }
            ]
        },
        "payload": [
            {
                "id": 1,
                "username": "Plato",
                "email": "plato@epistemology.edu"
            },
            {
                "id": 2,
                "username": "Aristotle",
                "email": "aristotle@metaphysics.edu"
            },
            {
                "id": 3,
                "username": "Socrates",
                "email": "socrates@maieutics.edu"
            },
            {
                "id": 4,
                "username": "Nietzsche",
                "email": "friedrich@nihilism.org"
            },
            {
                "id": 5,
                "username": "Kierkegaard",
                "email": "søren@existence.net"
            }
        ]
    }

The `route` contains information for where the payload needs to go, whether it be a `controller`, `user`, or some other destination.  If this is filled out by using a `RESTful` request like `/Api/User`

The `meta` always contains a `method` and `status`, at the very least.  The methods are `get`, `set`, `new`, and `del`.  These can also be set by using a `RESTful` interface of `GET`, `PUT`, `POST`, and `DELETE`, respectively.  There is also a `PATCH` option, but it is synonymous with `PUT`, as they are both designed to be a patchable request.  The `status` should not be set unless we encounter an error.  If nothing fails at the time of serialization, the system will automatically place a `SUCCESS` status into the correlating array.  There may be other bits of information inside the `meta` as required by the destination.

.. _Semantic Versioning: http://semver.org/spec/v2.0.0.html