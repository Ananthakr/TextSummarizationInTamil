#!/usr/bin/env python
# -*- coding: utf-8 -*-

from py4j.java_gateway import JavaGateway
gateway = JavaGateway()                   # connect to the JVM
str="இப்போது ஆன்மீக விழாவில் பங்கேற்க வந்த பிரதமர் விவசாயிகளுக்கு ஒன்றும் சொல்லவில்லை"
res=gateway.entry_point.stemSent(str)
print(res)