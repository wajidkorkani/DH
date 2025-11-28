from flask import Flask, render_template as render

app = Flask(__name__)

listOfusers = [
    {
        "id":1,
        "username": "tom12",
        "name": "Tom",
        "age": 23
    },
    
    {
        "id":2,
        "username": "steve12",
        "name": "Steve",
        "age": 27
    },
    
    {
        "id":3,
        "username": "ahmed12",
        "name": "Ahmed",
        "age": 37
    },
    
    {
        "id":4,
        "username": "ali123",
        "name": "Ali",
        "age": 47
    }
]

@app.route('/')
def Home():
    return render('index.html', users=listOfusers)

app.run(debug=True)