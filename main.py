#Since the Client is initiating the communication, I am writing the python implementation w.r.t client.
# 1. Client starting the communication
# 2. Server sending public key
# 3. Now before going forward, client will check for the correctness of the public key provided by the server. The code goes as follows:

public_key = input();                                      #just assuming that public key is taken as input
if public_key == correct_key:                              #checking for the correctness of key received, by assuming that we have the correct key
    print("key is correct, we can start the session");     #key provided is correct, so we can establish connection with server
    #Start sharing the data.
else:
    print("key is incorrect, stoping the session");        #key doesn't match so we discontinue
    
#Uptill this part of the code, we are checking for the correct server and public key for the client to use.

#please correct me if I have made mistakes or misunderstood something.
