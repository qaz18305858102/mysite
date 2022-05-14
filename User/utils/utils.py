import re
from User.models import UserBase, UserInfo, Question
from User.utils.encryption import Encryption
from django.db import models


class Utils:

    def __init__(self):
        pass

    def login(self, userName: str, pwd: str):
        newpwd = Encryption.des_encrypt(pwd)
        Username = UserBase.objects.filter(username=userName, password=newpwd)
        print(Username)
        if Username:
            return '登陆成功'
        return '帐号密码错误'

    '''注册'''

    def register(self, username: str, password: str, question: str, answer: str, Email: str
                 , repeatpassword: str, firstname=None, lastname=None):
        creat_time = 'now()'
        update_time = 'now()'
        Username = UserBase.objects.filter(username=username).first()
        # print(date)

        if password != repeatpassword:
            return "密码不一致"

        '''判断用户名是否存在'''
        if Username is not None:
            return "用户名已存在"

        '''判断用户名长度'''
        if len(username) < 6 or len(username) > 12:
            return "用户名长度为6-12"

        '''判断密码长度'''
        if len(password) < 6 or len(password) > 12:
            return "密码长度为6-12"

        '''判断用户名组成'''
        if re.search(r'[0-9]', username) is None or re.search(r'[a-zA-Z]', username) is None:
            return "用户名须包含数字，英文"

        '''判断密码组成'''
        if re.search(r'[0-9]', password) is None or re.search(r'[a-zA-Z]', password) is None:
            return "密码须包含数字，英文"
        newpwd = Encryption.des_encrypt(password)
        UserBase.objects.create(username=username, password=newpwd, creat_time=creat_time,
                                updtae_time=update_time)
        UserInfo.objects.create(username=username, firstname=firstname, lastname=lastname, Email=Email,
                                question=question, answer=answer, creat_time=creat_time,
                                updtae_time=update_time)
        return "注册成功"

    '''获取用户名，判断用户名是否已存在'''

    def get_username(self):
        Username = UserBase.objects.values("username")
        user_list = []
        for username in Username:
            user_list.append(username["username"])
        return user_list

    '''获取注册时的问题'''

    def get_question(self):
        question = Question.objects.values("question")
        question_list = []
        for q in question:
            question_list.append(q["question"])
        return question_list
    #
    # '''修改密码'''
    #
    # def changePassword(self, userName, newpwd):
    #     updateSql = Mysql()
    #     '''判断密码长度'''
    #     if len(newpwd) < 6 or len(newpwd) > 12:
    #         return "密码长度为6-12"
    #
    #     '''判断密码组成'''
    #     if re.search(r'[0-9]', newpwd) is None or re.search(r'[a-zA-Z]', newpwd) is None:
    #         return "密码须包含数字，英文"
    #     pwd = Encryption.des_encrypt(newpwd)
    #     sql = f"update user_info set user_password = '{pwd}' ,update_time=now() where user_name='{userName}'  "
    #     date = updateSql.update_one(sql)
    #     if date == 1:
    #         return "修改成功"
    #
    # '''根据旧密码修改密码'''
    #
    # def changePassword_OldPwd(self, userName, oldpwd, newpwd):
    #     updateSql = Mysql()
    #     # sql = 'select user_password from user_info where user_name = \'{userName}\' '.format(userName=userName)
    #     sql = f"select user_password from user_info where user_name = '{userName}' "
    #     user_password = updateSql.selectSql(sql=sql)
    #     if user_password is not None:
    #         pwd = user_password["user_password"]
    #         s = Encryption.des_descrypt(pwd)
    #         if s == oldpwd:
    #             # selectSql = Mysql()
    #             # sql1 = f"select user_password from user_info where user_name = '{userName}' "
    #             # user_password = selectSql.selectSql(sql=sql1)
    #             # oldpwd = user_password["user_password"]
    #             if s == newpwd:
    #                 return "新密码与原密码一致"
    #             date = self.changePassword(userName, newpwd)
    #             return date
    #         return '原密码错误'
    #     return '账号不存在'
    #
    # '''根据问题答案修改密码'''
    #
    # def changePassword_Question(self, userName, answer, newpwd):
    #     updateSql = Mysql()
    #     # sql = 'select user_password from user_info where user_name = \'{userName}\' '.format(userName=userName)
    #     sql = f"select answer from user_info where user_name = '{userName}' "
    #     original_answer = updateSql.selectSql(sql=sql)
    #     if original_answer is not None:
    #         if original_answer["answer"] == answer:
    #             selectSql = Mysql()
    #             sql1 = f"select user_password from user_info where user_name = '{userName}' "
    #             user_password = selectSql.selectSql(sql=sql1)
    #             pwd = user_password["user_password"]
    #             s = Encryption.des_descrypt(pwd)
    #             if s == newpwd:
    #                 return "新密码与原密码一致"
    #             date = self.changePassword(userName, newpwd)
    #             return date
    #         return '答案错误'
    #     return '账号不存在'


if __name__ == "__main__":
    date = UserBase.objects.filter(username="hehaodong123")
    print(date)
