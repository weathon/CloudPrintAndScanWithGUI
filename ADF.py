def main():
    import pyinsane2

    pyinsane2.init()
    try:
        devices = pyinsane2.get_devices()
        assert(len(devices) > 0)
        device = devices[0]
        print("I'm going to use the following scanner: %s" % (str(device)))

        try:
            pyinsane2.set_scanner_opt(device, 'source', ['ADF', 'Feeder'])
        except PyinsaneException:
            print("No document feeder found")
            return

    # Beware: Some scanners have "Lineart" or "Gray" as default mode
    # better set the mode everytime
        pyinsane2.set_scanner_opt(device, 'mode', ['Color'])

    # Beware: by default, some scanners only scan part of the area
    # they could scan.
        pyinsane2.maximize_scan_area(device)

        scan_session = device.scan(multiple=True)
        try:
            while True:
                try:
                    scan_session.scan.read()
                except EOFError:
                    print ("Got a page ! (current number of pages read: %d)"
                        % (len(scan_session.images)))
        except StopIteration:
            print("Document feeder is now empty. Got %d pages"
                % len(scan_session.images))
        
        for idx in range(0, len(scan_session.images)):
            image = scan_session.images[idx]
            image.save("output/"+str(datetime.datetime.now())+".png")
    finally:
        pyinsane2.exit()
