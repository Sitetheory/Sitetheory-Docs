Angular Filters
###############


Time
====

`moment`
--------
Format a Unix timestamp into a human readable string. The default moment format is `MMM Do YYYY, H:mma` e.g. Jan 1st 2016, 2:30pm.
*Arguments*
You can pass in arguments by specifying a JSON string, e.g. `moment:{format:"M/D/YY"}`
- `format` (string): specify the [moment time format](http://momentjs.com/docs/#/displaying/).
- `since` (boolean): specify that the date should be displayed as a time "since", e.g. "1 day ago" (default false)
- `relative` (string): time that the `since` value should apply, after which it should go back to the format. Specify the time based a number and time identifier, e.g. `1y`, `4w`, `7d`, `8h`, `15m`, `30s`, or join multiple like `7d8h` (default `1w`)

Example: {{ model.data.time | moment:{since:true,format:"MM/DD/YY, h:mm a"} }}