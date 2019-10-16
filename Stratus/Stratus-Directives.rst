NOTE: See our :doc:`Stratus documentation </1.0/Stratus/Overview>` for an overview of how Stratus works.

##################
Stratus Directives
##################

Like Stratus Components, you can create Angular style Directives for implementing functionality that isn't a Component or a Filter.


Available Directives
====================


trigger
*********

TODO: NOTE - this does not work at the moment.

There are cases where we need to set a variable for use in other parts of the page (and ng-init is deprecated and/or doesn't have the right timing). So we can use a directive to trigger a variable to be set on `ng-model` basaed on the `stratus-trigger` expression.

Usage
-----

.. code-block:: html+twig
    :linenos:

    <span ng-model="foo"
          stratus-trigger="model.data.version.tags.length > 0 ? 'tags' : 'manual'"
          style="display:none">
    </span>
    <md-select ng-model="foo" flex>
        <md-option value="manual">Curated Content</md-option>
        <md-option value="tags">Tags</md-option>
    </md-select>


