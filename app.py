from gwBackend import app

def _run():
    """ Imports the app and runs it. """
app.run(debug=True, host="0.0.0.0", port=5000)
#app.run(debug=True, host="0.0.0.0", port=5000,ssl_context=('cert.pem', 'key.pem') )


if __name__ == '__main__':
    _run()
    