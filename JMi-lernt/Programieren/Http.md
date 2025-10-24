# Http Verben
#http #vokabeln
https://wiki.selfhtml.org/wiki/HTTP/Anfragemethoden
## Die häufigsten für Inhalte
`GET  
`POST  
`PUT  
`DELETE  
`PATCH  `
- C  => Create
- R => Read
- U => Update
- D => Delete

## Technisches drum rum
HEAD  
CONNECT  
OPTIONS  
TRACE
### GET:  
Fragt Daten vom Server ab. An den Daten auf dem Server ändert sich nichts. Eine URL wird bei einem Get-Request immer gleich zurückgeliefert. Die Daten können gecacht werden, weil sie nicht verändert werden. Der Querystring ist in der Adresszeile sichtbar und steht in den Logfiles. ! PW in Klartext
-  als Pfad mit `/` 
	- [https://www.testseite.de/](https://www.testseite.de/ "https://www.testseite.de/")  
	- [https://www.testseite.de/user/1](https://www.testseite.de/user/1        => "https://www.testseite.de/user/1%e2%80%83%e2%80%83%e2%80%83%e2%80%83%e2%80%83%e2%80%83%e2%80%83%e2%80%83=%3e")
-  als Query `?`
	-  [https://www.testseite.de/user?id=1](https://www.testseite.de/user?id=1      => "https://www.testseite.de/user?id=1%e2%80%83%e2%80%83%e2%80%83%e2%80%83%e2%80%83%e2%80%83=%3e") 
	- [https://www.testseite.de/user?id=1&name=bla](https://www.testseite.de/user?id=1&name=bla)
	- Dokumentenanker (Verweis)  mit `#
		- [https://www.testseite.de/#page=User](https://www.testseite.de/#page=User "https://www.testseite.de/#page=user")
Nach dem Path wird mit `?` ein Query angeschlossen, dass mit `&` mehrere Parameter verbindet. z.B. bei einer Amazon URL. Beim Bookmarking sollte man darauf achten nur die notwendigen Teile der URL zu speichern.

[https://www.amazon.de/-/en/b/](https://www.amazon.de/-/en/b/ "https://www.amazon.de/-/en/b/") => Path

? => Query  
encoding = UTF8  
& node = 562066  
& ref = gwmm_27c8d0f0  
& pd_rd_w = Or8W4  
& content-id = amzn1.sym.95020868-0b7e-4444-af08-08862310a632  
& pf_rd_p = 95020868-0b7e-4444-af08-08862310a632  
& pf_rd_r = V0MTWDK5W265WXZDN4BC  
& pd_rd_wg = LKrJF  
& pd_rd_r = decae515-8016-40ef-af90-527ce907d681  
& ref = pd_hp_d_atf_unk
#### ULR
Der Pfad in einer URL hat eine feste Syntax
[https://www.testseite.de/](https://www.testseite.de/ "https://www.testseite.de/")  
[https://testseite.de/](https://testseite.de/ "https://testseite.de/")  
[https://swyxonportal.dev.swyx.engineering/](https://swyxonportal.dev.swyx.engineering/ "https://swyxonportal.dev.swyx.engineering/")  
[https://blablub.co.uk/](https://blablub.co.uk/ "https://blablub.co.uk/") Commonwealth United Kingdom  
[https://blablub.co.au/](https://blablub.co.au/ "https://blablub.co.au/") Commonwealth Australia  
[https://blablub.co.nz/](https://blablub.co.nz/ "https://blablub.co.nz/") Commonwealth New Zealand

| Teil       | Name             |
| ---------- | ---------------- |
| http://    | Protokoll        |
| www.       | Subdomain        |
| testseite. | Domain           |
| de         | Top Level Domain |
Die Top Level Domain besteht aus 2-3 Buchstaben außer für Domains im Commenwealth die haben zusätzlich noch ein vorgestelltes `co.` 

### POST:  
Post fügt dem Daten auf dem Server etwas hinzu. Große Datenmengen werden an  den Server gesendet - z.B. Bilder oder Web - Formulare
Die Daten werden vom User an den Server geschickt, dabei werden Formularname und Werte als  Paar  mit `=` in der URL codiert. Der Formularinhalt wird im Header mit gesendet.
Auf dem Server entstehen neue Ressourcen oder werden verändert.
Post Parameter werden nicht archiviert.
Für Passwörter wir immer POST verwendet

[https://www.testseite.de/process/start?bla=blub](https://www.testseite.de/process/start?bla=blub "https://www.testseite.de/process/start?bla=blub")
Die gesendeten Daten werden als Payload bezeichnet
{  
  id: 5,  
  action: "sendMail",  
  token: "amzn1.sym.95020868-0b7e-4444-af08-08862310a632"  
}

[https://www.testseite.de/login?username=juliane&password=Test1234](https://www.testseite.de/login?username=juliane&password=Test1234 "https://www.testseite.de/login?username=juliane&password=test1234")  
Schlechte Idee

[https://www.testseite.de/login](https://www.testseite.de/login "https://www.testseite.de/login")  
{  
  username: "juliane",  
  password: "Test1234"  
}

### PUT:  
Put updatet ein bestehendes Objekt. Das ganze Objekt wird überschreiben.

[https://www.testseite.de/user/7](https://www.testseite.de/user/7 "https://www.testseite.de/user/7")  
{  
  id: 7,  
  username: "juliane2",  
  password: "Test12345"  
}

### PATCH:  
Der Client kann Daten ändern, ohne das ganze Objekt neu zu erstellen. Patches in Json oder XML
[https://www.testseite.de/user/7](https://www.testseite.de/user/7 "https://www.testseite.de/user/7")  
{  
  username: "juliane2"  
}   
Löscht eine Ressource auf dem Server. 
#### Trace
Der Server liefert die Anfrage so zurück wie er sie empfangen hat. Fürs debugging
####  Connect
Für Proxyserver und SSL-Tunel
# RFC Http Statuscodes
https://www.rfc-editor.org/rfc/rfc2616
1xx    Informationelle Codes

2xx    Success Codes  
200    OK  
201    Created

3xx    Redirect Codes  
301    Moved permanently (Permanent Redirect)  
302    Found (Temporary Redirect)

4xx    Client-Side Errors  
400    Bad Request  
401    Unauthorized (not logged in)  
403    Forbidden (logged in, but not enough rights)  
404    Page not found  
405    Method not allowed (POST anstatt GET verwendet)

5xx    Server-Side Errors  
500    Internal Server Error  
502    Bad Gateway  
503    Service Unavailable  
504    Gateway Timeout (Proxy bekommt keine Verbindung zum Ziel)


