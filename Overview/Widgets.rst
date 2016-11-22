Sitetheory is designed to make it easy for designers to create beautiful websites that are highly interactive and functional. We wanted to separate design and code as much as possible, so that a designer could easily build HTML/CSS without having to stumble around intimidating code. And yet, allow developers unlimited creativity to implement complex javascript if necessary. To make this possible, we've adopted the Angular framework (full MVC) which has a great templating system for designers, with beautiful pre-built widgets for the most common use cases and a few widgets (Directives) of our own for our custom needs. All of this allows the designer to create anything he/she wants. Then either the designer or a programmer can add logic to the page using Angular syntax, pull dynamic data from APIs, and create a rich experience. At any time the designer can go into an existing dynamic page, and easily edit the design.

A widget could be a simple display field to show the value of an entity, a text field that allows editing the value of an entity property, or it can be like a complex media selector that shows you all the elements you have selected and allows you to upload or select new media. Widgets render a template and add functionality to the page so the designer can control the user experience. Most widgets are set to auto-save changes, so the experience is much more responsive than traditional forms. Widgets are used extensively throughout the CMS admin and Live Edit mode.


#######
Angular
#######

Sitetheory implements Angular 1 (https://angularjs.org) to display and edit data on any website. Angular's Material.js (https://material.angularjs.org) also provides a lot of prebuilt widgets, general CSS and a Javascript framework to help rapid development and a general base for creating interactive sites. Generally speaking, Angular replaces Bootstrap and jQuery.

####################
Implementing Widgets
####################


**************
Widget Options
**************

In addition to all the standard Angular options, the following options are the most common basic options used in our system.

`ng-controller` (string:required) This tells Angular to use our standard StratusController which fetches and binds the models to the current scope, e.g. ng-controller="StratusController". This standard StratusController is good enough for most situations, but if you need a fully custom implementation, you can declare one in a <script> tag above (see example below).

`data-target` (string:required) This is the name of the entity that the RESTful API will target, e.g. "User".

`ng-model` (string:required) This is the property that is being edited, e.g. "model.data.name"

`data-api` (json:optional) This is an optional json array of settings that will be passed to the API via the Convoy's Meta property.


***************************
Widget Properties Available
***************************

`collection` (object) This is an object available inside a ListController, it contains methods, meta data, and an array of individual `models` (see model).

`model` (object) This is an object available inside an EditController, as well as inside a collection.models array from a ListController. It contains methods (e.g. save, fetch, sync) and all the `data` for the model's properties.


*************
Example: List
*************

NOTE: below is sample HTML, but a lot of the outer HTML is reusable in Twig by extending the ListBase. The raw HTML will be shown first so you understand the big picture, and the Twig implementation will be shown second.


HTML
----
<!-- The ng-controller is the name of the API that will be called, e.g. ListApiController -->
<md-list ng-controller="StratusController"
data-target="User" data-api='{"options":{"limitContext":true, "showProfile":true, "showMailLists":true}}"
layout-padding ng-cloak>

    <!-- Proggress Bar -->
    <md-progress-linear ng-if="collection.pending" md-mode="indeterminate"></md-progress-linear>

    <!-- Header -->
    <div layout="row">
        <div>
            <md-button ng-disabled="true" class="md-fab md-primary md-mini white-svg">
                <md-icon md-svg-src="/Api/Resource?path=@SitetheoryCoreBundle:images/icons/actionButtons/edit.svg"></md-icon>
            </md-button>
        </div>
        <div flex><h2>Name</h2></div>
        <div flex><h2>Profile</h2></div>
        <div flex><h2>Permissions</h2></div>
    </div>

    <!-- List Body with Repeating Rows -->
    <md-list-item ng-repeat="model in collection.models" layout="row" layout-xs="column" layout-sm="column" layout-align="space-between center" layout-wrap>
        <div>
            <md-button href="{{ collection.meta.attributes.editUrl }}?id={{ model.data.id }}" aria-label="edit" class="md-fab md-primary md-mini white-svg">
                <md-icon md-svg-src="/Api/Resource?path=@SitetheoryCoreBundle:images/icons/actionButtons/edit.svg"></md-icon>
            </md-button>
        </div>
        <div class="user" layout="column" flex>
            <h4><a href="{{ collection.meta.attributes.editUrl }}?id={{ model.data.id }}">{{ model.data.bestName }}</a></h4>
            <div><a href="mailto:{{ model.email }}">{{ model.data.email }}</a></div>
            <!-- Convert unix timestamp to readable date -->
            <div>Created {{ model.data.time*1000 | date:'medium' }}</div>
        </div>
        <div class="profile" layout="column" flex>
            <div>
                <span ng-if="model.data.profile.lookupValues.ageGroup">{{ model.data.profile.lookupValues.ageGroup }}</span>
                <span ng-if="model.data.profile.lookupValues.relationshipStatus">{{ model.data.profile.lookupValues.relationshipStatus }}</span>
                <span ng-if="model.data.profile.lookupValues.gender">{{ model.data.profile.lookupValues.gender }}</span>
                <span ng-if="model.data.profile.zip">from {{ model.data.profile.zip }}</span>
            </div>
            <div ng-if="model.data.profile.mailLists.length > 0" ng-repeat="mailList in model.data.profile.mailLists">
                <span>{{ mailList.name }}<span ng-if="!$last">, </span></span>
            </div>
        </div>
        <div class="permissions" layout="column" flex>
            <div>{{ model.roles.join(', ') }}</div>
        </div>
        <md-divider md-inset ng-if="!$last"></md-divider>
    </md-list-item>
</md-list>


TWIG
----
{% extends 'SitetheoryCoreBundle:Core:ListBase.html.twig' %}.
{% set entityContentType = 'User' %}
{% set entityApi = '{"options":{"limitContext":true, "showProfile":true, "showMailLists":true}}' %}
{% block listHeader %}
    <!-- HTML header-->
{% endblock listHeader %}
{% block listRow %}
    {% verbatim %}
    <!-- HTML for individual repeating rows with access to the `model` data -->
    {% endverbatim %}
{% endblock listRow %}



*************
Example: Edit
*************

<!-- Targeting the Article entity API for the specified ID -->
<div ng-controller="StratusController" data-target="Article" data-id="35558" data-manifest="true" layout-padding ng-cloak>
    <div layout="row" layout-xs="column" layout-sm="column" layout-align="space-between center" layout-wrap>
        <md-progress-linear ng-if="model.pending" md-mode="indeterminate"></md-progress-linear>
        <md-input-container ng-show="model.completed">
            <!-- set a variable unconnected to the model -->
            <md-switch ng-model="showHints">Hints</md-switch>
        </md-input-container>
        <md-input-container flex="100" ng-show="model.completed">
            <label>Title</label>
            <input ng-model="model.data.viewVersion.title" type="text" required>
        </md-input-container>

        <md-input-container flex="100" ng-show="model.completed">
            <label>Subtitle</label>
            <input ng-model="model.attributes.viewVersion.subtitle" type="text">
            <div class="hint" ng-show="showHints">
                This hint will show when showHints switch is true.
            </div>
        </md-input-container>

        <md-input-container flex="100" ng-show="model.completed">
            <label>Display Date</label>
            <md-datepicker ng-model="model.data.viewVersion.timeCustom"></md-datepicker>
        </md-input-container>

        <md-input-container flex="100" ng-show="model.completed">
        <label>Body</label>
        <textarea ng-model="model.data.viewVersion.text"
        redactor='{"focus":false,"codemirror":true,"definedLinks":"\/Api\/MenuLink","paragraphize":false,"replaceDivs":false,"minHeight":120,"fileUpload":"https:\/\/app.sitetheory.io:3000\/?session=75j69973dvp3mfqg5ig9pcutn0","fileManagerJson":"\/Api\/Media\/?filter=file","imageUpload":"https:\/\/app.sitetheory.io:3000\/?session=75j69973dvp3mfqg5ig9pcutn0","imageManagerJson":"\/Api\/Media\/?filter=image","formatting":["p","blockquote","pre","h1","h2","h3","h4","h5","h6","script","svg"],"plugins":["clips","definedlinks","filemanager","fullscreen","imagemanager","table","textexpander","video"]}'></textarea>
        </md-input-container>

        <md-button aria-label="save" class="md-raised md-primary white-svg" ng-show="model.completed" ng-click="model.save()">Save</md-button>
    </div>
</div>


##################
Deprecated Widgets
##################


See the Javascript documentation for detailed specs of each widget.
http://js.sitetheory.io/2/0/stratus.html


**************************
Deprecated: Widget Options
**************************

data-property (string): This is the model property that is being edited.

data-label (string): The label for the information being edited.

data-help (string): Additional information to help users, which will appear as a popover on a help icon.

data-template (string): This would be a full web path to a template file or a template key from config.js.

data-templates (JSON): This is a JSON object with names of the templates and a key or web path to the template that should be used for each part of the widget. Usually most widgets have only one template, but in cases like the Collection widget, there may be a list, container, and entity template, and this allows you to customize all of them, e.g. {"list": "/path-to-list", "container": "/path-to-container", "entity": "/path-to-entity"


.. _overview-display:

*******
Display
*******

.. _overview-text:

****
Text
****


.. _overview-toggle:

******
Toggle
******


.. _overview-select:

******
Select
******



data-multiple (boolean): This determines if people can select one or multiple options. BEWARE: the entity property being edited needs to support multiple, otherwise this obviously won't save properly.

data-ui (string): specify the way the select should display, either as a "list" where you can see all the options on the page (as radio, checkboxes or image buttons), or as a "menu" where the options are hidden in a drop down menu to conserve space.

data-placeholder (string): If this select has ui set to display "menu" this is the value that will appear in the dropdown when there are no options selected.

data-choices (JSON): If you want to manually set the options, you can pass in a JSON object. This can be either a simple array (e.g. ["value1", "value2"] where the values will be used for key and label), or an array of objects (e.g. [{value: "foo", label: "Foo", image: "//www.sitetheory.io/images/foo.jpg"}, {value: "bar", label: "Bar", image: "//www.sitetheory.io/images/foo2.jpg"}]). Allowed Properties include: value, label, image, containerClass, checked.

data-source (string): If you want the options to be pulled from an API source, you can specify the entity, e.g. "Layout" will initiate a call to /Api/Layout, and this will in turn pull all Layouts.

data-sourcetarget (JSON): If you need to limit the API call you can pass in additional target limits, e.g. a value like {"entity":"contentType", "id":100} will cause the API to actually send a limiting request like /Api/ContentType/100/Layout which will only return layouts that are assigned to contentType 100. If you don't know the content type, but that exists on the model of the current entity you are editing, you can pass in a dynamic "idAttribute" like {"entity":"contentType", "idAttribute":"contentType.id"} and the current entity will look up it's value for contentType.id and use that value.

data-sourcelabelattribute (string): When the API returns the model, it needs to know what field to use as the label for the options. So you would specify "name" or "title" or whatever the field is on that model.


data-sourceImageAttribute (string): When the API returns the model, it needs to know what field to find the images. This will default to 'images'.

data-sourceidattribute (string): When the API returns the model, it needs to know what field to use as the value for the options. So you would specify "id" or whatever the field is on that model. It defaults to 'id'.

 data-sourcelimit (integer): This determines the limit of how many options should appear at a time.

data-showSearch (boolean): This determines whether a search box appears to filter the options. This is only available if the options are sourced from the API, and will only appear if there are more than 1 page of results.

data-showselected (boolean): this allows you to specify that a collection will appear that shows all the elements selected. If the choices for the select are dynamically populated from a data-source (API) than the selected list will be a collection.

data-textSelectedNoContent (string): This determines what appears in the "selected" zone when there are no options selected. Depending on context, this message needs to change frequently. This area can also be customized with a template
data-cssSelectedNoContent="addAnimation"







.. _overview-datetime:

********
DateTime
********


.. _overview-editor:

******
Editor
******



.. _overview-link:

****
Link
****



.. _overview-popover:

*******
Popover
*******



.. _overview-pagination:

**********
Pagination
**********



.. _overview-collection:

**********
Collection
**********

data-meta: this allows you to pass in data to the collection widget so that it will be accessible in the template, e.g. when defining the widget on the DOM, add an attribute for data-meta='{"foo":"bar"}' will pass in values to the template to be accessed as {{ globals.meta.foo }}


.. _overview-save:

****
Save
****



.. _overview-publish:

*******
Publish
*******



.. _overview-delete:

******
Delete
******



.. _overview-seo:

***
Seo
***


.. _overview-routing:

*******
Routing
*******