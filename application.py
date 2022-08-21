# ------------------------------------------------
# Program by Denis Astahov
#
#
# Version      Date           Info
# 1.0          13-Dec-2019    Initial Version
#
# ----------------------------------------------
from flask import Flask, render_template

application = Flask(__name__)


@application.route('/')
def root():
    return 'It Works!'
