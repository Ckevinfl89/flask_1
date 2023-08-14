from app import app

# Add a route
@app.route('/')
def index():
    return 'Hello World!!!!!!!!'

@app.route('/new')
def new():
    name = 'Christian' + ' ' + 'Sanabria'
    return f'This is a new route! How are you, {name}?'

