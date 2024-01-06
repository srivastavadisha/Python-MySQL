from flask import Flask, request, render_template
import BusinessLayer as bl_layer


app = Flask(__name__)

# @app.route('/')
# def default():
#    return 'welcome default page'

# @app.route('/success/<name>')
# def success(name):
#    return 'welcome %s' % name

# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         user = request.form['nm']
#         return redirect(url_for('login', name=user))
#     else:
#         user = request.args.get('nm')
#         return redirect(url_for('login', name=user))
#     return render_template("login.html")
    

@app.route('/login' , methods=['GET', 'POST'])
def sign_up():
    print("amshjd")
    if request.method == 'POST':
        bookid = request.form.get('bookid')
        bookname = request.form.get('bookname')
        price = request.form.get('price')
    print('bookid', bookid)
    bl_layer.insert_with_parameter(bookid,bookname,price)
    return render_template("login.html")  

if __name__ == '__main__':
     app.run(debug=True)


