            ################################
            ### CARGA DE DFs y LIBRERIAS ###
            ################################

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from fastapi import FastAPI
import uvicorn #servidor ASGI(Asynchronous Server Gateway Interface)
from collections import Counter

# Consulta 'developer(desarrollador: str)'
df_steam_games_developer_desarrollador = pd.read_parquet('./Data/df_steam_games_developer_desarrollador.parquet')

# Consulta 'userdata(user_id:str)
df_user_items_userdata_user_id_respuesta1 = pd.read_parquet('./Data/df_user_items_userdata_user_id_respuesta1.parquet')
df_steam_games_userdata_user_id_respuesta1 = pd.read_parquet('./Data/df_steam_games_userdata_user_id_respuesta1.parquet')
df_user_reviews_userdata_user_id_respuesta2 = pd.read_parquet('./Data/df_user_reviews_userdata_user_id_respuesta2.parquet')

# Consulta 'UserForGenre(genero: str)'
df_steam_games_userforgenre_genero = pd.read_parquet('./Data/df_steam_games_userforgenre_genero.parquet')
df_user_items_userforgenre_genero = pd.read_parquet('./Data/df_user_items_userforgenre_genero.parquet')

# Consulta 'best_developer_year(año : int)'
df_user_reviews_best_developer_year_año = pd.read_parquet('./Data/df_user_reviews_best_developer_year_año.parquet')
df_steam_games_best_developer_year_año = pd.read_parquet('./Data/df_steam_games_best_developer_year_año.parquet')

# Consulta 'developer_reviews_analysis( desarrolladora: str)'
# Esta consulta reutiliza los dataframes:
#   df_steam_games_best_developer_year_año
#   df_user_reviews_best_developer_year_año

# Consulta 'recomendacion_usuario(user_id: srt)'
df_recommendacion_usuario_user_id = pd.read_parquet('./Data/df_recommendacion_usuario_user_id.parquet')


app = FastAPI() #crea un objeto app(una instancia de FastAPI), que se usará para definir las rutas y las operaciones que realizará la API.



            ################################################
            ### CONSULTA 'developer(desarrollador: str)' ###
            ################################################ 
@app.get('/developer/')
def developer(desarrollador: str):
    try:
        # Asegúrate de convertir 'release_date' a objetos datetime
        df_steam_games_developer_desarrollador['release_date'] = pd.to_datetime(df_steam_games_developer_desarrollador['release_date'], format='%Y-%m-%d')

        # Acceder a los años
        df_steam_games_developer_desarrollador['año'] = df_steam_games_developer_desarrollador['release_date'].dt.year

        # Filtrar el DataFrame para obtener registros de la empresa desarrolladora especificada
        df_desarrolladora = df_steam_games_developer_desarrollador[df_steam_games_developer_desarrollador['developer'] == desarrollador]

        # Calcular la cantidad de elementos por año
        elementos_por_anio = df_desarrolladora['año'].value_counts().reset_index()
        elementos_por_anio.columns = ['Año', 'Cantidad de Items']

        # Calcular el porcentaje de contenido "Free" por año
        contenidos_free_por_anio = df_desarrolladora['año'][df_desarrolladora['genres'].str.contains('Free to Play')].value_counts().reset_index()
        contenidos_free_por_anio.columns = ['Año', 'Contenido Free']

        # Combinar los dataFrames de cantidad de elementos y contenido "Free"
        resultados = elementos_por_anio.merge(contenidos_free_por_anio, on='Año', how='left').fillna(0)
        resultados['Contenido Free'] = (resultados['Contenido Free'] / resultados['Cantidad de Items'] * 100).astype(int).astype(str) + '%'

        respuesta1 = f"Desarrollador: {desarrollador}"
        datos_por_anio = [{"Año": int(row['Año']), "Items": row['Cantidad de Items'], "Porcentaje Free": row['Contenido Free']} for index, row in resultados.iterrows()]
        respuesta2 = f"Cantidad de items y contenido free por año: {datos_por_anio}"
        return respuesta1, respuesta2
    except Exception as e:
        return {"error": str(e)}


            ########################################
            ### CONSULTA 'userdata(user_id:str)' ###
            ########################################
@app.get('/userdata/')
def userdata(user_id:str):
    try:
        # RESPUESTA 1        
        # Filtra las filas correspondientes al 'user_id' en df_user_items_userdata_user_id_respuesta1.
        user_items = df_user_items_userdata_user_id_respuesta1[df_user_items_userdata_user_id_respuesta1['user_id'] == user_id]

        # Utiliza los 'item_id' del usuario para filtrar las filas correspondientes en df_steam_games_userdata_user_id_respuesta1.
        user_game_prices = df_steam_games_userdata_user_id_respuesta1[df_steam_games_userdata_user_id_respuesta1['id'].isin(user_items['item_id'])]
        
        # Reemplaza 'Alan' con '0' en la columna 'mi_columna'
        user_game_prices['price'] = pd.to_numeric(user_game_prices['price'], errors='coerce')

        # Calcula la cantidad total gastada por el usuario sumando los precios de los juegos.
        total_gastado = user_game_prices['price'].sum()
        resp1 = f"El usuario {user_id} ha gastado un total de ${total_gastado:.2f} en juegos."

        # RESPUESTA 2
        # Filtra las recomendaciones del usuario con el 'User_id' especificado.
        user_recommendations = df_user_reviews_userdata_user_id_respuesta2[df_user_reviews_userdata_user_id_respuesta2['user_id'] == user_id]

        # Calcula el porcentaje de recomendación en base a las recomendaciones del usuario.
        if len(user_recommendations) > 0:
            porcentaje_recomendacion = (user_recommendations['recommend'].sum() / len(user_recommendations)) * 100
        else:
            porcentaje_recomendacion = 0
        resp2 = f"El porcentaje de recomendaciones positivas dadas por el usuario {user_id} es de: {porcentaje_recomendacion:.2f}%"

        # RESPUESTA 3
        # Calcula la cantidad de elementos para ese usuario.
        cantidad_elementos = len(user_items)

        # El resultado 'cantidad_elementos' contendrá la cantidad de elementos para el usuario.
        resp3 = f"El usuario {user_id} tiene {cantidad_elementos} juegos en su catalogo."

        #Retornamos las respuestas
        return resp1, resp2, resp3
    except Exception as e:
        return {"error": str(e)}


            ############################################
            ### CONSULTA 'UserForGenre(genero: str)' ###
            ############################################
@app.get('/UserForGenre/')
def UserForGenre(genero: str):
    try:
        # Filtrar juegos por género
        genre_games = df_steam_games_userforgenre_genero[df_steam_games_userforgenre_genero['genres'].str.contains(genero, case=False, na=False)]

        if len(genre_games) == 0:
            response = {"No se encontraron juegos para el género especificado"}
            #raise ValueError("No se encontraron juegos para el género especificado")
        else:
            # Combinar información del usuario y juegos por 'item_id'
            merged_data = df_user_items_userforgenre_genero.merge(genre_games, left_on='item_id', right_on='id')
            
            # Convertir 'release_date' a año
            merged_data['release_date'] = pd.to_datetime(merged_data['release_date']).dt.year

            # Encontrar el usuario con más horas jugadas para el género dado
            user_with_most_playtime = merged_data.groupby('user_id')['playtime_forever'].sum().idxmax()

            # Filtrar los datos solo para el usuario con más horas jugadas en el género dado
            user_data = merged_data[merged_data['user_id'] == user_with_most_playtime]

            # Calcular las horas jugadas por año para el usuario
            user_playtime_by_year = user_data.groupby(user_data['release_date'])['playtime_forever'].sum().reset_index()
            user_playtime_by_year = [{"Año": int(row['release_date']), "Horas": round(int(row['playtime_forever'])/60)} for index, row in user_playtime_by_year.iterrows()]
            resp1 = f"Usuario con más horas jugadas para {genero}: {user_with_most_playtime}"
            #resp1 = "Usuario con más horas jugadas para {}".format(genero): user_with_most_playtime
            resp2 = f"Horas jugadas por año: {user_playtime_by_year}" 
 
        return resp1, resp2 
    except Exception as e:
        return {"error": str(e)}




            #################################################
            ### CONSULTA 'best_developer_year(año : int)' ###
            #################################################
@app.get('/best_developer_year/')
def best_developer_year(año: int):
    try:        
        # Convertir el campo 'posted' a tipo fecha
        df_user_reviews_best_developer_year_año['posted'] = pd.to_datetime(df_user_reviews_best_developer_year_año['posted'])

        # Filtrar las reseñas para el año específico y con 'recommend' igual a True
        filtered_reviews = df_user_reviews_best_developer_year_año[(df_user_reviews_best_developer_year_año['posted'].dt.year == año) & (df_user_reviews_best_developer_year_año['recommend'] == True)]

        # Filtrar las reseñas con valoraciones positivas o neutrales ('sentiment_analysis' 1 o 2)
        filtered_reviews = filtered_reviews[(filtered_reviews['sentiment_analysis'] == 1) | (filtered_reviews['sentiment_analysis'] == 2)]
            
        if filtered_reviews.empty:
            response = ["No hay registros para el año ingresado"]
        else:
            # Unir los datos de las reseñas con los datos de los juegos
            merged_data = filtered_reviews.merge(df_steam_games_best_developer_year_año, left_on='item_id', right_on='id')

            # Contar la cantidad de recomendaciones por juego y encontrar el top 3
            top_3_devs = merged_data['developer'].value_counts().head(3)

            # Eliminar los números
            nombres_devs = list(top_3_devs.keys())

            # Crear el resultado en el formato deseado
            response = [{f'Puesto {i+1}': dev} for i, dev in enumerate(nombres_devs)]

        return response
    except Exception as e:
        return {"error": str(e)}


            ###################################################################
            ### CONSULTA 'developer_reviews_analysis( desarrolladora: str)' ###
            ###################################################################
@app.get('/developer_reviews_analysis/')
def developer_reviews_analysis(desarrolladora: str):
    try:     
        # Filtrar los juegos de la desarrolladora específicada
        games_in_dev = df_steam_games_best_developer_year_año[df_steam_games_best_developer_year_año['developer'] == desarrolladora]

        # Obtener los IDs de los juegos de la desarrolladora específicada
        game_ids = games_in_dev['id'].tolist()
        del games_in_dev

        # Filtrar las reseñas para los juegos de la desarrolladora específicada
        filtered_reviews = df_user_reviews_best_developer_year_año[df_user_reviews_best_developer_year_año['item_id'].isin(game_ids)]

        if len(game_ids) == 0:
            response = {"No se han encontrado juegos para la desarrolladora ingresada"}
        elif filtered_reviews.empty:
            response = {"No hay reseñas para la desarrolladora ingresada"}
        else:
            # Crear un contador de valoraciones
            sentiment_counter = Counter(filtered_reviews['sentiment_analysis'])

            # Obtener la cantidad de reseñas en cada categoría
            negativas = sentiment_counter[0]
            positivas = sentiment_counter[2]

            # Crear la respuesta en el formato especificado
            response = {f'{desarrolladora} : [Valoraciones Negativas = {negativas}, Valoraciones Positivas = {positivas}]'}
            #response = {desarrolladora: {"Valoraciones Negativas": negativas, "Valoraciones Positivas": positivas}}
        del game_ids
        return response
    except Exception as e:
        return {"error": str(e)}


            ######################################################
            ### CONSULTA 'recomendacion_usuario(user_id: str)' ###
            ######################################################

@app.get('/recomendacion_usuario/')
def recomendacion_usuario(user_id: str):
    # df_colaborativo = df_recommendacion_usuario_user_id
    try:
        # Crear una matriz de usuarios y juegos
        columnas_a_mantener = ['user_id','item_id']
        df_colaborativo = df_recommendacion_usuario_user_id[columnas_a_mantener]
        user_item_matrix = df_colaborativo.pivot_table(index='user_id', columns='item_id', aggfunc=lambda x: 1, fill_value=0)
        del df_colaborativo


        # Calcular similitud de coseno entre usuarios
        user_similarity = cosine_similarity(user_item_matrix)
        user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)
        del user_similarity


        # Procesamos las Recomendaciones

        # Obtener las puntuaciones de similitud para el usuario especificado
        user_scores = user_similarity_df.loc[user_id]
        del user_similarity_df

        # Ordenar los usuarios por similitud en orden descendente
        user_scores = user_scores.sort_values(ascending=False)

        # Filtrar los juegos que el usuario ya ha jugado
        user_played_games = user_item_matrix.loc[user_id]
        already_played = user_played_games[user_played_games == 1].index
        del user_played_games

        # Obtener recomendaciones para el usuario
        recommendations = user_item_matrix.columns.difference(already_played)
        del already_played
        user_recommendations = user_scores.dot(user_item_matrix.loc[:, recommendations])
        del user_item_matrix
        del user_scores

        # Ordenar las recomendaciones por puntaje en orden descendente
        user_recommendations = user_recommendations.sort_values(ascending=False)

        # Capturar las 5 primeras recomendaciones y convertir la serie a DF
        df_top5_recomendaciones = user_recommendations.head(5).reset_index()
        del user_recommendations

        # Cambiar el nombre de las columnas del DataFrame
        df_top5_recomendaciones.columns = ['item_id', 'score']

        # Agregar el campo 'nombre de juego' y descartar el resto
        df_top5_recomendaciones = df_top5_recomendaciones.merge(df_recommendacion_usuario_user_id[['item_id', 'item_name']], on='item_id')
        df_top5_recomendaciones = df_top5_recomendaciones.drop_duplicates()
        df_top5_recomendaciones = df_top5_recomendaciones['item_name']

        # Mostrar el DataFrame resultante
        lst_top5_recomendaciones = df_top5_recomendaciones.reset_index(drop=True).tolist()
        del df_top5_recomendaciones
        response = f'Recomendaciones para el usuario {user_id}: {lst_top5_recomendaciones}'


        return response
    except Exception as e:
        return {"error": str(e)}


    # Run the API with uvicorn
    if __name__ == '__main__':
        uvicorn.run(app, host='127.0.0.1', port=8000)



'''
Ejecucion de la API

En PS ejecutar: uvicorn app:app --reload 
En Opera tipear:
    http://127.0.0.1:8000/docs
'''