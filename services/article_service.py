from routes import db
from models.article import Article
from sqlalchemy import Select, func

class ArticleService:
    def get_article(self, id):
        return db.session.get(Article, id)
    
    def get_articles(self):
        query = Select(Article)
        return db.session.scalars(query).all()
    
    def create_article(self, article: Article):
        query = Select(Article).where(Article.title == article.title)
        exist_articles = db.session.scalars(query).all()
        if exist_articles:
            # 如果文章已存在，返回現有文章對象和錯誤訊息
            return exist_articles[0], '同標題的文章已经存在' 
        
        db.session.add(article)
        db.session.commit()
        return article, None 
    
    def update_article(self, article: Article):
        exist_article = db.session.get(Article, article.id)
        if not exist_article:
            return None, '文章不存在'
        
        query = Select(Article).where(Article.title == article.title).where(Article.id != article.id)
        exist_articles = db.session.scalars(query).all()
        if exist_articles:
            return exist_article, '同標題的文章已经存在'
        
        exist_article.title = article.title
        exist_article.content = article.content
        exist_article.update_time = db.func.now()
        
        db.session.commit()
        return exist_article, None
    
    def delete_article(self, article_id: int):
        article = db.session.get(Article, article_id)
        if article:
            db.session.delete(article)
            db.session.commit()
            return True, None
        else:
            return False, '找不到要刪除的文章'