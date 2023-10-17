from flask import Flask, render_template
import logging
from logging.handlers import SysLogHandler

app = Flask(__name__, template_folder='templates')

# Configure logging at the application level
log_handler = SysLogHandler(address='/dev/log')
log_handler.setLevel(logging.WARNING)
log_format = '%(asctime)s %(levelname)s: %(message)s'
log_formatter = logging.Formatter(log_format, '%Y-%m-%d %H:%M:%S')
log_handler.setFormatter(log_formatter)
app.logger.addHandler(log_handler)


@app.route("/yaml", methods=['GET', 'POST'])
def yaml_upload():
    # Log the message without configuring the handler again
    app.logger.warning("Security Incident occurred")
    return render_template('yaml_test.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5050)