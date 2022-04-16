#!/usr/bin/python3.8.4 (python版本)
# -*- coding: utf-8 -*-
# @Author  : UzJu@菜菜狗
# @Email   : UzJuer@163.com
# @Software: PyCharm
# @Time    : 2022/4/14 15:40
# @File    : ecs.py


from config import conf
import json
import prettytable as pt
from colorama import Fore, Back, Style
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest
from aliyunsdkecs.request.v20140526.RunCommandRequest import RunCommandRequest


class AliyunEcs:
    # 列出所有地区的ECS
    def AliyunDescribeInstancesRequest(self, GetRegionId):
        try:
            client = AcsClient(conf.Aliyun_AK, conf.Aliyun_SecretKey, GetRegionId)
            tb = pt.PrettyTable()
            tb.field_names = ["RegionId", "OSName", "HostName", "InstanceId", "InstanceName", "PublicIpAddress"]
            request = DescribeInstancesRequest()
            request.set_accept_format('json')
            response = client.do_action_with_exception(request)
            result = str(response, encoding="utf-8")
            if not json.loads(result)['Instances']['Instance']:
                pass
            else:
                for i in json.loads(result)['Instances']['Instance']:
                    tb.add_row([GetRegionId,
                                i['OSName'],
                                i['HostName'],
                                i['InstanceId'],
                                i['InstanceName'],
                                i['PublicIpAddress']['IpAddress']
                                ])
                print(Fore.GREEN, tb)
        except Exception as e:
            print("[-]GetEcsList Faild: ", e)

    # 执行命令
    def AliyunRunCommand(self, InstanceId, CommandContent, GetRegionId):
        try:
            client = AcsClient(conf.Aliyun_AK, conf.Aliyun_SecretKey, GetRegionId)
            request = RunCommandRequest()
            request.set_accept_format('json')
            request.set_Type("RunShellScript")
            request.set_CommandContent(CommandContent)
            request.set_InstanceIds([InstanceId])

            response = client.do_action_with_exception(request)
            print(Fore.GREEN, "[+]ExecCommand Success!", str(response, encoding="utf-8"))
        except Exception as e:
            print(Fore.RED, "[-]ExecCommand Faild: ", e)


def GetIntancesTables():
    for i in conf.Aliyun_RegionIdes:
        ECS = AliyunEcs()
        ECS.AliyunDescribeInstancesRequest(i)


def RunCommandInInstances(InstanceId, Command, GetRegionId):
    ECS = AliyunEcs()
    ECS.AliyunRunCommand(InstanceId, Command, GetRegionId)

