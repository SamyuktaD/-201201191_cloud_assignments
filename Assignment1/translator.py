source_file_name="32_bit.asm"
destination_file_name="new.asm"
f1=open(source_file_name,"r")
f2=open(destination_file_name,"w")
for line in f1:
	if "%ebp" in line:
		line=line.replace("%ebp","%rbp")
	if "%esp" in line:
		line=line.replace("%esp","%rsp")
	if "8\n" in line:
		line=line.replace("8\n","16\n")
	if "5" in line :
		line=line.replace("5","6")
	if "leave" in line:
		line="	popq	%rbp\n"
	if "4, 4" in line:
		line=line.replace("4, 4","7, 8")
	if "movl	%rsp" in line:
		line=line.replace("movl","movq") 
	if "pushl" in line:
		line=line.replace("pushl","pushq")
	if "restore" not in line and "subl" not in line:
		f2.write(line)	
		
	
		
