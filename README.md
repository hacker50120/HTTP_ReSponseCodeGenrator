# HTTP_ReSponseCodeGenrator

Simply Genrate HTTP Response code in Terminal.
This will Help You to find Which Domain Is Corrently Working or not.
You can set manually Timeout,(defult =3) .

HOW TO USE-->

1.) Download file --> { $ git clone https://github.com/hacker50120/HTTP_ReSponseCodeGenrator }

2.) Use Command --> { $ chmod +x HTTP_ReSponseCodeGenrator.sh }

3.) It will Download all require Library. and file.txt will be open now paste all url here and save them..

4.) Paste Your All Domain here, Example-->( https/http://xyz.com).

NOTE- All domain must be start with http/https.

5.) Run the script -> { python3 Genrator.py }

5.) save that response in file use--> { python3 Genrtor.py | tee -a file-name.txt }

6.) you Can Set timeOut Connection --> timeouts = (conn_timeout, read_timeout)

NOTE------>
IF YOU GOT SUCH TYPE ERROR {

Error Connecting: HTTPSConnectionPool(host='confluence.defense.gov', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLError("bad handshake: Error([('SSL routines', 'tls_process_server_certificate', 'certificate verify failed')])")))


Error Connecting: HTTPSConnectionPool(host='www.acq.osd.mil', port=443): Max retries exceeded with url: /eie/OE/OE_index.html (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x7fb79e87d150>: Failed to establish a new connection: [Errno -2] Name or service not known'))


}

RERUN THE PROGRAMM.
IT'S COMMING BECAUSE SSL CERTIFICATE ERROE (NOT SECURE SITE) OR MAY BE CONNECTION ERROR..

OUTPUT-->

URL------------>Status_code

http://google.com------------>200

http://facebook.com------------>200

http://twitter.com------------>200 .



Genrated By Abhishek Kanaujia..
