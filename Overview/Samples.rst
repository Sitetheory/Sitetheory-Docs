#######
SAMPLES
#######


============================
Signup Form for External API
============================

NOTE: Use the "Sitetheory Registration" component for capturing signups locally.

This is a sample form for submitting to an external third-party API for processing the signup and returning success. This
is useful if you have your data stored elsewhere, and/or want to create custom functionality (e.g. customized email response).
A great solution would be to use a Heroku node.js server to quickly setup logic to process the API call that we make below.


Javascript
----------

```
{% block script %}
    {{ parent() }}

    {# SIGNUP FORM #}
    <script>
        (function (root, factory) {
            if (typeof require === 'function') {
                require(['stratus', 'underscore', 'angular', 'angular-material'], factory);
            } else {
                factory(root.Stratus);
            }
        }(this, function (Stratus, _) {

            Stratus.Controllers.SignupController = function ($scope, $element, $http, $attrs, $window) {

                $scope.options = {
                    pattern: {
                        email: /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/,
                        zip: /[a-zA-Z0-9 \-]{5,}/
                    },
                    // URL to
                    url: 'https://api.thirdpartydomain.com/signup',
                    response: {
                        success: 'Thanks for signing up! We\'ll be in touch shortly.',
                        error: 'Sorry ;( looks like there was an error saving your info. Please email us directly so we can help.'
                    },
                    redirect: {
                        // NOTE: browsers block popups so this isn't advised
                        popup: false,
                        url: false,
                        config: null // 'width=400,height=500,toolbar=no,menubar=no,scrollbars=yes,resizable=yes'
                    }
                };

                // Merge Custom Options
                if($attrs.options) _.extend($scope.options, JSON.parse($attrs.options));

                $scope.response = '';
                $scope.status = null;

                $scope.data = {
                    email: '',
                    zip: ''
                };


                $scope.submit = function(form) {
                    var prototype = {
                        method: 'POST',
                        url: $scope.options.url,
                        data: JSON.stringify($scope.data)
                    };
                    $scope.status = 'sending';
                    $http(prototype).then(
                        // Success
                        function successCallback(response) {
                            if (response && (response.status === 200)) {
                                if($scope.options.redirect.url) {
                                    if ($scope.options.redirect.popup) {
                                        var win = $window.open($scope.options.redirect.url, '_blank', $scope.options.redirect.config);
                                        if(win) win.focus();
                                    } else {
                                        $window.location($scope.options.redirect.url);
                                    }
                                }
                                $scope.response = $scope.options.response.success;
                                $scope.status = 'success';
                            } else {
                                $scope.response = $scope.options.response.error;
                                $scope.status = 'error';
                            }
                        },
                        // Error
                        function errorCallback(response) {
                            $scope.response = $scope.options.response.error;
                            $scope.status = 'error';
                        }
                    );
                }

            };
        }));
    </script>

{% endblock script %}
```


Twig
----


```
{% block registrationForm %}

<form name="Signup" ng-submit="submit(form)" ng-controller="SignupController" options='{"redirect":{"url":"https://secure.actblue.com/contribute/page/bncdec", "popup":false}}' ng-class="status" ng-cloak>

    <md-progress-linear md-mode="indeterminate" ng-show="status === 'sending'"></md-progress-linear>
    <p class="message" ng-show="response.length" ng-bind-html="response"></p>
    <ul class="listInline divCenter fontSecondary">

        {{ registrationFormBefore|default('')|raw }}

        {% verbatim %}
        <li>
            <md-input-container>
                <label>Email</label>
                <input name="email1" type="email" ng-pattern="options.pattern.email" ng-model="data.email" required>
                <div ng-messages="Signup.email1.$error" role="alert">
                    <div ng-message-exp="['required', 'pattern']">
                        Please enter a valid email.
                    </div>
                </div>
            </md-input-container>
        </li>
        <li>
            <md-input-container>
                <label>Zip</label>
                <input name="zip" ng-pattern="options.pattern.zip" ng-model="data.zip" required>
                <div ng-messages="Signup.zip.$error" role="alert">
                    <div ng-message-exp="['required', 'pattern']">
                        Please enter a valid zip code.
                    </div>
                </div>
            </md-input-container>
        </li>
        {% endverbatim %}
        <li>
            <button type="submit" class="btn fakeFormSubmit" ng-disabled="Signup.$invalid">{{ textSubmit|default('Count Me In') }}</button>
        </li>

        {{ registrationFormAfter|default('')|raw }}

    </ul>
</form>
{% endblock registrationForm %}


<div id="footerJoinForm" class="joinForm purple" ng-cloak>
    {% set registrationFormBefore = '<li><div class="starLeft"></div></li><li><h1>Add Your Name</h1></li>' %}
    {% set registrationFormAfter = '<li><div class="starRight"></div></li>' %}
    {{ block('registrationForm') }}
</div>

```



Count Up
========
A counter that changes a number from a start to an end value. You can also tell countUp to animate other elements like a progress bar.

This sample code is using a Custom API to fetch custom data `results.count` which is set to fetch on load and then every 10 seconds afterwards.

```
<div ng-controller="CustomApi" options='{"controller":"/people/count", "onLoad": "fetch", "onTime": {"time": "10s", "method":"fetch"}}'>
    <div id="progressBar" class="positionLeftTop salmon" style="max-width: 100%"></div>
    <div id="totalSignUp" class="borderDashed fontSecondary salmonText" count-up start-val="0" end-val="results.count" count-instance="countUp" related-target="progressBar" related-style="{ width: (100*(frameVal/500000))+'%' }" duration="1.5" decimals="0" scroll-spy-event="elementFirstScrolledIntoView" scroll-spy></div>
</div>
```