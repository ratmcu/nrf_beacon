import sys
from blatann import BleDevice
from blatann.gap.scanning import Scanner
from blatann.examples import example_utils


logger = example_utils.setup_logger(level="INFO")


def main(port):
    ble_device = BleDevice(port)
    ble_device.configure()
    ble_device.open()

    scanner = Scanner(ble_device)
    scanner.set_default_scan_params(
        interval_ms=200, window_ms=150, timeout_seconds=1, active_scanning=True
    )
    last_arr = ""
    try:
        while True:
            waitable = scanner.start_scan()
            scan_report_collection = waitable.wait()
            # print(scan_report_collection)
            # for report in scan_report_collection.advertising_peers_found:
            #     logger.info(report.peer_address)
            #     logger.info(report)
            # continue
            reports = []
            for report in scan_report_collection.advertising_peers_found:
                # logger.info(report)
                # print(report)
                if report.device_name == "RDL52810" and report.peer_address not in reports:
                    # print(report.advertise_data)
                    # print(report.advertise_data.service_data)
                    # print(report.resolved_address)
                    reports.append(report.peer_address)
                    byte_list = list(report.advertise_data.service_data)
                    # print ('0x' + ''.join('{:02x}'.format(x) for x in byte_list))
                    if byte_list[0] == 24 and byte_list[1] == 3:
                        # logger.info(last_arr)
                        logger.info(f"MAC: {report.peer_address}")
                        # print(report)
                        # logger.info(report)

                        temperature = float(str(byte_list[2]) + "." + str(byte_list[3]))
                        logger.info(f"Temperature: {temperature}")
                        humidity = float(str(byte_list[4]) + "." + str(byte_list[5]))
                        logger.info(f"Humidity: {humidity}")

                        # print(byte_list)
                        acc_start_idx = 6
                        acc_X = float(
                            str(
                                (-1) ** byte_list[acc_start_idx]
                                * float(
                                    str(byte_list[acc_start_idx + 1])
                                    + "."
                                    + str(
                                        byte_list[acc_start_idx + 2] * 10
                                        + byte_list[acc_start_idx + 3]
                                    )
                                )
                            )
                        )
                        logger.info(f"X: {acc_X}")

                        acc_Y = float(
                            str(
                                (-1) ** byte_list[-8]
                                * float(
                                    str(byte_list[-7])
                                    + "."
                                    + str(byte_list[-6] * 10 + byte_list[-5])
                                )
                            )
                        )
                        logger.info(f"Y: {acc_Y}")

                        acc_Z = float(
                            str(
                                (-1) ** byte_list[-4]
                                * float(
                                    str(byte_list[-3])
                                    + "."
                                    + str(byte_list[-2] * 10 + byte_list[-1])
                                )
                            )
                        )
                        logger.info(f"Z: {acc_Z}")
                        print("\n")
                    else:
                        last_arr = "0x" + "".join(
                            "{:02x}".format(x) for x in byte_list[2:8]
                        )

    except KeyboardInterrupt:
        print("interrupted!")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please specify the serial port!")
        exit(1)
    main(sys.argv[1])
    quit()
