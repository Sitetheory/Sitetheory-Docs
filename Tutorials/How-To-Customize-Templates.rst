##########################
How to Customize Templates
##########################

Modify Body Tag
---------------

You can modify the template `<body>` tag by extending the block or adding attributes to the view.body.attributes object (required if you want to merge with existing attributes like class).

**Add Attributes Directly**
{% block bodyAttributes %}
    {{ parent() }}
    data-spy="scroll" data-target="#mainNavigationContainer
{% endblock bodyAttributes %}

**Modify Existing Body Attributes without Overwriting, e.g. class**
{% block bodyAttributes %}
    {% set bodyAttributes = bodyAttributes|merge({'class':'foobarstache'}) %}
    {{ parent() }}
{% endblock bodyAttributes %}



