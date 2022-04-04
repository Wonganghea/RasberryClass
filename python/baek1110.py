n= int (input())
num= n
count = 0

while True:
    
 a = num //10  #일의자리
 b = num % 10  # 십의자리
 c = (a+b) % 10 # 일의자리
 num = (b*10) +c
 
 count = count + 1
 if(num ==n): # num 에서 입력된 n 과 똑같은 숫자가 나오면 멈춤 
     break
print(count)