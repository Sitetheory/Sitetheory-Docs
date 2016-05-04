Lists


The API adds the editUrl in the meta data it returns, so that you can know where entities should be edited. This is based on the current page's controller, but sometimes you need to specify an alternative URL. That can be easily customized for an entire entity by editing the entity's ApiController, e.g. SiteApiController and adding options like this:

protected $options = [
        'altEditUrl' => [
            'bundle' => 'Hosting',
            'controller' => 'SiteSettingsEdit'
        ]
    ];

Or if you just want an alternative editUrl in specific widgets, just add it to the data attribute like this:

data-api='{"options”:{“altEditUrl":{"bundle":"Hosting", "controller":"SiteSettingsEdit"}}}'