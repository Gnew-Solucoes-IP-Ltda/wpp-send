#!/bin/bash
cp wpp-send.service /etc/systemd/system/
systemctl enable wpp-send
systemctl daemon-reload
systemctl start wpp-send.service