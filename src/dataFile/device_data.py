# -*- coding: utf-8 -*-
"""
Created on 2018/5/2

@author: Simba
"""


from config import config as CONFIG


# test_queryDeviceList 查询设备列表 参数字典
QUERY_DEVICE_LIST_DIC = {
    "payload": {
        "Offset": 0,
        "LogicDeviceIDs": [],
        "DeviceNames": [],
        "DeviceIDs": []
    },
    "headers": {
        #"Content-Type": "application/json",
        "access_key": "AK-123",
        "secret_key": "SK-123",
        "authkey": "dp-auth-v0",
        "Cache-Control": "no-cache",
        #"Postman-Token": "25ecc927-c6be-45a1-8e55-dcf5b2ead821"
    },
    "url": "http://%s:%s/api/device/list" % (CONFIG.IP, CONFIG.PORT)
}

# 添加设备参数字典
ADD_DEVICE_DIC = {
    "url": "http://%s:%s/api/device/add" % (CONFIG.IP, CONFIG.PORT),
    "payload": {
        "DeviceType": "nemo",
        "LogicDeviceID": "1f0845c4-4955-4ebe-8dfb-2dc675911a0f", # 逻辑设备为初始化到数据库中的，所以目前这里使用固定数据
        "DeviceName": "add device test.",
        "DeviceID": "2018050301",
        "Comment": "Comment for add device test.",
    },
    "headers": {
        'secret_key': "SK-123",
        'access_key': "AK-123",
        'authkey': "dp-auth-v0",
        'Cache-Control': "no-cache",
    }
}

# 更新设备信息参数字典
UPDATE_DEVICE_DIC = {
    "url": "http://%s:%s/api/device/update" % (CONFIG.IP, CONFIG.PORT),
    "payload": {
        "DeviceType": "nemo",
        "LogicDeviceID": "%s" % ADD_DEVICE_DIC["payload"]["LogicDeviceID"],  # 逻辑设备为初始化到数据库中的，所以目前这里使用固定数据
        "DeviceName": "update device test.",
        "DeviceID": "%s" % ADD_DEVICE_DIC["payload"]["DeviceID"],
        "Comment": "Comment for update device test.",
    },
    "headers": {
        'secret_key': "SK-123",
        'access_key': "AK-123",
        'authkey': "dp-auth-v0",
        'Cache-Control': "no-cache",
    }
}