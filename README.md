# django-ranged-fileresponse-filter

This package adds the ability strip `xss` and other malicious content from files upon opening them within a `Django` context.

This package is the same code as [django-ranged-fileresponse](https://github.com/wearespindle/django-ranged-fileresponse) but with [bleach](https://github.com/mozilla/bleach) added

Upon reading the content of a file, it passes it through `bleach`

If you're in the situation that you have an authenticated Django view that returns
files for download, you may have noticed that Safari 9.x doesn't play audio files
properly when returning audio-files. The reason is that Safari sends a HTTP_RANGE request header and expects a proper `Content-Range` response header in return.
There is a [Django ticket](https://code.djangoproject.com/ticket/22479)
for this, however no indication that this feature will be implemented soon.

The [original suggested fix](https://github.com/satchamo/django/commit/2ce75c5c4bee2a858c0214d136bfcd351fcde11d)
applies the code to Django's static view. This is a packaged version of that fix,
but uses a modified FileResponse, instead of applying it to Django's static view.

## Status

Maintained

## Usage

For now, it uses a simple bool flag to toggle filtering on/off 

```
RangedFileResponseFilter(request, open(filename, 'r'), content_type='audio/wav', add_filter=True)
```

setting add_filter=False disables the need for this module you may as well use: `django-ranged-fileresponse-filter`

TODO: in the future you will be able to have more control over what `bleach` filters.


### Requirements

 * django >= 1.4

### Installation

    pip install django-ranged-fileresponse-filter

### Running

    from ranged_fileresponse_filter import RangedFileResponseFilter

    def some_proxy_view(request):
        filename = 'myfile.wav'
        response = RangedFileResponseFilter(request, open(filename, 'r'), content_type='audio/wav', add_filter=True)
        response['Content-Disposition'] = 'attachment; filename="%s"' % filename
        return response

## Contributing

See the [CONTRIBUTING.md](CONTRIBUTING.md) file on how to contribute to this project.

## Contributors

See the [CONTRIBUTORS.md](CONTRIBUTORS.md) file for a list of contributors to the project.

## Roadmap

### Changelog

The changelog can be found in the [CHANGELOG.md](CHANGELOG.md) file.

### In progress

 * Maintaining

### Future

 * Compatibility

## Get in touch with a developer

If you want to report an issue see the [CONTRIBUTING.md](CONTRIBUTING.md) file for more info.

We will be happy to answer your other questions at opensource@wearespindle.com

## License

django-ranged-fileresponse-filter is made available under the MIT license. See the [LICENSE file](LICENSE) for more info.
