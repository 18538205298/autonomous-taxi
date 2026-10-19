# 数据库配置文件

# MySQL数据库连接配置
db_config = {
    'host': 'localhost',     # 数据库服务器地址
    'user': 'root',          # MySQL用户名
    'password': 'REDACTED_LOCAL_SECRET',    # MySQL密码
    'port': 3306,            # MySQL默认端口
    'database': 'autonomous_taxi_system'  # 数据库名
}

# SQLAlchemy数据库URI
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:REDACTED_LOCAL_SECRET@localhost/autonomous_taxi_system'
SQLALCHEMY_TRACK_MODIFICATIONS = False 