from flask import render_template
from .application import app

from systeminfo import sysinfo

platform = sysinfo.get_platform_info()

@app.route('/')
def index():
	returnDict = {'title': 'System Information', 'platform': platform}
	return render_template("index.html", **returnDict)
