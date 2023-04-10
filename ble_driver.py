from blatann import BleDevice
from blatann.gap.scanning import Scanner
from blatann.examples import example_utils

logger = example_utils.setup_logger(level="INFO")


ble_device = BleDevice("/dev/tty.usbmodemC9A6DD9E4BC22")
ble_device.configure()
ble_device.open()

scanner = Scanner(ble_device)
scanner.set_default_scan_params(interval_ms=200, window_ms=150, timeout_seconds=1, active_scanning=True)
try:
    while True:
        waitable = scanner.start_scan()
        scan_report_collection = waitable.wait()
        for report in scan_report_collection.advertising_peers_found:
            # logger.info(report)
            # print(report)
            if report.device_name == 'RDL52810':
                # print(report.advertise_data)
                # print(report.advertise_data.service_data)
                byte_list = list(report.advertise_data.service_data)
                if byte_list[0] == 24 and byte_list[1] == 3:
                    temperature = float(str(byte_list[2])+'.'+str(byte_list[3]))
                    print(f'Temperature: {temperature}')
                    humidity = float(str(byte_list[4])+'.'+str(byte_list[5]))
                    print(f'Humidity: {humidity}')

                    # print(byte_list)
                    acc_start_idx = 6
                    acc_X = float(str((-1)**byte_list[acc_start_idx] * float(str(byte_list[acc_start_idx+1])+'.'+str(byte_list[acc_start_idx+2]*10+byte_list[acc_start_idx+3]))))
                    print(f'X: {acc_X}')

                    acc_Y = float(str((-1)**byte_list[-8] * float(str(byte_list[-7])+'.'+str(byte_list[-6]*10+byte_list[-5]))))
                    print(f'Y: {acc_Y}')

                    acc_Z = float(str((-1)**byte_list[-4] * float(str(byte_list[-3])+'.'+str(byte_list[-2]*10+byte_list[-1]))))
                    print(f'Z: {acc_Z}')



except KeyboardInterrupt:
    print('interrupted!')

# scan_report_collection = ble_device.scanner.start_scan().wait(timeout=20)

# print(scan_report_collection)

# for report in scan_report_collection.advertising_peers_found:
#     # logger.info(report)
#     print(report)