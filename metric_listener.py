from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__, template_folder='template')

@app.route("/alerts", methods = ['POST', 'GET'])
def alerts():
	if request.method == 'POST':
		req_data = request.get_json()
		metric_alert = 'alerts' in req_data
		if metric_alert:
				req_data_alert = req_data['alerts']
				with open('template/alerts.html','w') as m:
					write_content = ''
					for alert in req_data_alert:
						write_content += '<p>'
						for parameter in alert:
							write_content += '<h5>'+ parameter + ' : ' + alert[parameter] + '</h5>'
						write_content+= '</p>'
					m.write(write_content)
				
				return ''
		
	return render_template("alerts.html")




if __name__ == '__main__':

	app.run(host='0.0.0.0', debug=True)