
Queue Paster
============


Copy Copy Copy, Paste Paste Paste.   
A simple python script the queue your clipboard allow you copy and paste as a queue.  
Use shortcut `Ctrl + Win + C` and `Ctrl + Win + V`  


Installation
------------

Install AutoHotKey  
`pip install clipboard`, a python package  
Create `C:\.keycache\queue_paster.txt` and make it writable  

AHK Example
``` 
;Copy Paste As A Queue

^#C::  ;Enqueue
Sendinput, ^{c}
clipwait, 1,1  ;Wait until clipboard contain data
Run, "C:\Users\Liu\Dropbox\Keyboard\QueuePaster\run_run_enqueue_bat.vbs"
Exit

^#V::  ;Dequeue
Run, "C:\Users\LIU\Dropbox\Keyboard\QueuePaster\run_run_dequeue_bat.vbs"
Sleep 1000
Sendinput, ^{v}
Exit
```


Limitation
----------

Currently only support plain text copy.  
For copy multiple rows, it will paste each row seperatly.  
