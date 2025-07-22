from routes import app
from flask import render_template, abort, redirect, url_for, flash
from flask_login import logout_user, current_user
from services.article_service import ArticleService
from forms.login_form import LoginForm
from services.user_service import UserService
from forms.delete_articel_form import DeleteArticleForm

# 定義路由，表示進入目錄時的處理函數
@app.route('/', methods=['GET', 'POST'])
@app.route('/index.html', methods=['GET', 'POST'])
def home_page():
    if current_user.is_authenticated:
        delete_article_form = DeleteArticleForm()
        if delete_article_form.validate_on_submit():
            if delete_article_form.validate_on_submit():
                result, error = ArticleService().delete_article(int(delete_article_form.article_id.data))
                if result:
                    flash(f'成功刪除文章', category='success')
                    return redirect(url_for('home_page'))
                else:
                    flash(f'刪除文章失敗: {error}', category='danger')
    articles = ArticleService().get_articles()
    if current_user.is_authenticated:
        return render_template('index.html', articles=articles, delete_article_form=delete_article_form)

    return render_template('index.html', articles=articles) 

@app.route('/article/<article_id>.html')
def article_page(article_id):
    article = ArticleService().get_article(article_id)
    if article:
        return render_template('article.html', my_title=article.title, article=article)
    abort(404) 

@app.route('/about.html')
def about_page():
    return render_template('about.html', my_title="About Page")

# 方法 GET 獲取表單；POST 提交表單
@app.route('/login.html', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        result = UserService().do_login(username=form.username.data, password=form.password.data)
        if result:
            flash(f'歡迎{form.username.data}回來', category='success')
            return redirect(url_for('home_page'))
        else:
            flash('用戶名稱或密碼錯誤，請重試!', category='danger')
    return render_template('login.html', form=form)

@app.route('/logout.html', methods=['GET'])
def logout_page():
    logout_user()
    return redirect(url_for('home_page'))