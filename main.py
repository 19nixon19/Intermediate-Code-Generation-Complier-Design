def arithmetic(eqn): 
 pflist=[]
 st=[]
 op=('+','-','*','/','^')
 prec={'+':1,'-':1,'*':2,'/':2,'^':3}
 for c in eqn:
   if(c in op):
     if(len(st)==0 or prec[st[-1]]<prec[c]): 
      st.append(c)
     else:
      while(len(st)>0 and prec[st[-1]]>=prec[c]):         
        pflist.append(st.pop())
      st.append(c)
   else:
     pflist.append(c) 
 for st_ in st:
   pflist.append(st_) 
 pf=''.join(pflist)
 print("Postfix expression: ",pf)
 st=[]
 r_cnt=1
 print("Three address code: ") 
 for i in pf:
   if i not in op:
     st.append(i)
   else:
     a=st.pop(-1)
     b=st.pop(-1)
     print('\tR'+str(r_cnt)+'='+a+i+b)
     r_cnt+=1
     st.append('R'+str(r_cnt-1))
 return r_cnt-1

def relational(eqn): 
   rcnt=100
   t=0
   sts={}
   sts_=["if "+eqn+" goto "+str(rcnt+3), "T:= "+str(t), " goto "+str(rcnt+4),"T:= "+str(t+1), "End"] 
   for cnt in range(rcnt, rcnt+5):
     sts[cnt]=sts_[cnt-rcnt]
   for k,v in sts.items():
     print(k,v)
def assignment(eqn):
   res=eqn[0]
   x=arithmetic(eqn[2:])
   print('\t',eqn[0:2],'R'+str(x),sep='')
while(True):
 tp=input("Enter the type expression (Assignment/Arithmetic/Relational): ")  
 if(tp=='Exit'):
   break
 eqn=input("Enter the equation: ")
 if(tp=='Assignment'): 
   assignment(eqn)
 elif(tp=='Arithmetic'):
   x=arithmetic(eqn) 
 elif(tp=='Relational'):
   relational(eqn)
 else:
   print("Invalid choice")




