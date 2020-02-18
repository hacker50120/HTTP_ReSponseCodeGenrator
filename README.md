# HTTP_ReSponseCodeGenrator

Simply Genrate HTTP Response code in Terminal.
This will Help You to find Which Domain Is Corrently Working or not.
You can set manually Timeout,(defult =3) .

HOW TO USE-->

1.) Install the python library --> 'pip3 install requests'
2.) Create a new file with name 'file.txt'.
3.) Paste Your All Domain here, Example-->( https/http://xyz.com).
NOTE- All domain must be start with http/https.
4.) Run the script -> { python3 Genrator.py }
5.) save that response in file use--> { python3 Genrtor.py | tee -a file-name.txt }


NOTE------>
IF YOU GOT SUCH TYPE ERROR {

Error Connecting: HTTPSConnectionPool(host='confluence.defense.gov', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLError("bad handshake: Error([('SSL routines', 'tls_process_server_certificate', 'certificate verify failed')])")))

}

DELETE THAT DOMAIN IT'S COMMING BECAUSE SSL CERTIFICATE ERROE..

OUTPUT-->

URL------------>Status_code

http://google.com------------>200

http://facebook.com------------>200

http://twitter.com------------>200 .



Genrated By hacker50120..
