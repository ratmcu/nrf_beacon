# nrf_beacon


## Setup

everything mentioned otherwise should be run on python3.8(`brew install python@3.8`)

### build and install the driver:

https://github.com/NordicSemiconductor/pc-ble-driver-py branch `release/0.13`

can also be done with given wheel and python3.8

### Install blatann https://github.com/ThomasGerstenberg/blatann:

`python3.8 -m pip install blatann`

run the script https://github.com/ThomasGerstenberg/blatann/blob/master/tools/macos_retarget_pc_ble_driver_py.sh by changing 

https://github.com/ThomasGerstenberg/blatann/blob/fe2d85b3e39ff681bb43a0e98c3e41b5d6f06b83/tools/macos_retarget_pc_ble_driver_py.sh#L13-L14

to python3.8

![image](https://user-images.githubusercontent.com/16415585/231025866-35453884-2838-451f-9c0e-5eaaf7b4958d.png)
