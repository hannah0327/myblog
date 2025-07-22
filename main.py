import bcrypt
from sqlalchemy import inspect
from routes import app, db
from models.user import User 
from models.article import Article 

def init_db():
    with app.app_context():
        inspector = inspect(db.engine)
        db.create_all() 

        # 檢查 'users' 表格是否存在，如果不存在，表示 db.create_all() 剛剛首次運行
        root_user = db.session.query(User).filter_by(username="root").first()
        password_to_set = '1234566' 
        password_hashed = bcrypt.hashpw(password_to_set.encode(), bcrypt.gensalt()).decode('utf-8')
        if not root_user:
            # 如果 'root' 使用者不存在，則創建它
            print("正在創建初始 'root' 使用者...")
            user = User(username="root", password=password_hashed, fullname='hannah', description='')
            db.session.add(user)
        else:
            root_user.password = password_hashed
        db.session.commit()

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', debug=True, port=8080)