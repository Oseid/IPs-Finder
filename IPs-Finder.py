ó
öñYc           @   sÏ   d  Z  yT d d l Z d d l Z d d l Z d d l m Z d d l m Z d d l	 Z	 Wn d GHe
   n Xd Z d   Z d   Z d	   Z d
   Z d   Z e   Z d   Z e d k rË e   n  d S(   sµ   

[+] Welcome To IPs-Finder Script Source Code :) [+]

[+] Simply Script For Find IPADDRESSES [WEB,Public,LOCAL] [+]
-------------------+
By: Oseid Aldary:) |
-------------------+

iÿÿÿÿN(   t   system(   t   sleeps]   
[!]the [ dnspython lib ] is not found!
[*]Please run this command [ pip install dnspython ]
s   www.google.comc          C   s=   y/ t  j t  }  t  j |  d f d  } t SWn n Xt S(   NiP   i   (   t   sockett   gethostbynamet   servert   create_connectiont   Truet   False(   t   ipt   ss(    (    sA   /media/root/Persistence/my-tools/mytestes/IPs-Finder/IPsFinder.pyt   check   s    c             s/  t    t k r
t d    t d    d k s=   d  k rL d GHt   q+  f d   }  |    t k rÛ  d  d k r   d } n#   d  d	 k r¤   d } n   } d
 } d j    GHt d  d GHxs d d g D]e } yE t j j	 | |  } x) | D]! } d j | |  GH| d
 7} qÿ WWqÚ t j j
 k
 r>qÚ XqÚ W| d
 } d j |  GHd GHt d  } | d k s| d k rt d  t   q| d k s°| d k r¿d GHt   qd GHt d  t d
  q+|    t k r+d j    GHd GHt   q+n! t    t k r+d GHt d
  n  d  S(   Ns   [+]:Enter target WebSite:> g      ø?t    s3   
[!]:Please Enter website: e.g:- www.facebook.com!
c             s}   yo   d  d k r    d }  n#   d  d k r=   d }  n   }  t  j |   } t  j | d f d  } t SWn n Xt S(   Ni   s   https://i   s   http://iP   i   (   R   R   R   R   R   (   t   hostR   t   run(   t   target(    sA   /media/root/Persistence/my-tools/mytestes/IPs-Finder/IPsFinder.pyt   checker.   s    i   s   https://i   s   http://i   s'   

[*]:Finding IPaddresses TARGET[ {} ]
gÍÌÌÌÌÌ @s)   
[+]:Found
------------------------------t   At   AAAAs   WebServer:[{}] : {}s:   

[+]:This Target WebSite Has [{}] WebServer![:status:[UP]s&   
[?]:[b]ack [a]gain [e]xit

[IPs-F]=> t   bt   Bs   clear || clst   as   
Exiting.......i   sI   
[x]Error:404 Server Not Found!
[x]:This Target[> {} <]Website not Found s   
s^   
[!]:Ops Your Not Connected To The Internet
[*]:Please Connected To The Internet and Try Agian(   R
   R   t	   raw_inputR   t   Nonet   webt   formatt   dnst   resolvert   queryt   NoAnswerR    t   maint   exitR   (   R   R   t   loobt   address_typet   answerst   rdatat   resulitt   ask(    (   R   sA   /media/root/Persistence/my-tools/mytestes/IPs-Finder/IPsFinder.pyR   &   sZ    







c          C   s|   t    t k rl d GHt d  t j d  j   j   }  d GHd j |   GHt d  } t	 d  t
   n d GHt   d  S(	   Ns!   
[*]Finding Your Public IP...... i   s   http://wtfismyip.com/texts   [#]:Found
------------------s   [+]:YOUR Public IP: {}s!   
Press Enter To back to Main Menus   clear || clss^   
[!]:Ops Your Not Connected To The Internet
[*]:Please Connected To The Internet and Try Agian(   R
   R   R   t   urllibt   urlopent   readt   rstripR   R   R    R   R   (   t   ppipt   press(    (    sA   /media/root/Persistence/my-tools/mytestes/IPs-Finder/IPsFinder.pyR)   j   s    


c          C   s¹   t    t k r© d GHt d  g  t j t j t j  g D]. }  |  j d  |  j   d |  j   f ^ q: d d } d GHd j	 |  GHt
 d	  } t d
  t   n d GHt   d  S(   Ns    
[*]Finding Your Local IP...... i   s   8.8.8.8i5   i    i   s   [#]:Found
------------------s   [+]:YOUR Local IP: {}s!   
Press Enter To back to Main Menus   clear || clss]   
[!]:Ops Your Not Connected To Any Network
[*]:Please Connected To Some Network and Try Agian(   s   8.8.8.8i5   (   R
   R   R   R   t   AF_INETt
   SOCK_DGRAMt   connectt   getsocknamet   closeR   R   R    R   R   (   t   st   locipR*   (    (    sA   /media/root/Persistence/my-tools/mytestes/IPs-Finder/IPsFinder.pyR1   x   s    
X

c          C   s"   d d d g }  t  j |   } | S(   Nt   GoodByes   See you laters   Have a nice day(   t   randomt   choice(   t   sayt   rsay(    (    sA   /media/root/Persistence/my-tools/mytestes/IPs-Finder/IPsFinder.pyt	   randomsay   s    c          C   s°   y t  d  }  |  d k r% t   na |  d k r; t   nK |  d k rQ t   n5 |  d k ru d j t  GHt   n t d  t   Wn" t	 k
 r« t d  t   n Xd  S(   Ns-  
 /$$$$$$ /$$$$$$$                  /$$$$$$$$ /$$                 /$$                     /$$
|_  $$_/| $$__  $$                | $$_____/|__/                | $$                    | $$
  | $$  | $$  \ $$ /$$$$$$$       | $$       /$$ /$$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$ | $$
  | $$  | $$$$$$$//$$_____//$$$$$$| $$$$$   | $$| $$__  $$ /$$__  $$ /$$__  $$ /$$__  $$| $$
  | $$  | $$____/|  $$$$$$|______/| $$__/   | $$| $$  \ $$| $$  | $$| $$$$$$$$| $$  \__/|__/
  | $$  | $$      \____  $$       | $$      | $$| $$  | $$| $$  | $$| $$_____/| $$          
 /$$$$$$| $$      /$$$$$$$/       | $$      | $$| $$  | $$|  $$$$$$$|  $$$$$$$| $$       /$$
|______/|__/     |_______/        |__/      |__/|__/  |__/ \_______/ \_______/|__/      |__/
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
[---]        By: Oseid Aldary        [---]
[---]	     ve:    2.0		     [---]
==========================================
[#]:WELCOME(^-^)

[+] Select Choice [+]

1 ---> Find WebSite IPADDRESSES
2 ---> Find Your Public IP Addr
3 ---> Find Your Local IP Addr

4 ---> exit

[IPs-F]--> t   1t   2t   3t   4s&   
Thanks For using IPs-Finder Script
{}s   clear || cls(
   R   R   R)   R1   R   R6   R   R    R   t   KeyboardInterrupt(   t   menu(    (    sA   /media/root/Persistence/my-tools/mytestes/IPs-Finder/IPsFinder.pyR      s"    	





t   __main__(   t   __doc__t   dns.resolverR   R   R%   t   osR    t   timeR   R3   R   R   R
   R   R)   R1   R7   R6   R   t   __name__(    (    (    sA   /media/root/Persistence/my-tools/mytestes/IPs-Finder/IPsFinder.pyt   <module>   s$   $			D					*