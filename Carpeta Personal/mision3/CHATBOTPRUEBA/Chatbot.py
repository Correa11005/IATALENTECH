import pandas as pd

df = pd.read_excel("ventas.xlsx")
print(df.head())
print(df.columns)


import os
os.environ["GROQ_API_KEY"]
from groq import Groq
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")

)
chat_completion = client.chat.completions.create( 
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content":(
                "Eres un experto en Microsoft Excel y analisis de datos "
                "Tu tarea es interpretar instrucciones en lenguaje natural "
                "y extraer la instruccion del usuario. \n\n"
                "Debes identificar:\n"
                "- la accion principal (sumar,filtrar,ordenar,agrupar,etc.)\n"
                "- las columnas involucradas \n"
                "- las condiciones si existen \n"
                "Devuelve SIEMPRE la respuesta en formato JSON con esta estructura: \n"
                "{\n"
                ' "accion":"",\n'
                '"columnas":[],\n'
                '"condiciones":[],\n'
                '"resultado":""\n'
                "}"

            )

         },
         {
            "role":"user", 
            "content":"Quiero sumar las ventas por vendedor solo del año 2024"

         }
   ]
)
print(chat_completion.choices[0].message.content)

