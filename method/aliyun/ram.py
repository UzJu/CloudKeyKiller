#!/usr/bin/python3.8.4 (python版本)
# -*- coding: utf-8 -*-
# @Author  : UzJu@菜菜狗
# @Email   : UzJuer@163.com
# @Software: PyCharm
# @Time    : 2022/4/14 20:28
# @File    : ram.py

from config import conf
from colorama import Fore, Back, Style
import prettytable as pt
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkram.request.v20150501.AttachPolicyToUserRequest import AttachPolicyToUserRequest
from aliyunsdkram.request.v20150501.CreateUserRequest import CreateUserRequest
from aliyunsdkram.request.v20150501.CreateLoginProfileRequest import CreateLoginProfileRequest
import json


class AliyunRam:
    def __init__(self, UserName, PassWord):
        self.UserName = UserName
        self.PassWord = PassWord
        self.tb = pt.PrettyTable()
        self.tb.field_names = ["UserName", "PassWord", "LoginUrl"]

    def CreateUser(self):
        try:
            client = AcsClient(conf.Aliyun_AK, conf.Aliyun_SecretKey, 'cn-hangzhou')

            request = CreateUserRequest()
            request.set_accept_format('json')

            request.set_UserName(self.UserName)

            response = client.do_action_with_exception(request)
            print(Fore.GREEN, f"[+]Create {self.UserName} Success {str(response, encoding='utf-8')}")
        except Exception as e:
            print(Fore.RED, f"[-]Create {self.UserName} Faild: ", e)

    def CreateLoginProfile(self):
        try:
            client = AcsClient(conf.Aliyun_AK, conf.Aliyun_SecretKey, 'cn-hangzhou')

            request = CreateLoginProfileRequest()
            request.set_accept_format('json')

            request.set_UserName(self.UserName)
            request.set_Password(self.PassWord)

            response = client.do_action_with_exception(request)
            print(Fore.GREEN, f"[+]Create {self.UserName} PassWord {self.PassWord} Success: {str(response, encoding='utf-8')}")
        except Exception as e:
            print(Fore.RED, f"[-]Create {self.UserName} Password {self.PassWord} Faild: ", e)

    def AttachPolicyToUser(self):
        try:
            client = AcsClient(conf.Aliyun_AK, conf.Aliyun_SecretKey, 'cn-hangzhou')

            request = AttachPolicyToUserRequest()
            request.set_accept_format('json')

            request.set_PolicyType("System")
            request.set_PolicyName("AdministratorAccess")
            request.set_UserName(self.UserName)

            response = client.do_action_with_exception(request)
            self.tb.add_row([self.UserName, self.PassWord, "https://signin.aliyun.com/"])
            print(Fore.GREEN, f"[+]Create UserPolicy Success {str(response, encoding='utf-8')}\n"
                              f"[+]UserName: {self.UserName}, PassWord: {self.PassWord}\n"
                              f"[+]Login: https://signin.aliyun.com/")
            print(Fore.GREEN, self.tb)
        except Exception as e:
            print(Fore.RED, f"[-]Create UserPolicy Faild: ", e)


def CreateRamUser(UserName, PassWord):
    Ram = AliyunRam(UserName, PassWord)
    Ram.CreateUser()
    Ram.CreateLoginProfile()
    Ram.AttachPolicyToUser()
