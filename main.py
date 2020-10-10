import falcon

import regex

app = falcon.API()
regex.add_apis(app)

if __name__ == '__main__':
    import sys
    from gunicorn.app.wsgiapp import run

    sys.argv.extend(['main:app'])

    run()
