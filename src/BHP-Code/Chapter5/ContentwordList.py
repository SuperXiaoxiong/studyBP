# coding=utf-8

import threading
import Queue
'''
Created on 2016��4��27��

@author: arthur001
'''
wordlist_file  = "D:\\webtools\\worldlists\\dirbuster\\directory-list-2.3-small.txt" 
resume         = None
threads        = 1
writefile = "ContentWordlists.txt"
def build_wordlist(wordlist_file):

    # read in the word list
    fd = open(wordlist_file,"rb") 
    raw_words = fd.readlines()
    fd.close()
    
    found_resume = False
    words        = Queue.Queue()
    
    for word in raw_words:
        
        word = word.rstrip()
        
        if resume is not None:
            
            if found_resume:
                words.put(word)
            else:
                if word == resume:
                    found_resume = True
                    print "Resuming wordlist from: %s" % resume
                                        
        else:
            if word[0:1] == '#':
                pass
            else:
                words.put(word)
    
    return words

def dir_bruter(extensions=None):
    
    write = open(writefile,"w") 
    while not word_queue.empty():
        attempt = word_queue.get()
        
        attempt_list = []
        
        # check if there is a file extension if not
        # it's a directory path we're bruting
        if "." not in attempt:
            attempt_list.append("/%s/" % attempt)
        else:
            attempt_list.append("/%s" % attempt)
    
        # if we want to bruteforce extensions
        if extensions:
            for extension in extensions:
                attempt_list.append("/%s%s" % (attempt,extension))
                write.write(attempt+extension)        
              
       
   
    
    write.close()

word_queue = build_wordlist(wordlist_file)
extensions = [".php",".bak",".orig",".inc"]

for i in range(threads):
            t = threading.Thread(target=dir_bruter,args=(extensions,))
            t.start()