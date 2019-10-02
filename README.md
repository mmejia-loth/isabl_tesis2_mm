# isabl_tesis2

[![travis badge][travis_badge]][travis_base]
[![codecov badge][codecov_badge]][codecov_base]

El proyectico de Daniela

## Quick Start

See [settings] for general configurations and also check [Live reloading and SASS compilation]. To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go. To create a **superuser account**, use this command:

    python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

## Celery

This app comes with Celery. To run a celery worker:

    cd isabl_tesis2
    celery -A isabl_tesis2.taskapp worker -l info

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.

## Deployment

See [Docker]  deployment documentation.

## Testing

Use pytest with coverage.

    # run tests
    pytest --ds config.settings.local --cov=isabl_tesis2 -s

    # see coverage report
    open htmlcov/index.html

<!-- references -->
[settings]: http://cookiecutter-django.readthedocs.io/en/latest/settings.html
[Live reloading and SASS compilation]: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html
[docker]: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html
[heroku]: http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html

<!-- badges -->
[codecov_badge]: https://codecov.io/gh/isabl-io/isabl_tesis2/branch/master/graph/badge.svg
[codecov_base]: https://codecov.io/gh/isabl-io/isabl_tesis2
[travis_badge]: https://img.shields.io/travis/isabl-io/isabl_tesis2.svg
[travis_base]: https://travis-ci.org/isabl-io/isabl_tesis2
