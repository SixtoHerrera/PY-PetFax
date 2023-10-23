[ ... ]
import json 

pets = json.load(open('pets.json'))
print(pets)

[ ... ]


from flask import ( Blueprint, render_template ) 

from flask import Flask

@bp.route('/')
def index(): 
    return render_template('index.html')

@bp.route('/')
def index(): 
    return 'This is the pets index'

@bp.route('/')
def index(): 
    return render_template('index.html', pets=pets)
