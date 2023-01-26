# BLE

[![ Codacy Badge](https://api.codacy.com/project/badge/Grade/880ed281aff445f890766ccccbe81d7d)](https://www.codacy.com/app/xiaoyaoyou1212/BLE?utm_source=github.com&amp;utm_medium =referral&amp;utm_content=xiaoyaoyou1212/BLE&amp;utm_campaign=Badge_Grade) [![License](https://img.shields.io/badge/License-Apache--2.0-green.svg)](https://github. com/xiaoyaoyou1212/BLE/blob/master/LICENSE) [![API](https://img.shields.io/badge/API-18%2B-brightgreen.svg?style=flat)](https:// android-arsenal.com/api?level=18)

**Android BLE basic operation framework, based on callback, easy to operate. It includes functions such as scanning, multi-connection, broadcast packet parsing, service reading and writing, and notification . **

- ** Project address : ** [ https://github.com/xiaoyaoyou1212/BLE](https://github.com/xiaoyaoyou1212/BLE )

- ** Project dependencies : ** `compile ' com.vise .xiaoyaoyou:baseble:2.0.6'`

## function
- ** Support multi- device connection management ; **

- ** Support broadcast packet parsing ; **

- ** Support custom scanning filter conditions ; **

- ** Support filtering scanning devices based on device name regular expressions ; **

- ** Support filtering scanning devices based on the minimum value of the device signal ; **

- ** Support filtering scanning devices based on device name or MAC address list ; **

- ** Support filtering scanning devices based on device UUID ; **

- ** Support searching for specified devices based on specified device names or MAC addresses ; **

- ** Supports retrying on device failure ; **

- ** Support operation device data failure retry ; **

- ** Support binding data sending and receiving channels, the same capability can bind multiple channels ; **

- ** Support registration and cancellation notification monitoring ; **

- ** Supports the configuration of the maximum number of connections, when the maximum number of connections is exceeded, it will be based on Lru The algorithm automatically disconnects the device that has not been used for the longest time ; **

- ** Supports configuration scan, connection and operation data timeout ; **

- ** Support configuration of connection and operation data retry times and retry interval time . **

## Introduction
building this library is to simplify the process of connecting Bluetooth devices. This library is the basic framework of BLE operation, it only deals with BLE device communication logic, and does not include specific data processing, such as data packetization and grouping. This library provides multi-device connection management, the maximum number of connections can be configured, and when the maximum number of connections is exceeded, it will be based on Lru The algorithm automatically disconnects the device that has not been used for the longest time . The library also customizes commonly used scanning device filtering rules, and also supports custom filtering rules. All operations of the library use a callback mechanism to inform the upper layer of the call result, which is easy to operate and easy to access.

## Release notes
[![ LatestVersion](https://img.shields.io/badge/LatestVersion-2.0.6-orange.svg)](https://github.com/xiaoyaoyou1212/BLE/blob/master/VERSION.md)

Latest version update record
- V2.0.6 ( 2018-04-25 )
-Add byte array and integer conversion method ;
- Increase the configuration of interval scanning ;
-Add methods to obtain services, feature values, and attributes .

## Installation package download
[ BLE_V2.0.6.apk]( https://github.com/xiaoyaoyou1212/BLE/blob/master/screenshot/BLE_V2.0.6.apk)

## code hosting
[![ JCenter](https://img.shields.io/badge/JCenter-2.0.6-orange.svg)](https://jcenter.bintray.com/com/vise/xiaoyaoyou/baseble/2.0. 6/)

## FAQ
[![ FAQ](https://img.shields.io/badge/FAQ-%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98-red.svg)] (https://github.com/xiaoyaoyou1212/BLE/blob/master/FAQ.md)

## Effect display
![ BLE effect ](https://github.com/xiaoyaoyou1212/BLE/blob/master/screenshot/screenshot.gif)

## Introduction to use

### Permission configuration
Bluetooth operation , the following permissions need to be configured for systems below 6.0 :
```
<uses-permission android:name =" android.permission.BLUETOOTH " />
<uses-permission android:name =" android.permission.BLUETOOTH_ADMIN " />
```
And systems above 6.0 also need to add fuzzy positioning permissions :
```
<uses-permission-sdk-23 android:name =" android.permission.ACCESS_COARSE_LOCATION " />
```
For the sake of easy operation, the relevant settings for the permissions required for Bluetooth operations have been made in the library without repeated settings, but systems above 6.0 need to dynamically apply for fuzzy positioning permissions .

### Introduce the SDK
the engineering module build.gradle Add the following dependencies to the dependencies in the file :
```
compile ' com.vise.xiaoyaoyou :baseble:2.0.5'
```
After building, you can directly use the functions of the library .

### Initialization
using it, and the initialization code is as follows :
```
// Bluetooth related configuration modification
ViseBle.config ()
        .setScanTimeout ( -1)// Scan timeout, here is set to permanent scan
        .setConnectTimeout (10 * 1000)// connection timeout
        .setOperateTimeout ( 5 * 1000)// Set data operation timeout
        .setConnectRetryCount (3)// Set the number of connection failure retries
        .setConnectRetryInterval (1000)// Set connection failure retry interval
        .setOperateRetryCount (3)// Set the number of retries for data operation failures
        .setOperateRetryInterval ( 1000)// Set data operation failure retry interval time
        .setMaxConnectCount (3);// Set the maximum number of connected devices
// Bluetooth information initialization, globally unique, must be called when the application is initialized
ViseBle . getInstance ( ). init (this);
```
Initialization can be in Application or in MainActivity In , it only needs to be before using the Bluetooth function. It should also be noted that the Bluetooth configuration must be modified before Bluetooth initialization. If the default configuration meets the requirements, the configuration does not need to be modified .

### Device scan
The library defines several common filtering rules for device scanning. If the requirements are not met, you can also define the filtering rules yourself. The following describes how to use the filtering rules provided in the library :

- Scan all devices
```
ViseBle . getInstance ( ). startScan (new ScanCallback (new IScanCallback () {
@Override
public void onDeviceFound ( BluetoothLeDevice bluetoothLeDevice ) {

}

@Override
public void onScanFinish ( BluetoothLeDeviceStore bluetoothLeDeviceStore ) {

}

@Override
public void onScanTimeout ( ) {

}
}));
```

- Scan the device for the specified device MAC
```
// This method is to stop scanning when scanning to the specified device
ViseBle.getInstance().startScan(new SingleFilterScanCallback(new IScanCallback() {
    @Override
    public void onDeviceFound(BluetoothLeDevice bluetoothLeDevice) {

    }

    @Override
    public void onScanFinish(BluetoothLeDeviceStore bluetoothLeDeviceStore) {

    }

    @Override
    public void onScanTimeout() {

}
} ) .setDeviceMac ( deviceMac ));
```

-Scan for devices with the specified device name
```
// This method is to stop scanning when scanning to the specified device
ViseBle . getInstance ( ). startScan (new SingleFilterScanCallback (new IScanCallback () {
@Override
public void onDeviceFound ( BluetoothLeDevice bluetoothLeDevice ) {

}

@Override
public void onScanFinish ( BluetoothLeDeviceStore bluetoothLeDeviceStore ) {

}

@Override
public void onScanTimeout ( ) {

}
} ) .setDeviceName ( deviceName ));
```

-Scan for devices with the specified UUID
```
ViseBle.getInstance().startScan(new UuidFilterScanCallback(new IScanCallback() {
    @Override
    public void onDeviceFound(BluetoothLeDevice bluetoothLeDevice) {

    }

    @Override
    public void onScanFinish(BluetoothLeDeviceStore bluetoothLeDeviceStore) {

    }

    @Override
    public void onScanTimeout() {

}
} ) .setUuid ( uuid ));
```

-Scan for devices that specify a set of device MACs or names
```
ViseBle . getInstance ( ). startScan (new ListFilterScanCallback (new IScanCallback () {
@Override
public void onDeviceFound ( BluetoothLeDevice bluetoothLeDevice ) {

}

@Override
public void onScanFinish ( BluetoothLeDeviceStore bluetoothLeDeviceStore ) {

}

@Override
public void onScanTimeout ( ) {

}
} ).setDeviceMacList (deviceMacList).setDeviceNameList(deviceNameList));
```

-Scan for devices with a specified signal range or device canonical name
```
ViseBle . getInstance ( ). startScan (new RegularFilterScanCallback (new IScanCallback () {
    @Override
    public void onDeviceFound(BluetoothLeDevice bluetoothLeDevice) {

    }

    @Override
    public void onScanFinish(BluetoothLeDeviceStore bluetoothLeDeviceStore) {

    }

    @Override
    public void onScanTimeout() {

    }
} ) .setDeviceRssi ( rssi ) .setRegularDeviceName ( regularDeviceName ));
```

The scanned device list is managed by ` BluetoothLeDeviceStore` , and the individual device information is put into ` BluetoothLeDevice` , which contains all the information of the device, such as device name, device address, broadcast packet analysis information, etc., and related information of the device The information will be introduced in the device details .

### Device connection
There are three ways of device connection, one is to connect directly according to the device information, and the other two are to scan and connect directly through the device name or device MAC without scanning. The three connection methods are used as follows :

- Connect the device according to the device information
```
ViseBle.getInstance ( ) .connect ( bluetoothLeDevice , new IConnectCallback () {
@Override
public void onConnectSuccess ( DeviceMirror deviceMirror ) {

}

@Override
public void onConnectFailure ( BleException exception) {

}

@Override
public void onDisconnect ( boolean isActive ) {

}
});
```

- Directly scan and connect according to the device MAC
```
ViseBle . getInstance ( ). connectByMac ( deviceMac , new IConnectCallback () {
@Override
public void onConnectSuccess ( DeviceMirror deviceMirror ) {

}

@Override
public void onConnectFailure ( BleException exception) {

}

@Override
public void onDisconnect ( boolean isActive ) {

}
});
```

- Directly scan and connect according to the device name
```
ViseBle.getInstance().connectByName(deviceName, new IConnectCallback() {
    @Override
    public void onConnectSuccess(DeviceMirror deviceMirror) {

    }

    @Override
    public void onConnectFailure(BleException exception) {

    }

    @Override
    public void onDisconnect(boolean isActive) {

}
});
```

### Device Details
#### DEVICE INFO ( device information )
- Get the device name ( Device Name): ` bluetoothLeDevice.getName ()` ;
- Get the device address ( Device Address): ` bluetoothLeDevice.getAddress ()` ;
- Get the device class ( Device Class): ` bluetoothLeDevice.getBluetoothDeviceClassName ()` ;
- Get the main device class ( Major Class): ` bluetoothLeDevice.getBluetoothDeviceMajorClassName ()` ;
- Get service class ( Service Class): `bluetoothLeDevice.getBluetoothDeviceKnownSupportedServices()` ;
- Get the state of pairing ( Bonding State): ` bluetoothLeDevice.getBluetoothDeviceBondState ()` ;

#### RSSI INFO ( signal information )
- Get the first signal timestamp ( First Timestamp): ` bluetoothLeDevice.getFirstTimestamp ()` ;
- Get the first signal strength ( First RSSI): ` bluetoothLeDevice.getFirstRssi ()` ;
- Get the last signal timestamp ( Last Timestamp): ` bluetoothLeDevice.getTimestamp ()` ;
- Get the last signal strength ( Last RSSI): ` bluetoothLeDevice.getRssi ()` ;
- Get the average signal strength ( Running Average RSSI): ` bluetoothLeDevice.getRunningAverageRssi ()` ;

#### SCAN RECORD INFO ( broadcast information )
the type number ` record.getType ()` of a broadcast data unit ` AdRecord` according to the scanned broadcast packet ` AdRecordStore` , and then obtain the type description ` record.getHumanReadableType ()` of the broadcast data unit and the broadcast data unit according to the number The length and data content of the data unit, and finally convert the data content into a specific string through ` AdRecordUtil.getRecordDataAsString (record)` . For more information about broadcast packet analysis, please refer to the data analysis section in [Android BLE Study Notes ](http://blog.csdn.net/xiaoyaoyou1212/article/details/51854454) .

### Send data
Before sending data, you need to bind the write data channel first. When binding the channel, you need to set the callback monitor for writing data. The specific code example is as follows :
```
BluetoothGattChannel bluetoothGattChannel = new BluetoothGattChannel . Builder ()
        .setBluetoothGatt ( deviceMirror . getBluetoothGatt ())
        .setPropertyType ( PropertyType . PROPERTY_WRITE )
        .setServiceUUID(serviceUUID)
        .setCharacteristicUUID(characteristicUUID)
        .setDescriptorUUID(descriptorUUID)
        .builder();
deviceMirror.bindChannel(new IBleCallback() {
    @Override
    public void onSuccess(byte[] data, BluetoothGattChannel bluetoothGattChannel, BluetoothLeDevice bluetoothLeDevice) {

    }

    @Override
    public void onFailure(BleException exception) {

    }
}, bluetoothGattChannel);
deviceMirror.writeData(data);
```
here deviceMirror It can be obtained after the device is successfully connected. It should be noted that the channel for writing data only needs to be registered once when the service is the same. If there are multiple channels for writing data, multiple channels can be bound. Writing data must be done after binding the write data channel, and it can be written multiple times in different places.

### Receive data
like sending data, the data sent by the receiving device also needs to bind the receiving data channel. There are two ways here, one is the notification method and the other is the indicator method. The usage is as follows :

-Can be notified
```
BluetoothGattChannel bluetoothGattChannel = new BluetoothGattChannel.Builder()
        .setBluetoothGatt(deviceMirror.getBluetoothGatt())
        .setPropertyType(PropertyType.PROPERTY_NOTIFY)
        .setServiceUUID(serviceUUID)
        .setCharacteristicUUID(characteristicUUID)
        .setDescriptorUUID(descriptorUUID)
        .builder();
deviceMirror.bindChannel(new IBleCallback() {
    @Override
    public void onSuccess(byte[] data, BluetoothGattChannel bluetoothGattChannel, BluetoothLeDevice bluetoothLeDevice) {

    }

    @Override
    public void onFailure(BleException exception) {

    }
}, bluetoothGattChannel);
deviceMirror.registerNotify(false);
```

- 指示器方式
```
BluetoothGattChannel bluetoothGattChannel = new BluetoothGattChannel.Builder()
        .setBluetoothGatt(deviceMirror.getBluetoothGatt())
        .setPropertyType(PropertyType.PROPERTY_INDICATE)
        .setServiceUUID(serviceUUID)
        .setCharacteristicUUID(characteristicUUID)
        .setDescriptorUUID(descriptorUUID)
        .builder();
deviceMirror.bindChannel(new IBleCallback() {
    @Override
    public void onSuccess(byte[] data, BluetoothGattChannel bluetoothGattChannel, BluetoothLeDevice bluetoothLeDevice) {

    }

    @Override
    public void onFailure(BleException exception) {

    }
}, bluetoothGattChannel);
deviceMirror.registerNotify(true);
```
After binding the channel, you need to register for the notification, and you need to call the following code to set up the listener when you receive the registration success callback :
```
deviceMirror.setNotifyListener(bluetoothGattInfo.getGattInfoKey(), new IBleCallback ( ) {
@Override
public void onSuccess ( byte[ ] data, BluetoothGattChannel bluetoothGattChannel , BluetoothLeDevice bluetoothLeDevice ) {

}

@Override
public void onFailure ( BleException exception) {

}
});
```
all devices will be obtained through the above monitoring. If you don’t want to monitor, you can also cancel the registration. The usage is as follows :
```
deviceMirror . unregisterNotify ( isIndicate );
```
isIndicate Indicates whether it is an indicator mode .

### read data
Since the channel for reading device information is basically different every time, it is a bit different from sending and receiving data above. Every time you read data, you need to bind a channel. The usage example is as follows :
```
BluetoothGattChannel bluetoothGattChannel = new BluetoothGattChannel . Builder ()
        .setBluetoothGatt ( deviceMirror . getBluetoothGatt ())
        .setPropertyType ( PropertyType . PROPERTY_READ )
        .setServiceUUID ( serviceUUID ) _
        .setCharacteristicUUID(characteristicUUID)
        .setDescriptorUUID(descriptorUUID)
        .builder();
deviceMirror.bindChannel(new IBleCallback() {
    @Override
    public void onSuccess(byte[] data, BluetoothGattChannel bluetoothGattChannel, BluetoothLeDevice bluetoothLeDevice) {

    }

    @Override
    public void onFailure(BleException exception) {

    }
}, bluetoothGattChannel);
deviceMirror.readData();
```

## 总结
From the above description, we can know that all operations related to the device are uniformly handed over to ` ViseBle` for processing, and this class is a singleton mode, there is only one globally, and the management is very convenient. Before using the functions provided by this library, you must call ` ViseBle.getInstance ( ) .init (context);` for initialization. Every time a device is successfully connected, a device image will be added to the device image pool. This device image is the core class for maintaining all operations after the device is successfully connected. When the connection is disconnected , the device image will be removed from the image pool. , if the number of connected devices exceeds the configured maximum number of connections, the device mirror pool will be based on Lru The algorithm automatically removes the device that has not been used for the longest time and disconnects it . Several commonly used APIs are encapsulated in ` ViseBle` , such as : start and stop scanning, connect and disconnect, clear resources, etc. The functions provided by this library are as simple and easy to use as possible, which is the purpose of this project .

## thanks
I would like to thank the two authors for their open source library [android-lite- bluetoothLE]( https://github.com/litesuits/android-lite-bluetoothLE) and [Bluetooth-LE-Library---Android](https://github.com/litesuits/android-lite-bluetoothLE ) ://github.com/alt236/Bluetooth-LE-Library---Android) , these two open source libraries have provided great help to the completion of this project .

## about me
[![ Website](https://img.shields.io/badge/Website-huwei-blue.svg)](http://www.huwei.tech/)

[![ GitHub](https://img.shields.io/badge/GitHub-xiaoyaoyou1212-blue.svg)](https://github.com/xiaoyaoyou1212)

[![ CSDN](https://img.shields.io/badge/CSDN-xiaoyaoyou1212-blue.svg)](http://blog.csdn.net/xiaoyaoyou1212)

## last
If you find this project helpful, please click Star . If you want to support the author's open source action , please feel free to appreciate it. The appreciation channel is as follows :

![ WeChat payment ](https://github.com/xiaoyaoyou1212/BLE/blob/master/screenshot/wxpay.png)

Your support is my motivation for open source .

If you have good ideas and suggestions , the Fork project is also welcome to participate. If you have any questions and suggestions during use, you can enter the group for communication . The QR code of the QQ group is as follows :

![ QQ group ](https://github.com/xiaoyaoyou1212/XSnow/blob/master/screenshot/qq_chat_first.png)
( This group is full )

![ QQ group ](https://github.com/xiaoyaoyou1212/XSnow/blob/master/screenshot/qq_chat_second.png)




