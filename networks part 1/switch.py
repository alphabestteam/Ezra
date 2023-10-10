import csv


port_mac = {
    "70:5a:0f:46:30:50": "Eth0",
    "dc:4a:3e:7e:8f:2b": "Eth1",
    "70:5a:0f:44:3d:77": "Eth2",
    "dc:4a:3e:7e:90:12": "Eth3",
    "9c:7b:ef:aa:2c:6b": "Eth4",
    "9c:7b:ef:aa:2b:b7": "Eth5",
    "ec:b1:d7:5b:a1:b4": "Eth6",
    "70:5a:0d:4a:cd:c7": "Eth7",
}

with open("networks part 1\output.csv", "w", newline="") as output_file:
    csv_writer = csv.writer(output_file)
    csv_writer.writerow(["interface", "source_mac", "dest_mac"])

    with open("networks part 1\input.csv", mode="r") as input_file:
        csvFile = csv.DictReader(input_file)

        for lines in csvFile:
            if lines["dest_mac"] == "ff:ff:ff:ff:ff:ff":
                exclude_port = lines["source_mac"]
                for key, value in port_mac.items():
                    if key != exclude_port:
                        csv_writer.writerow([value, lines["source_mac"], key])
            else:
                new_interface = port_mac[lines["dest_mac"]]
                csv_writer.writerow(
                    [new_interface, lines["source_mac"], lines["dest_mac"]]
                )
