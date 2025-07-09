import pyttsx3,speech_recognition as sr,pywhatkit,webbrowser,datetime,wikipedia


#escuchar microfono y devolverlo como texto
def audio_a_texto():

    #colocamos el recognizer en una variable
    r = sr.Recognizer()

    #configuramos microfono
    with sr.Microphone() as origen:
        #tiempo de espera
        r.pause_threshold = 0.8

        #se informa que comenzo la grabacion
        print("Ya podes hablar")

        #se guarda en una variable lo que se escucha
        audio = r.listen(origen)

        try:
            #buscar en google
            pedido=r.recognize_google(audio,language="es-ar")

            #prueba de que ingreso

            return pedido
        #si no se comprende el audio
        except sr.UnknownValueError:
            return "Hubo un error inesperado"
        except sr.RequestError:
            return "Hubo un error en el pedido"
        except:
            return "Hubo un error"

#funcion para que el asistente hable
def hablar(mensaje):
    #encender el motor
    engine = pyttsx3.init()
    #pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()

#informar dia
def pedir_dia():
    #crear datos de hoy
    dia=datetime.date.today()
    #dia de semana
    dia_semana=dia.weekday()
    #diccionario con dias
    calendario={0:"Lunes",
                1:"Martes",
                2:"Miercoles",
                3:"Jueves",
                4:"Viernes",
                5:"Sabado",
                6:"Domingo"}
    hablar(f"Hoy es {calendario[dia_semana]}")

#informar hora
def pedir_hora():
    hora=datetime.datetime.now()
    if hora.hour==1:
        hablar(f"Son la {hora.hour} y {hora.minute}")
    hablar(f"Son las {hora.hour} y {hora.minute}")

#se define el saludo del asistente al iniciar
def saludo():
    hora=datetime.datetime.now()

    #segun la hora, saludara de una manera u otra
    if hora.hour>=6 and hora.hour<12:
        momento="Buen dia"
    elif hora.hour>=12 and hora.hour<20:
        momento="Buenas tardes"
    else:momento="Buenas noches"

    hablar(f"{momento}, soy tu asistente personal, porfavor dime que necesitas.")

#funcion principal del asistente
def pedidos():
    #nos saluda
    saludo()

    #variable de corte
    comenzar=True
    while comenzar:
        #activar micro y guardar pedido
        ped=audio_a_texto().lower()

        #se configuran las distintas posibilidades y como actua el asistente frente a lo que pedimos
        if "abrir youtube" in ped:
            hablar("Abriendo youtube")
            webbrowser.open("https://www.youtube.com")
            continue
        elif "abrir google" in ped:
            hablar("Abriendo navegador")
            webbrowser.open("https://www.google.com")
            continue
        elif "qué hora es" in ped:
            pedir_hora()
            continue
        elif "qué día es" in ped:
            pedir_dia()
            continue
        elif "buscar en wikipedia" in ped:
            hablar("Buscando en wikipedia")
            ped=ped.replace("buscar en wikipedia","")
            wikipedia.set_lang("es")
            resultado=wikipedia.summary(ped,sentences=1)
            hablar(resultado)
            continue
        elif "busca en internet" in ped:
            hablar("Buscando en internet")
            ped=ped.replace("busca en internet","")
            pywhatkit.search(ped)
            continue
        elif "en youtube" in ped:
            hablar("Buscando en youtube")
            ped=ped.replace("en youtube","")
            pywhatkit.playonyt(ped)
            continue

        elif "finalizar programa" in ped:
            hablar("Finalizando programa")
            comenzar=False




pedidos()