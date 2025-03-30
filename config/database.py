from flask_sqlalchemy import SQLAlchemy
from util.json_utils import open_json

# SQLAlchemy 객체 생성 (Flask 인스턴스는 app.py에서 설정)
db = SQLAlchemy()

# 데이터베이스 설정 함수
def init_db(app):
    # 하드코딩 방지를 위해 JSON에서 로드
    db_login = open_json(r"config\db_login.json")
    
    # DB 접속 정보 설정
    db_user = db_login["id"]
    db_password = db_login["password"]
    db_host = "localhost"
    db_port = "3306"
    db_name = db_login["db_name"]
    
    # SQLAlchemy URI 설정
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True  # SQL 쿼리 로그 출력 (디버깅용)
    
    db.init_app(app)
