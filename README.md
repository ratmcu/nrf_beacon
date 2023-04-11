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

### firmware is the nfr connectivity burned by this app
![image](https://user-images.githubusercontent.com/16415585/231025866-35453884-2838-451f-9c0e-5eaaf7b4958d.png)


### beacon

https://www.aliexpress.com/item/1005003384346722.html?spm=a2g0o.detail.1000013.14.3d096490dEvtkk&gps-id=pcDetailBottomMoreThisSeller&scm=1007.13339.291025.0&scm_id=1007.13339.291025.0&scm-url=1007.13339.291025.0&pvid=bf819fe4-a7af-4c18-99f2-5dafa890ae69&_t=gps-id:pcDetailBottomMoreThisSeller,scm-url:1007.13339.291025.0,pvid:bf819fe4-a7af-4c18-99f2-5dafa890ae69,tpp_buckets:668%232846%238115%232000&isseo=y&pdp_npi=3%40dis%21CAD%219.33%219.33%21%21%21%21%21%40210324a716811769141403246ebf0d%2112000025529247108%21rec%21CA%21
