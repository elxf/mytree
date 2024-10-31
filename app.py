from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 로그인 처리 로직이 필요 없으므로 바로 다음 페이지로 리디렉션
        return redirect(url_for('next_page'))
    
    return render_template('index.html')

@app.route('/next-page')
def next_page():
    return render_template('next_page.html')

if __name__ == '__main__':
    app.run(debug=True)
