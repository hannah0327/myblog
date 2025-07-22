from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required
from forms.article_form import ArticleForm
from routes import app
from models.article import Article
from services.article_service import ArticleService

# 定義路由，表示進入create.article.html 時的處理函數
@app.route('/create.article.html', methods=['GET', 'POST'])
@login_required
def create_articl_page():
    form = ArticleForm()
    if form.validate_on_submit():
        new_article = Article()
        new_article.title = form.title.data
        new_article.content = form.content.data

        try:
            article, error_msg = ArticleService().create_article(new_article)
            if error_msg: # 如果 message 存在，表示有錯誤訊息 (例如標題重複)
                flash(f'文章創建失敗: {error_msg}', category='danger')
                return render_template('editarticle.html', form=form) # 讓用戶留在頁面並顯示錯誤

            else: # 如果 message 不存在，表示文章成功創建
                flash(f'文章已成功創建!', category='success')
                return redirect(url_for('home_page')) # 重定向到主頁

        except Exception as error:
            flash(f'文章創建失敗: {error}', category='danger')
            return render_template('editarticle.html', form=form) # 讓用戶留在頁面並顯示錯誤
            
    return render_template('editarticle.html', form=form, is_edit=False)

@app.route('/editarticle/<article_id>.html', methods=['GET', 'POST'])
@login_required
def edit_articl_page(article_id: str):
    form = ArticleForm()
    if request.method == 'GET':
        try:
            article = ArticleService().get_article(article_id)
            if not article:
                flash('要修改的文章沒找到', category='danger')
                return redirect(url_for('home_page'))
            else:
                form.title.data = article.title
                form.content.data = article.content
        except Exception as error:
            flash(f'無法獲取文章: {error}', category='danger')
            return redirect(url_for('home_page'))
        
    if form.validate_on_submit():
        try:
            updated_article = Article()
            updated_article.id = int(article_id)
            updated_article.title = form.title.data
            updated_article.content = form.content.data

            article, error_msg = ArticleService().update_article(updated_article)
            if error_msg: 
                flash(f'修改文章失敗: {error_msg}', category='danger')
                return render_template('editarticle.html', form=form) # 讓用戶留在頁面並顯示錯誤

            else: # 如果 message 不存在，表示文章成功創建
                flash(f'文章已修改!', category='success')
                return redirect(url_for('home_page')) # 重定向到主頁

        except Exception as error:
            flash(f'修改文章失敗: {error}', category='danger')
            return render_template('editarticle.html', form=form) # 讓用戶留在頁面並顯示錯誤
            
    return render_template('editarticle.html', form=form, is_edit=True)