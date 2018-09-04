#!/usr/bin/env python

# Reference: http://pylink.readthedocs.io/en/latest/
# pip install pylink-square


import pylink
import time

try:
    import thread
except ImportError:
    import _thread as thread

SETTINGS_SERIAL     = 682010894
SETTINGS_DEVICE_ID  = 'nRF52832_xxAA'



def read_rtt(jlink):
    try:
        while jlink.connected():
            terminal_bytes = jlink.rtt_read(0, 1024)
            if terminal_bytes:
                sys.stdout.write("".join(map(chr, terminal_bytes)))
                sys.stdout.flush()
            time.sleep(0.1)
    except Exception:
        print("IO read thread exception, exiting...")
        thread.interrupt_main()
        raise


def write_rtt(jlink):
    try:
        while jlink.connected():
            print "write bytes"
            bytes = list(bytearray(input(), "utf-8") + b"\x0A\x00")
            bytes_written = jlink.rtt_write(0, bytes)
            time.sleep(1)
    except Exception:
        print("IO write thread exception, exiting...")
        thread.interrupt_main()
        raise



if __name__ == "__main__":
    jlink = pylink.JLink()
    jlink.open(SETTINGS_SERIAL)
    print "product name: ", jlink.product_name
    print "oem: ", jlink.oem
    print "opened: ", jlink.opened()
    print "connected: ", jlink.connected()
    print "target connected: ", jlink.target_connected()
    print "---"

    jlink.set_tif(pylink.enums.JLinkInterfaces.SWD)
    jlink.connect(SETTINGS_DEVICE_ID)
    print "core_id: ", jlink.core_id()
    print "device_family: ", jlink.device_family()
    print "target_connected: ", jlink.target_connected()

    #Flash device
    #jlink.flash_file('/path/to/file', address)

    #Start RTT
    jlink.rtt_start()

    while True:
        try:
            num_up = jlink.rtt_get_num_up_buffers()
            num_down = jlink.rtt_get_num_down_buffers()
            print("RTT started, %d up bufs, %d down bufs." % (num_up, num_down))
            break
        except pylink.errors.JLinkRTTException:
            time.sleep(0.1)
            print "Failed to get number of up/down buffers"

    try:
        thread.start_new_thread(read_rtt, (jlink,))
        thread.start_new_thread(write_rtt, (jlink,))
        while jlink.connected():
            time.sleep(1)
        print("JLink disconnected, exiting...")
    except KeyboardInterrupt:
        print("ctrl-c detected, exiting...")
        pass