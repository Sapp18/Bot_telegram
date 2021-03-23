def sample_responses(input_text): #FUNCION DE PRUEBA PARA CONTESTAR AL USUARIO 
    
    user_message = str(input_text).lower() #LEE EL MENSAJE DEL USUARIO Y LO CONVIERTE EN MINUSCULAS PARA QUE EL BOT LO PUEDA PROCESAR MAS FACIL
    if user_message in ('hola', 'holi', 'que onda',): #CONDICION PARA SABER SI EL USUARIO PONE ALGUNO DE ESOS TEXTOS
        return 'Hola.' #SI EL USUARIO PUSO ALGO DEL TEXTO DE ARRIBA, LE CONTESTARA Hola

    elif user_message in ('quien eres', 'quién eres', 'quien eres?', 'quién eres?', ): #CONDICION PARA SABER SI EL USUARIO PONE ALGUNO DE ESOS TEXTOS
        return 'Soy un boot programado para realizar una encuesta.' #SI EL USUARIO PUSO ALGO DEL TEXTO DE ARRIBA, LE CONTESTARA Soy un boot programado para realizar una encuesta

    return 'Lo siento, no te entiendo.' #FINALMENTE SI NINGUNA ENTRADA COINCIDE CON LO MENCIONADO, LE CONTESTARA Lo siento, no te entiendo