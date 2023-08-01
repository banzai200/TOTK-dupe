#!/bin/bash

service dbus start
bluetoothd &

nxbt webapp
