
import os
import sys
import readline
import random
import time as  t

def autocomplete(text, state):
    import readline
    line = readline.get_line_buffer()
    splitted = line.lstrip().split(" ")

    options = [x + " " for x in actions if x.startswith(text)]
    options.extend([x + " " for x in remap if x.startswith(text)])
    try:
        return options[state]
    except:
        return None

def get_input(prompt, auto_complete_fn=None, basefile_fn=None):
    try:
        if auto_complete_fn != None:
            import readline
            readline.set_completer_delims(' \t\n;/')
            readline.parse_and_bind("tab: complete")
            readline.set_completer(auto_complete_fn)
    except Exception as e:
        pass

    cmd = input("%s" % prompt)
    return cmd.strip()

CurrentDir = os.path.dirname(os.path.abspath(__file__))
readline.set_completer(autocomplete)
readline.parse_and_bind("tab: complete")
WHSL = '\033[0m'
ENDL = '\033[0m'
REDL = '\033[0;31m'
GNSL = '\033[0;32m'
load_count = 0
page2 = False

arrow = REDL + "└──>" + WHSL
arrow = str(" "+arrow)
connect = REDL + "│" + WHSL
page_1 = '''{2}

 {0}[{1}00{0}]{2} MOSTRAR PANTALLA DEL DISPOSITIVO
 {0}[{1}01{0}]{2} MOSTRAR DISPOSITIVOS CONECTADOS
 {0}[{1}02{0}]{2} DESCONECTAR DISPOSITIVOS 
 {0}[{1}03{0}]{2} CONECTAR NUEVO DISPOSITIVO
 {0}[{1}04{0}]{2} ACCEDER AL SHELL DEL DISPOSITIVO
 {0}[{1}05{0}]{2} INSTALAR UN APK EN EL DISPOSITIVO 
 {0}[{1}06{0}]{2} GRABAR PANTALLA DEL DISPOSITIVO
 {0}[{1}07{0}]{2} CAPTURE DE PANTALLA AL DISPOSITIVO
 {0}[{1}08{0}]{2} REINICIAR SERVIDOR FANTASMA
 {0}[{1}09{0}]{2} EXTRAER ARCHIVOS DEL DISPOSITIVO       
 {0}[{1}10{0}]{2} APAGAR EL DISPOSITIVO                          
 {0}[{1}11{0}]{2} DESINSTALAR UNA APP
 {0}[{1}12{0}]{2} MOSTRAR REGISTRO DEL DISPOSITIVO     
 {0}[{1}13{0}]{2} INFO DEL DISPOSITIVO        
 {0}[{1}14{0}]{2} LISTA DE TODAS LAS APPS DEL DISPOSITIVO  
 {0}[{1}15{0}]{2} INICIAR APPS DEL DISPOSITIVO       
 {0}[{1}16{0}]{2} REENVIAR PUERTOS           
 {0}[{1}17{0}]{2} TOMA WPA SUPPLICANT   
 {0}[{1}18{0}]{2} MOSTRAR MAC/INET        
 {0}[{1}19{0}]{2} EXTRAER APK DE UNA APP
 {0}[{1}20{0}]{2} OBTENER ESTADO DE LA BATERIA 
 {0}[{1}21{0}]{2} OBTENER ESTADO DE LA RED
 {0}[{1}22{0}]{2} ACTIVAR O DESACTIVAR WIFI DEL DISPOSITIVO
 {0}[{1}23{0}]{2} ELIMINAR BLOQUEO DE PANTALLA
 {0}[{1}24{0}]{2} EMULAR PULSACIONES DE BOTONES 
 {0}[{1}25{0}]{2} OBTENER ACTIVIDAD ACTUAL
 {0}[{1}26{0}]{2} ENTRAR EN MODO RECOVERY
 {0}[{1}27{0}]{2} ENTRAR EN MODO FASTBOOT
 {0}[{1}28{0}]{2} SALIR DEL SERVIDOR FANTASMA
'''.format(GNSL, REDL, WHSL)

page_2 = '''\n
'''.format(GNSL, REDL, WHSL)

def main():
    page_num = 1
    option = input(ENDL + ""+GNSL+"("+REDL + "MENU PRINCIPAL" + GNSL + ")"+ENDL + "> ")
        
    while(1):

        if option == '00':
            try:
                device_name
            except:
             os.system("scrcpy")
            option = input(ENDL + ""+GNSL+"("+REDL + "MENU PRINCIPAL" + GNSL + ")"+ENDL + "> ")

        elif option == '01':
            try:
                device_name
            except:
                print(("{1}[{0}+{1}]{2} DISPOSITIVOS NO ACTIVOS").format(REDL, GNSL, WHSL))
                main()
            os.system("adb devices -l")
            option = input(ENDL + ""+GNSL+"("+REDL + "MENU PRINCIPAL" + GNSL + ")"+ENDL + "> ")

        elif option  ==  '02':
            try:
                device_name
            except:
                print(("{1}[{0}+{1}]{2} DISPOSITIVOS NO ACTIVOS.").format(REDL, GNSL, WHSL))
                main()
            os.system("adb disconnect")
            option = input(ENDL + ""+GNSL+"("+REDL + "MENU PRINCIPAL" + GNSL + ")"+ENDL + "> ")

        elif option == '03':
            print(("\n{1}[{0}+{1}]{2} INGRESAR IP DEL DISPOSITIVO").format(REDL, GNSL, WHSL))
            try:
                device_name = input (arrow+""+GNSL+"("+REDL + "CONECTAR DISPOSITIVO" + GNSL + ")"+ENDL + "> ")
            except KeyboardInterrupt:
                main()
            if device_name == '':
                main()
            if device_name == '27':
                main()
                
            os.system("adb connect "+device_name+":5555")
            option = input(ENDL + ""+GNSL+"("+REDL + "MENU PRINCIPAL" + GNSL + ")"+ENDL + "> ")

        elif option  == '04':
            try:
                device_name
            except:
                print(("{1}[{0}+{1}]{2} DISPOSITIVOS NO ACTIVOS").format(REDL, GNSL, WHSL))
                main()
            os.system("adb -s "+device_name+" shell")
            option = input(ENDL + ""+GNSL+"("+REDL + "MENU PRINCIPAL" + GNSL + ")"+ENDL + "> ")

        elif option == '05':
            try:
                device_name
            except:
                print(("{1}[{0}+{1}]{2} DISPOSITIVOS NO ACTIVOS").format(REDL, GNSL, WHSL))
                main()
            print(("     "+connect))
            print(("    {1}[{0}+{1}]{2} INGRESAR DIRECCION DEL APK").format(REDL, GNSL, WHSL))
            apk_location = input("    "+arrow + ""+GNSL+"("+REDL + "INSTALAR APK" + GNSL + ")"+ENDL + "> ")

            os.system("adb -s  "+device_name+" install "+apk_location)
            print(GNSL  +  "APK INSTALADA")
            option = input(ENDL + ""+GNSL+"("+REDL + "MENU PRINCIPAL" + GNSL + ")"+ENDL + "> ")

        elif option ==  '06':
            try:
                device_name
            except:
                print(("{1}[{0}+{1}]{2} DISPOSITIVOS NO ACTIVOS.").format(REDL, GNSL, WHSL))
                main()
            print(("     "+connect))
            print(("    {1}[{0}+{1}]{2} GRABANDO VIDEO.").format(REDL, GNSL, WHSL))
            print(("     "+connect))
            os.system("adb -s "+device_name+" SHELL /sdcard/screen.mp4")
            print(("    {1}[{0}+{1}]{2} PRESIONA ENTER PARA GUARDAR VIDEO").format(REDL, GNSL, WHSL))
            place_location = input("    "+arrow + ""+GNSL+"("+REDL + "GRABADOR" + GNSL + ")"+ENDL + "> ")
            
            os.system("adb -s "+device_name+" GUARDADO /sdcard/screen.mp4 "+place_location)
            option = input(ENDL + ""+GNSL+"("+REDL + "MENU PRINCIPAL" + GNSL + ")"+ENDL + "> ")

        elif option  == '07':
            try:
                device_name
            except:
                print(("{1}[{0}+{1}]{2} DISPOSITIVOS NO ACTIVOS").format(REDL, GNSL, WHSL))
                main()
            os.system("adb -s "+device_name+" CAPTURA /sdcard/screen.png")
            print(("     "+connect))
            print(("    {1}[{0}+{1}]{2} CAPTURA DE PANTALLA GUARDADA").format(REDL, GNSL, WHSL))
            place_location = input("    "+arrow + ""+GNSL+"("+REDL + "CAPTURA" + GNSL + ")"+ENDL + "> ")

            os.system("adb -s "+device_name+" pull /sdcard/screen.png "+place_location)
            option = input(ENDL + ""+GNSL+"("+REDL + "MENU PRINCIPAL" + GNSL + ")"+ENDL + "> ")

        elif option == '08':
            print(("{1}[{0}+{1}]{2} REINICIANDO SERVIDOR FANTASMA{3}").format(REDL, GNSL, WHSL, ENDL))
            os.system("adb disconnect >> /dev/null")
            os.system("adb kill-server >> /dev/null")
            os.system("adb start-server >> /dev/null")
            t.sleep(4)
            option = input(ENDL + ""+GNSL+"("+REDL + "MENU PRINCIPAL" + GNSL + ")"+ENDL + "> ")

        elif option == '09':
            try:
                device_name
            except:
                print(("{1}[{0}+{1}]{2} DISPOSITIVOS NO ACTIVOS").format(REDL, GNSL, WHSL))
                main()
            print(("     "+connect))
            print(("    {1}[{0}+{1}]{2} UBICACION DEL ARCHIVO").format(REDL, GNSL, WHSL))
            file_location = input("    "+arrow + ""+GNSL+"("+REDL + "ARCHIVO" + GNSL + ")"+ENDL + "> ")
            print(("        "+connect))
            print(("       {1}[{0}+{1}]{2} ARCHIVO GUARDADO").format(REDL, GNSL, WHSL))
            place_location = input("       "+arrow + ""+GNSL+"("+REDL + "ARCHIVO" + GNSL + ")"+ENDL + "> ")

            os.system("adb -s "+device_name+" ARCHIVO "+file_location+" "+place_location)
            option = input(ENDL + ""+GNSL+"("+REDL + "MENU PRINCIPAL" + GNSL + ")"+ENDL + "> ")

        elif option == '10':
            try:
                device_name
            except:
                print(("{1}[{0}+{1}]{2} DISPOSITIVOS NO ACTIVOS").format(REDL, GNSL, WHSL))
                main()
            os.system("adb -s "+device_name+ " reboot ")
            option = input(ENDL + ""+GNSL+"("+REDL + "MENU PRINCIPAL" + GNSL + ")"+ENDL + "> ")

        elif option ==  '11':
            try:
                device_name
            except:
                print(("{1}[{0}+{1}]{2} DISPOSITIVOS NO ACTIVOS").format(REDL, GNSL, WHSL))
                main()
            print(("     "+connect))
            print(("    {1}[{0}+{1}]{2} NOMBRE DEL PAQUETE").format(REDL, GNSL, WHSL))
            package_name = input("    "+arrow + ""+GNSL+"("+REDL + "ELIMINAR APP" + GNSL + ")"+ENDL + "> ")
            os.system("adb -s "+device_name+" DESINSTALAR "+package_name)
            option = input(ENDL + ""+GNSL+"("+REDL + "MENU PRINCIPAL" + GNSL + ")"+ENDL + "> ")

        elif option == '12':
            try:
                device_name
            except:
                print(("{1}[{0}+{1}]{2} DISPOSITIVOS NO ACTIVOS").format(REDL, GNSL, WHSL))
                main()
            os.system('adb -s '+device_name+" logcat ")
            option = input(ENDL + ""+GNSL+"("+REDL + "MENU PRINCIPAL" + GNSL + ")"+ENDL + "> ")

        elif option == '13':
            try:
                device_name
            except:
                print(("{1}[{0}+{1}]{2} DISPOSITIVOS NO ACTIVOS").format(REDL, GNSL, WHSL))
                main()
            os.system("adb -s "+device_name+" shell dumpsys")
            option = input(ENDL + ""+GNSL+"("+REDL + "MENU PRINCIPAL" + GNSL + ")"+ENDL + "> ")

        elif option == '14':
            try:
                device_name
            except:
                print(("{1}[{0}+{1}]{2} DISPOSITIVOS NO ACTIVOS").format(REDL, GNSL, WHSL))
                main()
            os.system("adb -s " +device_name+ " shell pm list packages -f")
            option = input(ENDL + ""+GNSL+"("+REDL + "MENU PRINCIPAL" + GNSL + ")"+ENDL + "> ")

        elif option == '15':
            try:
                device_name
            except:
                print(("{1}[{0}+{1}]{2} DISPOSITIVOS NO ACTIVOS").format(REDL, GNSL, WHSL))
                main()
            print(("     "+connect))
            print(("    {1}[{0}+{1}]{2} INGRESAR NOMBRE DEL PAQUETE").format(REDL, GNSL, WHSL))
            package_name = input("    "+arrow + ""+GNSL+"("+REDL + "INICIANDO APP" + GNSL + ")"+ENDL + "> ")
            os.system("adb -s "+device_name+" shell monkey -p "+package_name+" -v 500")
            option = input(ENDL + ""+GNSL+"("+REDL + "MENU PRINCIPAL" + GNSL + ")"+ENDL + "> ")

        elif option == '16':
            try:
                device_name
            except:
                print(("{1}[{0}+{1}]{2} DISPOSITIVOS NO ACTIVOS ").format(REDL, GNSL, WHSL))
                main()
            print(("     "+connect))
            print(("    {1}[{0}+{1}]{2} INGRESAR PUERTO").format(REDL, GNSL, WHSL))
            port_device = input("    "+arrow + ""+GNSL+"("+REDL + "PUERTO" + GNSL + ")"+ENDL + "> ")
            print(("         "+connect))
            print(("        {1}[{0}+{1}]{2} INGRESE EL PUERTO Y REENVIELO").format(REDL, GNSL, WHSL))
            forward_port = input("        "+arrow + ""+GNSL+"("+REDL + "PUERTO REENVIADO" + GNSL + ")"+ENDL + "> ")
            os.system("adb -s "+device_name+" forward tcp:"+port_device+" tcp:"+forward_port)
            option = input(ENDL + ""+GNSL+"("+REDL + "MENU PRINCIPAL" + GNSL + ")"+ENDL + "> ")

        elif option == '17':
            try:
                print(("     "+connect))
                print(("    {1}[{0}+{1}]{2} ENTER PARA GUARDAR ARCHIVO").format(REDL, GNSL, WHSL))
                location = input("    "+arrow + ""+GNSL+"("+REDL + "WPA" + GNSL + ")"+ENDL + "> ")

                os.system("adb -s "+device_name+" SHELL "+" su -c 'cp /data/misc/wifi/wpa_supplicant.conf/sdcard/'")
                os.system("adb -s "+device_name+" ARCHIVO /sdcard/wpa_supplicant.conf "+location)
                option = input(ENDL + ""+GNSL+"("+REDL + "MENU PRINCIPAL" + GNSL + ")"+ENDL + "> ")

            except KeyboardInterrupt:
                try:
                    device_name
                except:
                    print(("{1}[{0}+{1}]{2} DISPOSITIVO NO ACTIVOS").format(REDL, GNSL, WHSL))
                    main()
                    
                option = input(ENDL + ""+GNSL+"("+REDL + "MENU PRINCIPAL" + GNSL + ")"+ENDL + "> ")

        elif option == '18':
            try:
                device_name
            except:
                print(("{1}[{0}+{1}]{2} DISPOSITIVOS NO ACTIVOS").format(REDL, GNSL, WHSL))
                main()
            os.system("adb -s " +device_name+ "shell ip address wlan0 ")
            option = input(ENDL + ""+GNSL+"("+REDL + "MENU PRINCIPAL" + GNSL + ")"+ENDL + "> ")

        elif option == '19':
            try:
                device_name
            except:
                print(("{1}[{0}+{1}]{2} DISPOSITIVOS NO ACTIVOS").format(REDL, GNSL, WHSL))
                main()
            print(("     "+connect))
            print(("    {1}[{0}+{1}]{2} INGRESAR DIRECCION DEL APK").format(REDL, GNSL, WHSL))
            package_name = input("    "+arrow + ""+GNSL+"("+REDL + "JALAR APK" + GNSL + ")"+ENDL + "> ")
            os.system("adb -s "+device_name+" shell pm path "+package_name)
            print(("         "+connect))
            print(("        {1}[{0}+{1}]{2} INGRESAR PARCHE APK.").format(REDL, GNSL, WHSL))
            path = input("        "+arrow + ""+GNSL+"("+REDL + "JALAR APK" + GNSL + ")"+ENDL + "> ")
            print(("             "+connect))
            print(("            {1}[{0}+{1}]{2} DIRECCION APK")  .format(REDL, GNSL, WHSL))
            location =   input("            "+arrow + ""+GNSL+"("+REDL + "JALAR APK" + GNSL + ")"+ENDL + "> ")

            os.system("adb -s " +device_name+" pull "+path+" "+location)
            option = input(ENDL + ""+GNSL+"("+REDL + "MENU PRINCIPAL" + GNSL + ")"+ENDL + "> ")

        elif option == '20':
            try:
                device_name
            except:
                print(("{1}[{0}+{1}]{2} DISPOSITIVOS NO ACTIVOS").format(REDL, GNSL, WHSL))
                main()
            os.system("adb -s " +device_name+ " shell dumpsys battery")
            option = input(ENDL + ""+GNSL+"("+REDL + "MENU PRINCIPAL" + GNSL + ")"+ENDL + "> ")

        elif option == '21':
            try:
                device_name
            except:
                print(("{1}[{0}+{1}]{2} DISPOSITIVOS NO ACTIVOS ").format(REDL, GNSL, WHSL))
                main()
            os.system("adb -s " +device_name+ " shell netstat")
            option = input(ENDL + ""+GNSL+"("+REDL + "MENU PRINCIPAL" + GNSL + ")"+ENDL + "> ")

        elif option == '22':
            try:
                device_name
            except:
                print(("{1}[{0}+{1}]{2} DISPOSITIVOS NO ACTIVOS").format(REDL, GNSL, WHSL))
                main()
            print(("     "+connect))
            print(("    {1}[{0}+{1}]{2} DESACTIVAR O ACTIVAR WIFI ON/OFF").format(REDL, GNSL, WHSL))
            print(("     "+connect))
            on_off = input(GNSL + "    ["+REDL+"+"+GNSL+"]"+WHSL+"WIFI")
            if on_off == 'off':
                command = " shell svc wifi disable"
            else:
                command = " shell svc wifi enable"

            os.system("adb -s "+device_name+command)
            option = input(ENDL + ""+GNSL+"("+REDL + "MENU PRINCIPAL" + GNSL + ")"+ENDL + "> ")

        elif option == '23':
            try:
                device_name
            except:
                print(("{1}[{0}+{1}]{2} DISPOSITIVOS NO ACTIVOS").format(REDL, GNSL, WHSL))
                main()
            print(("     "+connect))
            print(REDL + "****************** REMOVIENDO PASSWORD ******************")
            os.system("adb -s "+device_name+" shell su 0 'rm /data/system/gesture.key'")
            os.system("adb -s "+device_name+" shell su 0 'rm /data/system/locksettings.db'")
            os.system("adb -s "+device_name+" shell su 0 'rm /data/system/locksettings.db-wal'")
            os.system("adb -s "+device_name+" shell su 0 'rm /data/system/locksettings.db-shm'")
            print(REDL + "****************** REMOVIENDO PASSWORD ******************")
            option = input(ENDL + ""+GNSL+"("+REDL + "MENU PRINCIPAL" + GNSL + ")"+ENDL + "> ")

        elif option == '24':
            try:
                device_name
            except:
                print(("{1}[{0}+{1}]{2} DISPOSITIVOS NO ACTIVOS").format(REDL, GNSL, WHSL))
                main()
            print('''
 0   -->  KEYCODE_UNKNOWN
 1   -->  KEYCODE_MENU
 2   -->  KEYCODE_SOFT_RIGHT
 3   -->  KEYCODE_HOME
 4   -->  KEYCODE_BACK
 5   -->  KEYCODE_CALL
 6   -->  KEYCODE_ENDCALL
 7   -->  KEYCODE_0
 8   -->  KEYCODE_1
 9   -->  KEYCODE_2
 10  -->  KEYCODE_3
 11  -->  KEYCODE_4
 12  -->  KEYCODE_5
 13  -->  KEYCODE_6
 14  -->  KEYCODE_7
 15  -->  KEYCODE_8
 16  -->  KEYCODE_9
 17  -->  KEYCODE_STAR
 18  -->  KEYCODE_POUND
 19  -->  KEYCODE_DPAD_UP
 20  -->  KEYCODE_DPAD_DOWN
 21  -->  KEYCODE_DPAD_LEFT
 22  -->  KEYCODE_DPAD_RIGHT
 23  -->  KEYCODE_DPAD_CENTER
 24  -->  KEYCODE_VOLUME_UP
 25  -->  KEYCODE_VOLUME_DOWN
 26  -->  KEYCODE_POWER
 27  -->  KEYCODE_CAMERA
 28  -->  KEYCODE_CLEAR
 29  -->  KEYCODE_A
 30  -->  KEYCODE_B
 31  -->  KEYCODE_C
 32  -->  KEYCODE_D
 33  -->  KEYCODE_E
 34  -->  KEYCODE_F
 35  -->  KEYCODE_G
 36  -->  KEYCODE_H
 37  -->  KEYCODE_I
 38  -->  KEYCODE_J
 39  -->  KEYCODE_K
 40  -->  KEYCODE_L
 41  -->  KEYCODE_M
 42  -->  KEYCODE_N
 43  -->  KEYCODE_O
 44  -->  KEYCODE_P
 45  -->  KEYCODE_Q
 46  -->  KEYCODE_R
 47  -->  KEYCODE_S
 48  -->  KEYCODE_T
 49  -->  KEYCODE_U
 50  -->  KEYCODE_V
 51  -->  KEYCODE_W
 52  -->  KEYCODE_X
 53  -->  KEYCODE_Y
 54  -->  KEYCODE_Z
 55  -->  KEYCODE_COMMA
 56  -->  KEYCODE_PERIOD
 57  -->  KEYCODE_ALT_LEFT
 58  -->  KEYCODE_ALT_RIGHT
 59  -->  KEYCODE_SHIFT_LEFT
 60  -->  KEYCODE_SHIFT_RIGHT
 61  -->  KEYCODE_TAB
 62  -->  KEYCODE_SPACE
 63  -->  KEYCODE_SYM
 64  -->  KEYCODE_EXPLORER
 65  -->  KEYCODE_ENVELOPE
 66  -->  KEYCODE_ENTER
 67  -->  KEYCODE_DEL
 68  -->  KEYCODE_GRAVE
 69  -->  KEYCODE_MINUS
 70  -->  KEYCODE_EQUALS
 71  -->  KEYCODE_LEFT_BRACKET
 72  -->  KEYCODE_RIGHT_BRACKET
 73  -->  KEYCODE_BACKSLASH
 74  -->  KEYCODE_SEMICOLON
 75  -->  KEYCODE_APOSTROPHE
 76  -->  KEYCODE_SLASH
 77  -->  KEYCODE_AT
 78  -->  KEYCODE_NUM
 79  -->  KEYCODE_HEADSETHOOK
 80  -->  KEYCODE_FOCUS
 81  -->  KEYCODE_PLUS
 82  -->  KEYCODE_MENU
 83  -->  KEYCODE_NOTIFICATION
 84  -->  KEYCODE_SEARCH
 85  -->  TAG_LAST_KEYCODE
            ''')
            print(("{1}[{0}+{1}]{2} INGRESAR OPCION KEYCODE").format(REDL, GNSL, WHSL))
            num = input(arrow + ""+GNSL+"("+REDL + "TECLADO" + GNSL + ")"+ENDL + "> ")
            os.system("adb -s "+device_name+" shell input keyevent "+num)
            option = input(ENDL + ""+GNSL+"("+REDL + "MENU PRINCIPAL" + GNSL + ")"+ENDL + "> ")

        elif option == '25':
            try:
                device_name
            except:
                print(("{1}[{0}+{1}]{2} DISPOSITIVOS NO ACTIVOS").format(REDL, GNSL, WHSL))
                main()
            os.system("adb -s " +device_name+ " shell dumpsys activity")
            option = input(ENDL + ""+GNSL+"("+REDL + "MENU PRINCIPAL" + GNSL + ")"+ENDL + "> ")

        elif option == '26':
            os.system("adb reboot recovery")
            option = input(ENDL + ""+GNSL+"("+REDL + "MENU PRINCIPAL" + GNSL + ")"+ENDL + "> ")

        elif option == '27':
            os.system("adb reboot fastboot")

            option = input(ENDL + ""+GNSL+"("+REDL + "MENU PRINCIPAL" + GNSL + ")"+ENDL + "> ")

        elif option == '':
            option = input(ENDL + ""+GNSL+"("+REDL + "MENU PRINCIPAL" + GNSL + ")"+ENDL + "> ")
            
        elif option == '28':
            print(("{1}[{0}+{1}]{2} CERRANDO SERVIDOR FANTASMA{3}").format(REDL, GNSL, WHSL, ENDL))
            os.system("adb disconnect >> /dev/null")
            os.system("adb kill-server >> /dev/null")
            t.sleep(4)
            exit()
            break
        else:
            print("ERROR EN EL SERVIDOR")
            option = input(ENDL + ""+GNSL+"("+REDL + "MENU PRINCIPAL" + GNSL + ")"+ENDL + "> ")

    main()
    
import os
os.system("printf '\033]2;FANTASMA SCRIPT\a'")
print(("{1}[{0}+{1}]{2} INICIANDO SERVIDOR FANTASMA").format(REDL, GNSL, WHSL))
t.sleep(4)
os.system("adb tcpip 5555 >> /dev/null")
os.system('clear')
t.sleep(3)
os.system('clear')
print("SERVIDOR INICIADO EXITOSAMENTE")
t.sleep(2)
os.system('clear')
print("CARGANDO")
t.sleep(1)
os.system('clear')
print("CARGANDO.")
t.sleep(1)
os.system('clear')
print("CARGANDO..")
t.sleep(1)
os.system('clear')
print("CARGANDO...")
t.sleep(1)
os.system('clear')
print("DISTROS CONOCIDAS: ARCHLINUX")
t.sleep(1)
os.system('clear')
print("DISTROS CONOCIDAS: DEBIAN")
t.sleep(1)
os.system('clear')
print("DISTROS CONOCIDAS: UBUNTU")
t.sleep(1)
os.system('clear')
print("DISTROS CONOCIDAS: KALI")
t.sleep(1)
os.system('clear')
print("CAARGANDO INFO DEL SISTEMA")
t.sleep(1)
os.system('neofetch')
t.sleep(3)
os.system('clear')
print(page_1)
main()
