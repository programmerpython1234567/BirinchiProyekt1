import sqlite3

# Boglsh qismi:
class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db
    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)
#Boglash qismi yakuni.




    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE myfiles_teacher (
            id int NOT NULL,
            Name varchar(255) NOT NULL,
            email varchar(255),
            language varchar(3),
            PRIMARY KEY (id)
            );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, name: str, email: str = None, language: str = 'uz'):
        # SQL_EXAMPLE = "INSERT INTO myfiles_teacher(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO myfiles_teacher(id, Name, email, language) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, name, email, language), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM myfiles_teacher
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM myfiles_teacher where id=1 AND Name='John'"
        sql = "SELECT * FROM myfiles_teacher WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def update_user_email(self, email, id):
        # SQL_EXAMPLE = "UPDATE myfiles_teacher SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE myfiles_teacher SET email=? WHERE id=?
        """
        return self.execute(sql, parameters=(email, id), commit=True)

    def delete_users(self):
        self.execute("DELETE FROM myfiles_teacher WHERE TRUE", commit=True)

    def user_qoshish(self,ism: str, fam:str,username:str,tg_id:int):
        # SQL_EXAMPLE = "INSERT INTO myfiles_teacher(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO foydalanuvchilar(ism,fam,username,tg_id) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(ism,fam,username,tg_id), commit=True)

    def select_all_foydalanuvchilar(self):
        sql = """
        SELECT * FROM foydalanuvchilar
        """
        return self.execute(sql, fetchall=True)

    def foydalanuvchi_qoshish(self, ism: str,fam:str,tg_id:int,username:str=None):
        # SQL_EXAMPLE = "INSERT INTO myfiles_teacher(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO users(ism,fam,tg_id,username) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(ism,fam,tg_id,username), commit=True)

    def foydalanuvchi_qoshish(self, ism: str, fam:str, tg_id:int, username:str=None):
        # SQL_EXAMPLE = "INSERT INTO myfiles_teacher(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO users(ism, fam, tg_id, username) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(ism, fam, tg_id, username), commit=True)







def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")





