"""""
tp2-con cheatGPT y analizando el codigo con libreria como multimetric y pylint
"""""
import sys
import openai




class SinContenidoError(Exception): #asi se crea una exception q deriva de la clase madre Exception
    """""
    clase que deriva de Exception
    """""

class ArgumentNoExiste(Exception):
    """""
    clase que deriva de Exception
    """""
TOP_P=1
FREQ_PENALTY=0
PRES_PENALTY=0
STOP=None
MAX_TOKENS=1024
TEMPERATURE=0.75
NMAX=1
MODEL_ENGINE = "text-davinci-003"

def get_respuesta(preguntaa):
    """""
    metodo para obtener la respuesta de chatGPT
    """""
    completion = openai.Completion.create(
                                            engine=MODEL_ENGINE,
                                            prompt=preguntaa,
                                            max_tokens=MAX_TOKENS,
                                            n=NMAX,
                                            top_p=TOP_P,
                                            frequency_penalty=FREQ_PENALTY,
                                            presence_penalty=PRES_PENALTY,
                                            temperature=TEMPERATURE,
                                            stop=STOP)
    #print('aa: ',completion)
    return completion.choices[0].text

openai.api_key= "-API-KEY-"

pregunta=""
conversation=""
if len(sys.argv)==1:    #si no ingreso nada como argumento entonces es modo consulta
    while pregunta!='exit':
        try:
            print('MODO CONSULTA')
            print('para salir escriba exit')
            pregunta=input('escriba su consulta:')
            if pregunta=="":    #si el usuario no escribe nada se lanza una exception creada por mi
                raise SinContenidoError
            if pregunta!='exit':
                respuesta_chatGPT = get_respuesta(pregunta)
                print('you: ',pregunta)
                print('chatGPT: ',respuesta_chatGPT)

        except SinContenidoError:
            print('no has escrito nada')
else:
    try:    #eligio un modo conversacion
        #si el argumento  es --convers entra en modo conversacion
        #(recordando todo lo q dice el usuario)
        if sys.argv[1]=='--convers':
            print('MODO CONVERSACION')
            while pregunta!='exit':
                try:
                    print('para salir escriba exit')
                    pregunta = input("You: ")
                    if pregunta=="":#si el usuario no escribe nada se lanza una exception
                        raise SinContenidoError
                    if pregunta!='exit':
                        conversation += "\nYou:" + pregunta + "\nChatGPT:"
                        STOP = ["\n", " You:", " ChatGPT:"]
                        respuesta_chatGPT = get_respuesta(conversation)
                        conversation += respuesta_chatGPT
                        print('chatGPT: ',respuesta_chatGPT)
                except SinContenidoError:
                    print('no has escrito nada')
        else:   #si el argumento es es diferente a --convers lanzara una exception
            raise ArgumentNoExiste
    except ArgumentNoExiste:
        print('argumento no existe')
