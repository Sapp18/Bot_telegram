from setuptools.command.saveopts import saveopts

import Apykey as keys #IMPORTANDO EL TOKEN DE ACCESO DEL BOT CREADO EN TELEGRAM
from telegram.ext import * #IMPORTANDO LAS EXTENSIONES DE PYTHON-TELEGRAM-BOT
import Respuestas as R #IMPORTANDO LAS POSIBLES RESPUESTAS
import json #LIBRERIA PARA GENERAR EL ARCHIVO JSON
print('Empezando bot...') #MENSAJE PARA VERIFICAR QUE EL BOT HAYA EMPEZADO 

preguntas = { #DICCIONARIO PARA AGREGAR LAS PREGUNTAS A REALIZAR, SI SE DESEA AGREGAR UNA NUEVA PREGUNTA SIGA EL EJEMPLO
    1: 'como te llamas?',
    2: 'cual es tu fruta favorita?',
    3: 'que carro es tu favorito?',
    4: 'cuantos hermanos tienes?',
    5: 'lenguaje de programacion preferido?',
    #6: 'lenguaje de programacion preferido?', #EJEMPLO, LOS NUMEROS TIENEN QUE IR CONSECUTIVOS
}

contador = 0  # AUXILIAR PARA RECORRER EL DICCIONARIO

respuestas = {  # DICCIONARIO VACIO PARA ALMACENAR LAS RESPUESTAS

}


def start_command(update, context): #FUNCION DE INICIO DEL BOT
    update.message.reply_text('Escriba algo al azar para empezar.')


def help_command(update, context): #FUNCION DE AYUDA DEL BOT
    update.message.reply_text('Si necesita ayuda, pongase en contacto con el desarrollador.')


def handle_message(update, context): #FUNCION INICIAL (DE PRUEBA) QUE SE TENIA PARA COMUNICARSE CON EL BOT
    text = str(update.message.text).lower()
    response = R.sample_responses(text)
    update.message.reply_text(response)


def error(update, context): #FUNCION DE ERROR
    print(f'Actualizar {update} error causado {context.error}')


def save_answer(user_input): #FUNCION PARA ALMACENAR LAS RESPUESTAS EN EL DICCIONARIO
    global contador
    respuestas[contador] = user_input  # ALMACENA LAS RESPUESTAS EN EL DICCIONARIO


def reply(update, input_text): #FUNCION PRINCIPAL
    global contador
    if contador > 0:  # VALIDAR QUE LA ENCUESTA HAYA EMPEZADO
        save_answer(update.message.text)  # GUARDA LA RESPUESTA DEL USUARIO
    if contador < len(preguntas):  # CONDICION PARA MOSTRAR CADA UNA DE LAS PREGUNTAS
        contador += 1
        update.message.reply_text(preguntas[contador])  # REALIZA CADA PREGUNTA QUE SE TENGA ALMACENADA
    else:
        update.message.reply_text('Gracias por su tiempo, la encuesta terminó.')  # FINALIAZACION DE LA ENCUESTA
        with open('preguntas_y_respuestas.json', 'a') as f: #ABRIR EL ARCHIVO .JSON 
            json.dump(preguntas, f, indent=4, sort_keys=True) #GUARDA EL DICCIONARIO DE LAS PREGUNTAS
            json.dump(respuestas, f, indent=4, sort_keys=True) #GUARDA EL DICCIONARIO DE LAS RESPUESTAS
        print(preguntas) #IMPRIME EL DICCIONARIO DE preguntas EN CONSOLA PARA VERFIFICAR LOS DATOS
        print(respuestas) #IMPRIME EL DICCIONARIO DE respuestas EN CONSOLA PARA VERFIFICAR LOS DATOS


def main():
    updater = Updater(keys.API_KEY, use_context=True) 
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start_command)) #MANDA A LLAMAR LA FUNCION DE start_command
    dp.add_handler(CommandHandler('help', help_command)) #MANDA A LLAMAR LA FUNCION DE  help_command

    # dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_handler(MessageHandler(Filters.text, reply)) #MANDA A LLAMAR LA FUNCION DE reply

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
