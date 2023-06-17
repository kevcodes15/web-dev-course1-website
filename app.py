from flask import Flask,render_template
app=Flask(__name__)
#flask application created
@app.route("/")
def hello_world():
  return render_template('home.html')
#use the following statement to run the code
#0.0.0.0 is used to run locally
if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)