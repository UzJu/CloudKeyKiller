#!/usr/bin/python3.8.4 (python版本)
# -*- coding: utf-8 -*-
# @Author  : UzJu@菜菜狗
# @Email   : UzJuer@163.com
# @Software: PyCharm
# @Time    : 2022/4/2 12:07
# @File    : main.py
import argparse

from method.aliyun import ecs
from method.aliyun import ram
from config import BannerInfo


if __name__ == '__main__':
    BannerInfo.echoRandomBannerInfo()
    try:
        parser = argparse.ArgumentParser(description='')

        parser.add_argument('-aliyun', dest='aliyun', nargs="+",
                            help='python3 -aliyun ecs getecs')
        args = parser.parse_args()
        if args.aliyun:
            try:
                if args.aliyun[0] == 'ecs':
                    if args.aliyun[1] == 'getecs':
                        ecs.GetIntancesTables()
                    if args.aliyun[1] == 'exec':
                        ecs.RunCommandInInstances(args.aliyun[2], args.aliyun[3], args.aliyun[4])
                elif args.aliyun[0] == 'ram':
                    if args.aliyun[1] == 'createram':
                        ram.CreateRamUser(args.aliyun[2], args.aliyun[3])

            except Exception as e:
                print("python3 main.py -aliyun ecs getecs\n"
                      "python3 main.py -aliyun ecs exec instanceid command RegionId")
                print(e)
    except KeyboardInterrupt:
        print("KeyError Out")