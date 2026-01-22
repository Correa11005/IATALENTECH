#scikit-learn
import os 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

MODEL_DIR= "models"
MODEL_PATH =os.path.join(MODEL_DIR,"model.pkl")
VECTORIZER_PATH=os.path.join(MODEL_DIR,"vectorizer.pkl")
ANSWERS_PATH=os.path.join(MODEL_DIR,"answers.pkl")

#Funcion de entrenamiento preguntas y respuestas
def build_and_train_model(train_pairs):
    #train_pairs lista de pares (pregunta,respuesta)
    #Ejemplo [ ("hola","Hola!") , ("adios","!hasta luego!")]
    #separamos las preguntas y respuestas en dos listas 
    questions= [q for q, _ in train_pairs] #lista de preguntas
    answers= [a for _, a in train_pairs] #lista de respuestas
    # creamos el vectorizado , que traducira el texto a numeros 
    vectorizer= CountVectorizer()
    #Entrenamiento 
    x= vectorizer.fit_transform(questions)
    # obtenemos una lista de respuestas unicas
    unique_answers= sorted(set(answers))
    # crear el diccionario con las etiquetas 
    answer_to_label={a: i for i, a in enumerate (unique_answers)}
    #creamos una lista
    y=[answer_to_label[a] for a in answers]
    #modelo clasificacion de texto 
    model = MultinomialNB()
    #entrenar el modelo 
    model.fit(x,y)
    #crear carpeta para guardar el modelo si no existe 
    os.makedirs(MODEL_DIR,exist_ok=True)
    #guardar los objetos entrenados 
    with open (MODEL_DIR,"wb") as f:
        pickle.dump (model,f)
    return model,vectorizer,unique_answers 
#funcion predict_answer
def predict_answer(model,vectorizer,unique_answers,user_text):
    # convertimos el texto a numeros
    x = vectorizer.transform ([user_text])
    # el modelo predice la etiqueta de la respuesta correcta
    label = model.predict(x)[0]
    return unique_answers[label]
# programa principal 
if __name__ =="__main__":
    training_data =[
    ("hola","!Hola! En que puedo ayudarte?"),
    ("buenos días", "¡Buenos días! ¿Cómo puedo apoyarte hoy?"),
    ("buenas tardes", "¡Buenas tardes! ¿En qué puedo asistirte?"),
    ("buenas noches", "¡Buenas noches! ¿Cómo puedo ayudarte?"),
    ("informacion", "Con gusto te brindamos la información que necesitas."),
    ("contacto", "Puedes comunicarte con nuestro equipo al correo Jacobocorrea777@gmail.com"),
    ("gracias", "¡Con gusto! Estamos para servirte.")

        ]
    #entrenar el modelo con la lista 
    model,vectorizer,unique_answers=build_and_train_model(training_data)
    #mostrar un mensaje inicial al usuario 
    print:("Chatbot supervisado listo,Escribe Salir para terminar.\n")
    while True: 
        #pedimos una frase al usuario 
        user =input("Tu: ").strip()
        if user.lower() in {"salir","exit","quit"}:
            print("Bot: !Hasta pronto!")
            break
        response=predict_answer(model,vectorizer,unique_answers,user)
        print("Bot: ",response)