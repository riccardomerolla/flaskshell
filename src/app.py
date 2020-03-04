from flask import Flask
from flask import request
from flask import render_template
from flask import Markup
import subprocess


app = Flask('flaskshell')
#ip_whitelist = ['192.168.1.2', '192.168.1.3']

status_script = "cd {0} && sudo docker-compose ps && docker-compose logs --tail 200"
update_script = "cd {0} && docker-compose pull && docker-compose stop && docker-compose rm -f -v && docker-compose up -d"
test_env = "/opt/sixster"

def valid_ip():
    client = request.remote_addr
    if client in ip_whitelist:
        return True
    else:
        return False

@app.route('/status/test')
def status_test():
    #if valid_ip():
    if True:
        command = status_script.format(test_env)

        try:
            result_command = subprocess.check_output(
                [command], shell=True)
        except subprocess.CalledProcessError as e:
            return "An error occurred while trying to fetch task status updates."

        return render_template('response.html', response=Markup(result_command.decode()))
    else:
        return """<title>404 Not Found</title>
               <h1>Not Found</h1>
               <p>The requested URL was not found on the server.
               If you entered the URL manually please check your
               spelling and try again.</p>""", 404

@app.route('/update/test')
def update_test():
    #if valid_ip():
    if True:
        command = update_script.format(test_env)

        try:
            result_command = subprocess.check_output(
                [command], shell=True)
        except subprocess.CalledProcessError as e:
            return "An error occurred while trying to fetch task status updates."

        return render_template('response.html', response=Markup(result_command.decode()))
    else:
        return """<title>404 Not Found</title>
               <h1>Not Found</h1>
               <p>The requested URL was not found on the server.
               If you entered the URL manually please check your
               spelling and try again.</p>""", 404


if __name__ == '__main__':
    app.run(host='0.0.0.0')

