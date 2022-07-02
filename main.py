from flask import Blueprint, render_template
from .__init__ import create_app


main = Blueprint('main',__name__)

@main.route("/")
def home():
    # ambil content home dari database
    data = '''
    <h1>This is Home</h1>
    '''

    content = {
    "content": data, 
}
    return render_template('base.html',data=content)

app = create_app()
if __name__ == '__main__':
	app.run(debug=True)