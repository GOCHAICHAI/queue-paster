;IV. Copy Paste As A Queue

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