# README

Provides slightly easier set up for using django's built in password
reset mechansim. You will likely still have to overide the templates.

## Setup

In `urls.py` add a pattern like this.

    url(r'^passwords/', include('builtin_password_reset.urls')),

If you want to use the default templates rather than the ones sinked
like the admin you will need to add `builtin_password_reset` to
`INSTALL_APPS` above `django.contrib.admin`.

    INSTALLED_APPS = (
        # ...
        'builtin_password_reset',
        # ...
        'django.contrib.admin',
        # ...
    )

## Templates

Hopefully overriding `registration/passwords_reset_base.html` is enough
to get things works. All four templates inherit from this base template
so the common need of displaying a form should be covered.

## From Email

You will need to set your `DEFAULT_FROM_EMAIL` to an email you are allowed to send from.
