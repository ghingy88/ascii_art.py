import sys
import time


#ascii word
x = """
                                                                          kkkkkkkk
                                                                          k::::::k
                                                                          k::::::k
                                                                          k::::::k
wwwwwww           wwwww           wwwwwwwaaaaaaaaaaaaa  nnnn  nnnnnnnn     k:::::k    kkkkkkk
 w:::::w         w:::::w         w:::::w a::::::::::::a n:::nn::::::::nn   k:::::k   k:::::k
  w:::::w       w:::::::w       w:::::w  aaaaaaaaa:::::an::::::::::::::nn  k:::::k  k:::::k
   w:::::w     w:::::::::w     w:::::w            a::::ann:::::::::::::::n k:::::k k:::::k
    w:::::w   w:::::w:::::w   w:::::w      aaaaaaa:::::a  n:::::nnnn:::::n k::::::k:::::k
     w:::::w w:::::w w:::::w w:::::w     aa::::::::::::a  n::::n    n::::n k:::::::::::k
      w:::::w:::::w   w:::::w:::::w     a::::aaaa::::::a  n::::n    n::::n k:::::::::::k
       w:::::::::w     w:::::::::w     a::::a    a:::::a  n::::n    n::::n k::::::k:::::k
        w:::::::w       w:::::::w      a::::a    a:::::a  n::::n    n::::nk::::::k k:::::k
         w:::::w         w:::::w       a:::::aaaa::::::a  n::::n    n::::nk::::::k  k:::::k
          w:::w           w:::w         a::::::::::aa:::a n::::n    n::::nk::::::k   k:::::k
           www             www           aaaaaaaaaa  aaaa nnnnnn    nnnnnnkkkkkkkk    kkkkkkk

"""

#time to print ascii word
for i in x:
    print(i,end='')
    sys.stdout.flush()
    time.sleep(0.005)

#print doodle in a set time
doodle = "fuck you"
for i in doodle:
    print(i, end='')
    sys.stdout.flush()
    time.sleep(0.7)

end = input()
