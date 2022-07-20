from flask import Flask, render_template, jsonify

app = Flask(__name__)

PROJECTS = [
  {
    'id': 0,
    'title':'Deep Learning',
    'url': 'https://medium.com/jovianml/facial-expression-recognition-with-pytorch-using-4-differently-approached-models-ee5c35110193',
    'year': 2020
  },
  {
    'id': 1,
    'title':'Data Analysis',
    'url':'https://medium.com/jovianml/time-series-analysis-data-exploration-and-visualization-9dbede5cbb8d',
    'year': 2021
  },
  {
    'id': 2,
    'title':'Web Scraping',
    'url':'https://medium.com/jovianml/scraping-data-using-beautiful-soup-and-python-4170e7ec63fd',
    'year': 2021
  },
  {
    'id': 3,
    'title':'Machine Learning',
    'url':'https://www.section.io/engineering-education/hyperparmeter-tuning/',
    'year': 2022
  }

  
]


@app.route('/')
def hello():
  return render_template('index.html', projects = PROJECTS, name='HIMANI GULATI')



@app.route('/api/projects')
def list_projects():
  return jsonify(PROJECTS )



if __name__ == '__main__':
  app.run(host ='0.0.0.0', debug=True)
  