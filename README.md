# Automatic-Client

parameters:
"-me", "--measurement" - type of measurement, e.g. "TestCPU"
"-a", "--active" - flag used to choose only active monitors, non obligatory, default: active = True
"-na", "--noactive" - flag used to choose not only active monitors, non obligatory, default: active = True
"-mo", "--monitors" - list of monitors

example:
python3 client.py --measurement TestCPU --active --monitors https://pz-monitor.herokuapp.com https://pz-monitor-2.herokuapp.com
