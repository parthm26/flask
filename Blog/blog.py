from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy data for blog posts
posts = [
    {
        'title': 'First Post',
        'content': 'This is the first blog post.'
    },
    {
        'title': 'Second Post',
        'content': 'This is the second blog post.'
    }
]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
