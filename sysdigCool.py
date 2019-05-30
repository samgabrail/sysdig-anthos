from bottle import route, run

@route('/sysdig')
def sysdig():
   return '<body style="background-color:powderblue;"><h1>Sysdig Rocks with CI/CD!</h1><h3>What do you think?</h3>'

run(host='0.0.0.0', port=8001, debug=True)
