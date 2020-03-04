# Prerequisites
To go along with this tutorial you must have the following installed in your system.

- Python3 (usually installed by default on Ubuntu 14.04)
- virtualenv (sudo apt-get install python-virtualenv)
- Supervisor (sudo apt-get install supervisor)

## Prepare your virtual environment

Use the following commands to prepare your virtual environment (virtualenv) 

```bash
# create a virtualenv using python3
virtualenv -p /usr/bin/python3 flaskshell
# enter the virtualenv directory and perform the basic package installations and tasks
cd flaskshell
# activate virtualenv
source bin/activate
# install flask
pip install flask
```

# Run the application as a service
To run the application as a service I used Supervisor. This is a matter of personal preference; feel free to use any other process control system.

## Define a program on Supervisor.

Create a new Supervisor config file.

```bash
sudo vim /etc/supervisor/conf.d/flaskshell.conf
```

Copy and paste the following code into the file. At this point, you must put the app in - /home/user/workspace/flaskshell.

```
[program:stats]
directory = /home/user/workspace/flaskshell/src
command = /home/user/workspace/flaskshell/bin/python app.py
redirect_stderr = true
stdout_logfile = /home/user/workspace/flaskshell/logs/out.log
stderr_logfile = /home/user/workspace/flaskshell/logs/error.log
```

Now you should update the Supervisor config and start the application.

```bash
sudo supervisorctl update stats
sudo supervisorctl start stats
```
