[app]
title = android-prober
package.name = android-prober
package.domain = com.guna
source.dir = ./examples
source.include_exts = py,png,jpg,kv,html,css,otf,txt,jinja,java
source.exclude_dirs = tests, bin, examples, xml
version = 0.1
requirements = python3,plyer,pyjnius,flask==2.2.5,Werkzeug==2.3.3,kivy==2.3.0,oscpy==0.6.0,swagger-gen==0.1.2
orientation = portrait
services = Tester:./android_prober/services/android_service.py:foreground:sticky
fullscreen = 0
android.presplash_color = #FFFFFF
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, INTERNET,BLUETOOTH_ADMIN,BLUETOOTH,BLUETOOTH_SCAN,ACCESS_BACKGROUND_LOCATION,ACCESS_FINE_LOCATION,BLUETOOTH_CONNECT, FOREGROUND_SERVICE, ACCESS_ALL_DOWNLOADS, RECEIVE_BOOT_COMPLETED, CALL_PHONE, READ_PHONE_STATE ,VIBRATE,NEW_OUTGOING_CALL, PROCESS_OUTGOING_CALLS
android.api = 33
android.whitelist = unittest/*
android.add_src = java
android.arch = armeabi-v7a
android.useAndroidX=true
android.enableJetifier=true

# specific to webview
# p4a.port =  6000
# p4a.bootstrap = webview (or)  default as sld2

[buildozer]
log_level = 2
warn_on_root = 1