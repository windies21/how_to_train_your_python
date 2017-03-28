from flask import Flask, request, session, url_for, abort, render_template, \
    flash, redirect
import grpc
import sample_pb2
import sample_pb2_grpc

app = Flask(__name__)

app.config.from_object(__name__) # load config from this file, route.py

# Load default config and override config from an environment variable
app.config.update(dict(
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))


@app.route('/')
def show_entries():
    list_request = sample_pb2.ListRequest()
    post_list = stub.GetPosts(list_request)
    return render_template('show_entries.html', entries=post_list)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)

    """form 안의 title 필드와 text 필드의 내용을 가져와 Post 메시지 생성"""
    post = sample_pb2.Post(title=request.form['title'], text=request.form['text'])
    response = stub.AddPost(sample_pb2.AddRequest(post=post))
    flash(response.message)
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

if __name__ == '__main__':
    channel = grpc.insecure_channel('localhost:50051')
    stub = sample_pb2_grpc.PosterStub(channel)
    app.run(debug=True)
