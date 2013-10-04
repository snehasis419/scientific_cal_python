from add import add
from mul import multiply
from div import divide
from sub import substract
import math
prev=0;
while 1:
	print "Enter your choice \n Arithmetic\n1.Addition\n2.Substraction\n3.Multiplication\n4.Division\nTrigonometric\n5.sin\n6.cos\n7.tan\n8.cot\n9.sec\n10.cosec\n11.Exit";
	c=input();
#ADD
	if c==1:
		if prev==0:
			a=input("Enter one number");
			b=input("Enter another number");
		elif prev==1:
			a=k;
			b=input("Enter another number");
		k=add(a,b);
		print "The current sum is "+str(k);
#SUBSTRACT
	elif c==2:
		if prev==0:
			a=input("Enter one minuend");
			b=input("Enter subtrahend");
		elif prev==1:
                        while 1:
				print "Enter your choice\n1.Use answer as minuend\n2.Use answer as subtrahend";
				e=input();
				if e==1:
					a=k;
					b=input("Enter subtrahend");
					break;
				elif e==2:
					a=input("Enter minuend");
					b=k;
					break;
				else:
					print "Undefined";
                k=substract(a,b);
		print "The current difference is "+str(k);

#MULTIPLY
	elif c==3:
		if prev==0:
			a=input("Enter one number");
			b=input("Enter another number");
		elif prev==1:
			a=k;
			b=input("Enter another number");
		k=multiply(a,b);
		print "The current product is "+str(k);

#DIVIDE
	elif c==4:
		if prev==0:
			a=input("Enter numerator");
			b=input("Enter denominator");
		elif prev==1:
                        while 1:
				print "Enter your choice\n1.Use answer as numerator\n2.Use answer as denominator";
				e=input();
				if e==1:
					a=k;
					b=input("Enter denominator");
					break;
				elif e==2:
					a=input("Enter numerator");
					b=k;
					break;
				else:
					print "Undefined!!!";	
                k=divide(a,b);
		print "The current division is "+str(k);

#SIN
	elif c==5:
		if prev==0:
			a=input("Enter number");
		if prev==1:
			a=k;
		k=math.sin(a);
		print "The sin value is "+str(k);     

#COS
	elif c==6:
		if prev==0:
			a=input("Enter number");
		if prev==1:
			a=k;
		k=math.cos(a);
		print "The cos value is "+str(k);     	

#TAN
	
	elif c==7:
		if prev==0:
			a=input("Enter number");
		if prev==1:
			a=k;
		k=math.tan(a);
		print "The tan value is "+str(k);

#COT
	elif c==8:
		if prev==0:
			a=input("Enter number");
		if prev==1:
			a=k;
		k=math.tan(a);
                k=divide(1,k);
		print "The cot value is "+str(k);  	

#SEC
	elif c==9:
		if prev==0:
			a=input("Enter number");
		if prev==1:
			a=k;
		k=math.cos(a);
                k=divide(1,k);
		print "The sec value is "+str(k);  

#COSEC

	
	elif c==10:
		if prev==0:
			a=input("Enter number");
		if prev==1:
			a=k;
		k=math.sin(a);
                k=divide(1,k);
		print "The cosec value is "+str(k);  	
#Exit

	elif c==11:
		break;

#UNDEFINED
	else:
		print "Undefined !!!"	
#Further calculation
	while 1:
		print "Do you want to use this value for further calculation\n1.Yes\n2.No";
		f=input();
		if f==1:
			prev=1;
			break;
		elif f==2:
			prev=0;
			break;
		else:
			print "Undefined!!"

