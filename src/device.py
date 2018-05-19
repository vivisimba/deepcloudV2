# -*- coding: utf-8 -*-
"""
Created on 2018/5/2

@author: Simba
"""


import config.config as CONFIG
import tools.http_requests as REQ
import requests
import json
import unittest
import dataFile.device_data as DEVICE_DATA
import pprint


def standardDic(dic):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(dic)


class Device(unittest.TestCase):
    """
    验证查看设备列表
        查询设备列表，获得设备数量（逻辑设备是初始化的，所以写死，该查询结果中设备数量应该等于数据库中的该租户下的逻辑设备数量）
        指定逻辑设备id，该逻辑设备的设备ID为空（未绑定物理设备）
        添加物理设备（验证了添加设备，即绑定逻辑设备与物理设备）
        修改刚添加的设备（修改什么属性？修改设备名称和备注）
        调用查询设备列表API，传入刚增加的设备ID，查询单个设备信息（验证查询单个设备）
        删除刚添加的设备（解除绑定）
    """
    # 验证查看设备列表（验证了查看设备列表、添加设备、修改设备、查询单个设备、删除设备）
    def test_queryDeviceList(self):

        # 查看设备列表
        queryUrl = DEVICE_DATA.QUERY_DEVICE_LIST_DIC["url"]
        queryPayload = DEVICE_DATA.QUERY_DEVICE_LIST_DIC["payload"]
        queryHeaders = DEVICE_DATA.QUERY_DEVICE_LIST_DIC["headers"]

        test_queryDeviceListResponse = requests.request(
            "POST",
            queryUrl,
            data=json.dumps(queryPayload),
            headers=queryHeaders
        )
        standardDic(test_queryDeviceListResponse.json())

        # 验证结果
        self.assertEqual(1, test_queryDeviceListResponse.json()["Code"])
        self.assertEqual("success", test_queryDeviceListResponse.json()["Msg"])
        self.assertEqual(10, len(test_queryDeviceListResponse.json()["Data"]["Devices"]))

        # 获得1f0845c4-4955-4ebe-8dfb-2dc675911a0f逻辑设备对应的字典
        theLogicDeviceDic = {}
        theLogicDeviceList = test_queryDeviceListResponse.json()["Data"]["Devices"]
        tempList = []
        for i in theLogicDeviceList:
            if i["LogicDeviceID"] == DEVICE_DATA.ADD_DEVICE_DIC["payload"]["LogicDeviceID"]:
                tempList.append(i)
        if len(tempList) == 1:
            theLogicDeviceDic = tempList[0]

        self.assertEqual(theLogicDeviceDic["DeviceID"], '')
        self.assertEqual(theLogicDeviceDic["DeviceName"], '')
        self.assertEqual(theLogicDeviceDic["DeviceType"], '')
        self.assertEqual(theLogicDeviceDic["Comment"], '')

        # 添加设备
        addUrl = DEVICE_DATA.ADD_DEVICE_DIC["url"]
        addPayload = DEVICE_DATA.ADD_DEVICE_DIC["payload"]
        addHeaders = DEVICE_DATA.ADD_DEVICE_DIC["headers"]

        test_addDeviceResponse = requests.request(
            "POST",
            addUrl,
            data=json.dumps(addPayload),
            headers=addHeaders
        )

        # 验证
        self.assertEqual(1, test_addDeviceResponse.json()["Code"])
        self.assertEqual("success", test_addDeviceResponse.json()["Msg"])
        self.assertEqual(addPayload["payload"]["DeviceType"], test_addDeviceResponse.json()["Data"]["DeviceType"])
        self.assertEqual(addPayload["payload"]["LogicDeviceID"], test_addDeviceResponse.json()["Data"]["LogicDeviceID"])
        self.assertEqual(addPayload["payload"]["DeviceName"], test_addDeviceResponse.json()["Data"]["DeviceName"])
        self.assertEqual(addPayload["payload"]["DeviceID"], test_addDeviceResponse.json()["Data"]["DeviceID"])
        self.assertEqual(addPayload["payload"]["Comment"], test_addDeviceResponse.json()["Data"]["Comment"])

        # 更新设备
        updateDeviceUrl = DEVICE_DATA.UPDATE_DEVICE_DIC["url"]
        updateDevicePayload = DEVICE_DATA.UPDATE_DEVICE_DIC["payload"]
        updateDeviceHeaders = DEVICE_DATA.UPDATE_DEVICE_DIC["headers"]
        test_updateDeviceResponse =requests.request(
            "POST",
            updateDeviceUrl,
            data=json.dumps(updateDevicePayload),
            headers=updateDeviceHeaders
        )

        # 验证
        self.assertEqual(1, test_updateDeviceResponse.json()["Code"])
        self.assertEqual("success", test_updateDeviceResponse.json()["Msg"])
        self.assertEqual(updateDevicePayload["payload"]["DeviceType"], test_updateDeviceResponse.json()["Data"]["DeviceType"])
        self.assertEqual(updateDevicePayload["payload"]["LogicDeviceID"], test_updateDeviceResponse.json()["Data"]["LogicDeviceID"])
        self.assertEqual(updateDevicePayload["payload"]["DeviceName"], test_updateDeviceResponse.json()["Data"]["DeviceName"])
        self.assertEqual(updateDevicePayload["payload"]["DeviceID"], test_updateDeviceResponse.json()["Data"]["DeviceID"])
        self.assertEqual(updateDevicePayload["payload"]["Comment"], test_updateDeviceResponse.json()["Data"]["Comment"])

        # 指定id查询更新的设备
        queryPayload["LogicDeviceIDs"] = DEVICE_DATA.ADD_DEVICE_DIC["payload"]["LogicDeviceID"]
        queryPayload["DeviceIDs"] = DEVICE_DATA.ADD_DEVICE_DIC["payload"]["DeviceID"]

        test_newQueryDeviceListResponse = requests.request(
            "POST",
            queryUrl,
            data=json.dumps(queryPayload),
            headers=queryHeaders
        )

        # 验证
        self.assertEqual(1, test_newQueryDeviceListResponse.json()["Code"])
        self.assertEqual("success", test_newQueryDeviceListResponse.json()["Msg"])
        self.assertEqual(updateDevicePayload["payload"]["DeviceType"], test_newQueryDeviceListResponse.json()["Data"]["DeviceType"])
        self.assertEqual(updateDevicePayload["payload"]["LogicDeviceID"], test_newQueryDeviceListResponse.json()["Data"]["LogicDeviceID"])
        self.assertEqual(updateDevicePayload["payload"]["DeviceName"], test_newQueryDeviceListResponse.json()["Data"]["DeviceName"])
        self.assertEqual(updateDevicePayload["payload"]["DeviceID"], test_newQueryDeviceListResponse.json()["Data"]["DeviceID"])
        self.assertEqual(updateDevicePayload["payload"]["Comment"], test_newQueryDeviceListResponse.json()["Data"]["Comment"])

        # 删除










if __name__ == '__main__':
    unittest.main()
