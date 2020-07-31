def detect_intent_text(SESSION_ID,texto):
    import os
    import dialogflow_v2 as dialogflow
    
    from google.api_core.exceptions import InvalidArgument

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'dio-techchallenge_config.json'

    DIALOGFLOW_PROJECT_ID = 'dio-techchallenge-m9nu' #Project ID obtido no arquivo de chave do DialogFlow
    DIALOGFLOW_LANGUAGE_CODE = 'pt-BR'  #Linguagem da conversa
    #SESSION_ID = 'me'  #String de o max 36 bits. Identicador da sessão

    text_to_be_analyzed = texto

    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
    text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        print('Falha no processo de análise do Intent do DialogFlow')
        raise

    # print("Query text:", response.query_result.query_text)
    # print("Detected intent:", response.query_result.intent.display_name)
    # print("Detected intent confidence:", response.query_result.intent_detection_confidence)
    # print("Fulfillment text:", response.query_result.fulfillment_text)
    return response.query_result.fulfillment_text
