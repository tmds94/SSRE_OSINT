import os
#import imgkit
import pdfkit
import socket
import urllib.request 
import shutil
import time 



print('''


########################## SSRE OSINT 2018/19 v1.2 ########################## 
        Created by:  Kevin Vieira, Pedro Sousa Silva e Tiago Simões


''')

domain = input("Introduza o domínio pretendido (ex:google.pt):  ")


start = time.time()

#faz um dnslookup do dominio. Caso exista prossegue, senão para o script 
dnscheck = socket.gethostbyname(domain)
zas1 = domain.split('.')
zas2 = zas1[0]
print ("\nDNScheck: OK \n \nIP de {}: {}\n\n ".format(domain, dnscheck) )


#Cria directório
os.mkdir(domain)
os.chdir(domain)

#whois
print ("A procurar whois record de {}. Aguarde...\n".format(domain))
os.system("whois {} > whois_{}.txt".format(domain,zas2))


#URLs relevantes
shodan = 'https://www.shodan.io/search?query={}'.format(domain)
dnsdumpster = 'https://dnsdumpster.com/static/map/{}.png'.format(domain)
emails = 'https://www.email-format.com/i/search_result/?q={}'.format(domain)
#onyphe = 'https://www.onyphe.io/search/?query={}'.format(domain)
statscrop = 'http://www.statscrop.com/www/{}'.format(domain)

#Stats do dominio
print ("A aceder a {}. Aguarde...".format(statscrop))
pdfkit.from_url(statscrop, 'stats_{}.pdf'.format(zas2))
print ("Download de stats_{}.pdf completo\n".format(zas2))


#faz um check do shodan e faz download de um pdf com infromações do DNS 
print ("A aceder a {}. Aguarde...".format(shodan))
pdfkit.from_url(shodan, 'shodan_{}.pdf'.format(zas2))
print ("Download de shodan_{}.pdf completo\n".format(zas2))


#Ve os IP's que estão ligados ao IP central e faz um esquema e posterior download da imagem
print ("A aceder a {}. Aguarde...".format(dnsdumpster))
with urllib.request.urlopen(dnsdumpster) as response, open('mapa_{}.png'.format(zas2), 'wb') as out_file:
    shutil.copyfileobj(response, out_file)
print ("Download de mapa_{}.png completo\n".format(zas2))

#emails 
print ("A aceder a {}. Aguarde...".format(emails))
pdfkit.from_url(emails, 'emails_{}.pdf'.format(zas2))
print ("Download de emails_{}.pdf completo\n".format(zas2))


""" #Igual ao shodan mas para o Onyphe 
print ("A aceder a {}. Aguarde...".format(onyphe))
pdfkit.from_url(onyphe, 'onyphe_{}.pdf'.format(zas2))
print ("Download de onyphe_{}.png completo\n".format(zas2))
 """
stop = time.time() - start

print("O programa demorou {} segundos a executar.\n".format(stop))









