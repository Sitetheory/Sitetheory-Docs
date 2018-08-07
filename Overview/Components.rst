##########################
Introduction to Components
##########################

Sitetheory is designed to make it easy for designers to create beautiful websites that are highly interactive and functional. We wanted to separate design and code as much as possible, so that a designer could easily build HTML/CSS without having to stumble around intimidating code. And yet, we want to allow hard core developers unlimited creativity to implement complex javascript if necessary. To make this possible, we've adopted the Angular framework (full MVC) which has a great templating system for designers, with beautiful pre-built components for the most common use cases and a few components of our own for our custom needs. Then either the designer or a programmer can add logic to their design using Angular syntax, pull dynamic data from APIs, and create a rich experience. At any time the designer can go into an existing dynamic page, and easily edit the design without being too concerned about creating development bugs. If a developer needs to implement complex features, they have full access to the javascript through our Stratus framework, or they can use require.js to require third party libraries and implement any feature they want.

A component could be a simple display field to show the value of an entity, a text field that allows editing the value of an entity property, or it can be like a complex media selector that shows you all the elements you have selected and allows you to upload or select new media. Components render a template and add functionality to the page so the designer can control the user experience. Most components are set to auto-save changes, so the experience is much more responsive than traditional forms. Components are used extensively throughout the CMS admin and Live Edit mode.


#######
Angular
#######

Sitetheory implements `Angular 1 <https://angularjs.org>`_ to display and edit data on any website. `Angular's Material.js <https://material.angularjs.org>`_ also provides a lot of prebuilt components, general CSS and a Javascript framework to help rapid development and a general base for creating interactive sites. Generally speaking, Angular replaces Bootstrap and jQuery.

#######################
Implementing Components
#######################


*****************
Component Options
*****************

In addition to all the standard Angular options, the following options are the most common basic options used in our system.

* **ng-controller** (*string:required*) This tells Angular to use our standard `Generic` controller which fetches and binds the models to the current scope, e.g. `ng-controller="Generic"`. This standard `Generic` controller is good enough for most situations, but if you need a fully custom implementation, you can declare one in a `<script>` tag above (see example below).

* **data-target** (*string:required*) This is the name of the entity that the RESTful API will target, e.g. `User`.

* **ng-model** (*string:required*) This is the property that is being edited, e.g. `model.data.name`

* **data-api** (*json:optional*) This is an optional json array of settings that will be passed to the API via the Convoy's Meta property, e.g. `data-api='{"options":{"showRouting":true}}'`.

******************************
Component Properties Available
******************************

Inside an Angular controller scope the following objects, methods and properties can be accessed, e.g. `<span>{{ model.data.name }}</span>`

* **collection** (*object*) This is an object that is returned from the API when no specific ID is requested. It contains various methods and properties, including an array of models.
* **collection.meta** (*object*) This is meta data that was returned from the API with important information about the entity.
* **collection.models** (*array*) This is an array of models returned for a collection. The structure of each model is the same as when an individual model is returned
* **model**(*object*) This is an object that is returned from the API when a specific ID is requested. It shares the same data structure as an individual model inside a `collection.models`. It contains methods (e.g. save, fetch, sync) and all the `data` for the model's properties.
* **model.save** (*method*) Initiate this method to save a model.
* **model.fetch** (*method*) Initiate this method to refetch/refresh the model.
* **model.sync** (*method*) This is the manual method to interact with the API (not recommended). Save and Fetch use this method internally.
* **model.data** (*object*) This is where all the data for the model resides.


*************
Example: List
*************

NOTE: below is sample HTML, but a lot of the outer HTML is reusable in Twig by extending the ListBase. The raw HTML will be shown first so you understand the big picture, and the Twig implementation will be shown second if you want .


HTML
----

.. code-block:: html+twig
    :linenos:

    <!-- The ng-controller is the name of the API that will be called, e.g. ListApiController -->
    <md-list ng-controller="Generic"
    data-target="User" data-api='{"options":{"limitContext":true, "showProfile":true, "showMailLists":true}}'
    layout-padding ng-cloak>

        <!-- Proggress Bar -->
        <md-progress-linear ng-if="collection.pending" md-mode="indeterminate"></md-progress-linear>

        <!-- Header -->
        <div layout="row">
            <div flex="5"></div>
            <div flex><h2>Name</h2></div>
            <div flex><h2>Profile</h2></div>
            <div flex><h2>Permissions</h2></div>
        </div>

        <!-- List Body with Repeating Rows -->
        <md-list-item
            ng-repeat="model in collection.models"
            layout="row"
            layout-xs="column"
            layout-sm="column"
            layout-align="space-between center"
            layout-wrap>

            <div flex="5">
                <md-button href="{{ collection.meta.attributes.editUrl }}?id={{ model.data.id }}" aria-label="edit" class="md-fab md-primary md-mini white-svg">
                    <md-icon md-svg-src="/Api/Resource?path=@SitetheoryCoreBundle:images/icons/actionButtons/edit.svg"></md-icon>
                </md-button>
            </div>

            <div class="user" layout="column" flex>
                <h4><a href="{{ collection.meta.attributes.editUrl }}?id={{ model.data.id }}">{{ model.data.bestName }}</a></h4>
                <!-- Convert unix timestamp to readable date -->
                <div>Created {{ model.data.time*1000 | date:'medium' }}</div>
            </div>

            <div class="profile" layout="column" flex>
                <div>
                    <span ng-if="model.data.profile.lookupValues.gender">{{ model.data.profile.lookupValues.gender }}</span>
                </div>
                <div ng-if="model.data.profile.mailLists.length > 0">
                    <span ng-repeat="mailList in model.data.profile.mailLists">{{ mailList.name }}<span ng-if="!$last">, </span></span>
                </div>
            </div>

            <div class="permissions" layout="column" flex>
                {{ model.roles.join(', ') }}
            </div>

            <md-divider md-inset ng-if="!$last"></md-divider>

        </md-list-item>
    </md-list>



TWIG
----

.. code-block:: html+twig
    :linenos:

    {% extends 'SitetheoryCoreBundle:Core:ListBase.html.twig' %}
    {% set stratusTarget = 'User' %}
    {% set stratusApi = '{"options":{"limitContext":true, "showProfile":true, "showMailLists":true}, "q":"foo"}' %}
    {% block listHeader %}
        <!-- HTML header-->
    {% endblock listHeader %}
    {% block listRow %}
        {% verbatim %}
        <!-- HTML for individual repeating rows with access to the `model` data -->
        <div><a href="{{ collection.meta.attributes.editUrl}}?id={{ model.data.id }}">Edit</a></div>
        <div>{{ model.data.bestName }}</div>
        {% endverbatim %}
    {% endblock listRow %}


Javascript
----------
If you need to define custom functionality, you can easily create a custom controller that utilizes the services of the
default `Generic` controller. Then you either define the `ng-controller` manually, or if you are using the ListBase, you can
define your own controller, e.g.:

.. code-block:: html+twig
    :linenos:

    {% set stratusController = 'FooController' %}`
    {% block script %}

        {{ parent() }}

        <script>
        (function (root, factory) {
            if (typeof require === 'function') {
                require(['stratus'], factory);
            } else {
                factory(root.Stratus);
            }
        }(this, function (Stratus) {
            Stratus.Events.on('initialize', function () {
                Stratus.Apps.Generic.controller('FooController', function ($scope, $element, registry) {
                    // Make API call to the target entity (registry prevents duplicate calls)
                    $scope.registry = new registry();
                    // digests the HTML $element to find the data attributes defining the options
                    $scope.registry.fetch($element, $scope);

                    // CUSTOM CODE BELOW HERE------------------

                    // Make a Custom API call to some other User entity...
                    // NOTE: there is no $scope passed in the fetch options, but we define entity in $scope so {{ user }} can
                    // be referenced in the angular HTML.
                    $scope.user = $scope.registry.fetch({
                        // API Entity (required)
                        target:"User",
                        // Fetch one specific ID (optional)
                        id:1,
                        // Call the API and fetch an object on load (so you can save) (optional)
                        manifest: false,
                        // Specify if the results should be stored in the registry (in case you need something unique
                        decouple: true
                    });
                });
            });
        }));
        </script>

    {% endblock script %}


*************
Example: Edit
*************

.. code-block:: html+twig
    :linenos:

    <!-- Targeting the Article entity API for the specified ID -->
    <div ng-controller="Generic"
        data-target="Article"
        data-id="35558"
        data-manifest="true"
        layout-padding ng-cloak>

        <div layout="row" layout-xs="column" layout-sm="column" layout-align="space-between center" layout-wrap>

            <md-progress-linear ng-if="model.pending" md-mode="indeterminate"></md-progress-linear>

            {# Example: define variable for this scope #}
            <div flex="5"></div>
            <md-input-container flex="95" ng-show="model.completed">
                <!-- set a variable unconnected to the model -->
                <md-switch ng-model="showHints">Hints</md-switch>
            </md-input-container>

            {# Example: listen to defined variable for this scope #}
            <div class="hint" ng-show="showHints" flex="100">
                This hint will show when showHints switch is true.
            </div>

            {# Example: help and generic input #}
            <stratus-help flex="5">Lorem ipsum dolor sit amet.</stratus-help>
            <md-input-container flex="95" ng-show="model.completed">
                <label>Title</label>
                <input ng-model="model.data.contentVersion.title" type="text" required>
            </md-input-container>

            {# Example: basic date picker #}
            <div flex="5"></div>
            <md-input-container flex="95" ng-show="model.completed">
                <label>Display Date</label>
                <md-datepicker ng-model="model.data.contentVersion.timeCustom"></md-datepicker>
            </md-input-container>

            {# Example: Select with options hydrated from API #}
            <div flex="5"></div>
            <md-input-container flex="95" ng-show="model.completed">
                <label>Genre</label>
                {% verbatim %}
                <md-select
                    ng-model="model.data.genre.id"
                    ng-controller="Generic"
                    data-target="SiteGenre"
                    md-model-options="{trackBy: '$value.id'}"
                    required>
                    <md-option ng-repeat="option in collection.models" ng-value="option.data.id">{{ option.data.name }}</md-option>
                </md-select>
                {% endverbatim %}
            </md-input-container>

            {# Example: auto-complete with chips #}
            <div flex="5"></div>
            <md-input-container flex="95" ng-show="model.completed">
                <md-chips
                ng-model="model.data.profile.mailLists"
                md-removable="true"
                placeholder="Add Mailing List"
                flex="100">
                    {% verbatim %}
                    <md-chip-template class="mailList">{{ $chip.name || $chip.data.name }}</md-chip-template>
                    <md-autocomplete
                        md-items="mailList in mailLists.filter(query)"
                        md-item-text="mailList.data.name"
                        md-selected-item="selected"
                        md-search-text="query"
                        md-min-length="0"
                        md-no-cache="true"
                        placeholder="Pick a Mailing List">
                        <md-item-template>{{ mailList.data.name }}</md-item-template>
                        <md-not-found>No Mailing Lists Found...</md-not-found>
                    </md-autocomplete>
                    {% endverbatim %}
                </md-chips>
            </md-input-container>

            {# Example: Froala text editor #}
            <div flex="5"></div>
            <md-input-container flex="95" ng-show="model.completed">
                <label>Body</label>
                {# leave `froala` attribute empty to use default, provide value "froalaOptions" to use Stratus defaults, or pass in a JSON attribute of valid Froala options from their documentations #}
                <textarea froala="froalaOptions" ng-model="model.data.contentVersion.text"></textarea>
            </md-input-container>

            {# Example: Autosave is enabled by default in most contexts, but if you need to manually save the model you can do it this way #}
            <md-button aria-label="save" class="md-raised md-primary white-svg" ng-show="model.completed" ng-click="model.save()">Save</md-button>
        </div>
    </div>



############
# VALIDATION
############

The `validate` directive enhances `Angular's internal form<https://docs.angularjs.org/guide/forms>`_ by using the `Angular ngMessages<https://docs.angularjs.org/api/ngMessages/directive/ngMessages>`_ system to allow custom validation in addition to the Angular defaults validation like `required`, `min`, `max`, `email`, etc. This `validate` directive adds several new validation methods that can be triggered for inputs by including the requirements as options.

- string|array `validateInvalid` One or more invalid values not allowed. Can include scope variables that will be evaluated, e.g. `validate-invalid='[model.data.nominatorName, "foo"]'`
- string|array `validateValid` One or more values that are valid.
- string `validateComparison` A scope variable comparison that will be evaluated, e.g. `model.data.nominatorName != model.data.nomineeName`. NOTE: if the comparison value evaluates the current model value, e.g. model.data.nomineeName this is evaluates after the viewValue is updated but BEFORE the model is updated, so it won't work with the timing.

The ng-message validate key will be set if a specific validation fails. If more than one validation scheme is set, we will also show if any of them fail:
- `validateComparison`: if the comparison was false.
- `validateInvalid`: if an invalid value was provided.
- `validateValid`: if a valid value was not provided.
- `validateAny`: if any of the validations fail.

Example:

::

    <input name="nomineeName" ng-model="model.data.fooName" placeholder="" required stratus-validate validate-comparison="model.data.foo != model.data.bar" validate-invalid="['baz', 'rab']">
        <div ng-messages="Nominate.nomineeName.$error" ng-messages-multiple role="alert">
        <div ng-message="required">Please enter a name.</div>
        <div ng-message="validateComparison">Please do not nominate yourself.</div>
        <div ng-message="validateInvalid">Baz and Rab are not valid values.</div>
        <div ng-message="validateAny">Ya you really messed up.</div>
    </div>


#################
Custom Components
#################

See the `Stratus Documentation <http://js.sitetheory.io/1/0/stratus.html>`_ for detailed specs of each component.



****************
`<stratus-help>`
****************

Add a "Help" icon that reveals more information on hover.

Example
-------

.. code-block:: html
    :linenos:

    <stratus-help flex="5">This field allows you to explain how awesome you are.</stratus-help>


************************
`<stratus-option-value>`
************************

Add different types of dynamic fields that allow you to enter a value and select a label to describe what knd of infromation this is, e.g. an email field, that lets you select "Main", "Work", "Personal" or enter your own custom label.

Options
-------

* **data-type** (*string*): a string of one of the valid field types. A valid field type will add special styling, functionality, and validation relevant to that type of data. Valid options include: "phone", "email", "url", "location", "date". If no valid type is specified it will just be a simple field.
* **data-options** (*array: required*) an array of labels to choose from for this field e.g. ["Main", "Mobile", "Work", "Personal"]
* **data-custom** (*boolean*): specify `true` if you want users to be able to enter a custom value for the label. (*default: true*)
* **data-multiple** (*boolean*): specify `true` if you want users to be able to add more than one version of this type of field, e.g. multiple phone numbers. (*default: true*)

Additional Features for Type
----------------------------

- location: when saved, a location will attempt to do a geolocation lookup and store the latitude/longitude of the address.


Example
-------

.. code-block:: html
    :linenos:

    <stratus-option-value flex="95" ng-show="model.completed"
        ng-model="model.data.contentVersion.meta.phones"
        data-options='["Main", "Mobile", "Work", "Personal"]'
        data-type="phone"
        data-custom="true"
        data-multiple="true">
    </stratus-option-value>


Backend Info
------------

The label/value pairs are stored in the AssetManager, which allows for multiple dynamic fields to be attached to any entity.