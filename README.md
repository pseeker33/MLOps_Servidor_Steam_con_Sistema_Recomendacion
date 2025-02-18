# <h1 align=center> **`MLOps PROJECT`** </h1>

# <h1 align=center>**`Implementation of a Steam Query Server`**</h1>

<p align="center">
    <img src="./src/steam_portada1.jpg"  height=450>    
</p>
<br>

<p align="center">
    Check out the live demo of this project 
    <a href="https://simple-bank-dapp-fawn.vercel.app">HERE</a>
</p>

<p align="center">
    Read this in <a href="README-es.md">Spanish</a> / Lee este archivo en <a href="README-es.md">español</a>
</p>

<br>

<hr> 

## Table of Contents

1. **[Introduction](#1-introduction)**
2. **[Project Scope](#2-project-scope)**
3. **[Repository Structure](#3-repository-structure)**
4. **[Getting Started](#4-getting-started)**
5. **[Tech Stack](#5-tech-stack)**
6. **[Workflow](#6-workflow)**
7. **[Next Steps](#7-next-steps)**
8. **[Contact](#8-contact)**

<br>

## **1. Introduction**

**A Brief History of Video Games**

Since the 1950s, laboratories began designing the first video games, which would serve both to test the technical capabilities of the electronic systems at their disposal, and of the first computers built in those times. 

Notable from this period is the game 'Tennis for Two', developed in 1958 by William Higinbotham of the Brookhaven National Library, using an oscilloscope screen and transistor circuitry.
Another important development was 'Spacewar!', the first computerized game in history, developed in 1962 by MIT student Steve Russell, applying vector graphics on a PDP-1 minicomputer.
These first video games did not have a commercial purpose. 

<div style="display: flex; justify-content: center;">
    <div style="margin-right: 60px;">
        <img src="./src/Tennis-for-Two.jpg" height=250>
    </div>
    <div>
        <img src="./src/Spacewar.jpg" height=250>
    </div>
</div>

<br>

It wasn't until the 70s with the video game 'Computer Space' of 1971, based on Spacewar! of 1962, that the video game market started, with 'Pong' from Atari in 1972 being the cornerstone of the video game as an industry in those days. 

In the 80s a new era began in the industry where Namco developed Pac Man, Atari created Space Invaders and where later the Japanese Nintendo became the market leader with titles like Donkey Kong, Super Mario Bros and Tetris. 

In the nineties, with the advancement of chip technology, console manufacturers became the locomotives of the industry; Nintendo's monopoly ended and the console war began between Nintendo, Sega, Sony and later, Microsoft.
Today in the console market Sony competes with its Playstation, Microsoft with Xbox, and Nintendo with its Wii console.

<p align="center">
    <img src="./src/juegos_crono.png"  height=600>    
</p>

**The Role of Development in the Video Game Industry**

The video game industry is an economic sector that involves the development, distribution and sale of video games, as well as all associated hardware. 
In this chain, development is the most important stage, because although it is similar to any software development, here the artistic component takes much more force due to the importance of the interface, the soundtrack, the story, the character design, etc. 

<!-- <p align="center">
    <img src="./src/cadena_valor.png"  height=500>            
</p> -->

<br>

It is important to point out that, although the large conglomerates of developers lead the video game market, leaving less room for small and medium-sized enterprises, it is also true that the dynamism that characterizes this industry, coupled with continuous technological advances, is currently creating and will continue to create new business opportunities. 
<span style="float:right;">[top](#table-of-contents)</span> 

<br>

## **2. Project Scope**

This project aims to **develop an online query server that accepts requests for user data and games available on the Steam digital platform**.

To carry out this development, three raw datasets were used as a data source.

From these datasets, and applying **Data Preparation**, **Data Modeling** and **Deployment** processes using Restful API, a query server was implemented in the form of a minimum viable product (MVP) that meets the essential development and deployment requirements.

<span style="float:right;">[top](#table-of-contents)</span> 

<br>

## **3. Repository Structure**

<p align="center">  
    <img src="./src/estructura_repo.png"  height=500>      
</p>

<br>

**`app.py`**: Main file containing the implementation of the API and the endpoints for each query.

**`Data Prep`**: Folder with Jupyter notebooks for data preparation (cleaning and transformation) for standard queries and the recommendation system:
    * `australian_users_items_json.ipynb`: Data preparation of the `australian_users_items_json.ipynb` dataset.
    * `australian_user_reviews_json.ipynb`: Data preparation of the `australian_user_reviews_json.ipynb` dataset.
    * `output_steam_games_json.ipynb`: Data preparation of the `output_steam_games_json.ipynb` dataset.
    * `Preprocesamiento.ipynb`: Data preparation (merging of intermediate datasets) for the recommendation system.

**`Data`**: Folder with the prepared datasets ready to be used by the `app.py` endpoints.

**`README.md`**: This file.

**`src`**: Folder with source files (images, diagrams, etc.).

**`requirements.txt`**: File with the list of dependencies needed for deployment on Render.
<span style="float:right;">[top](#table-of-contents)</span> 

<br>

## **4. Getting Started**

### ️🛠️ Installation

1. Clone the repository:

    ```bash
    git clone [https://github.com/pseeker33/mlops-steam-api.git](https://github.com/pseeker33/mlops-steam-api.git)
    cd steam-api
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### ▶️ Execution

1. Make sure you have the Parquet files in `data/`.

2. Start the FastAPI API on your local environment:

    ```bash
    uvicorn app.main:app --reload
    ```

<span style="float:right;">[top](#table-of-contents)</span> 

<br>

## **5. Tech Stack**

![Static Badge](https://img.shields.io/badge/PYTHON%203-%233776AB?logo=python&labelColor=%231F1F1F)  
![Static Badge](https://img.shields.io/badge/JUPYTER%20NOTEBOOK-%23F37626?style=plastic&logo=jupyter&labelColor=%235C5C5C)  
![Static Badge](https://img.shields.io/badge/PANDAS-%23F5F5F5?style=plastic&logo=pandas&labelColor=%235C5C5C)  
![Static Badge](https://img.shields.io/badge/NUMPY-%234DABCF?style=plastic&logo=numpy&logoColor=%234DABCF&labelColor=%235C5C5C)  
![Static Badge](https://img.shields.io/badge/SCIKIT_LEARN-%23F7931E?style=plastic&logo=scikitlearn&labelColor=5C5C5C&color=%23F7931E)  
![Static Badge](https://img.shields.io/badge/FASTAPI-%23009688?style=plastic&logo=fastapi&logoColor=%23009688&labelColor=%235C5C5C)  
![Static Badge](https://img.shields.io/badge/UVICORN-%23499848?style=plastic&logo=gunicorn&logoColor=%23499848&labelColor=%235C5C5C) 

<span style="float:right;">[top](#table-of-contents)</span> 

<br>

## **6. Workflow**

### Data Preparation Stage <a name="data_preparation"></a>

This is the stage where most of the work was done. It has two distinct parts:

1. **Cleaning and transformation of raw datasets:** Data cleaning and data transformation treatments are performed on the raw datasets.
2. **Creation of endpoint datasets:** The final transformations are carried out, creating the final datasets that must be consumed by both the standard query endpoints and the recommendation system query endpoint.

The treatments performed on each dataset are summarized below:

**`australian_users_items_json.ipynb`**:

<p align="left">  
    <img src="./src/users_items_crudo.png"  height=300>        
</p>
<p align="left">  
    <img src="./src/users_items_endpoints.png"  height=230>        
</p>

<br>

**`australian_user_reviews_json.ipynb`**:

<p align="left">  
    <img src="./src/user_reviews_crudo.png"  height=350>        
</p>
<p align="left">  
    <img src="./src/user_reviews_endpoints.png"  height=250>        
</p>

<br>

**`output_steam_games_json.ipynb`**:

<p align="left">  
    <img src="./src/steam_games_crudo.png"  height=300>        
</p>
<p align="left">  
    <img src="./src/steam_games_endpoints.png"  height=250>        
</p>

<br>

**`Preprocesamiento.ipynb`**:

<p align="left">  
    <img src="./src/preprocesamiento.png"  height=300>        
</p>

<br>

### Deployment Stage <a name="deployment"></a>

Stage where the server API interface was implemented within the `app.py` file. The code consists of a series of response functions to the server queries for each endpoint.

Here is a summary of the **endpoints** you have in your FastAPI project:

---

#### 1. **`/developer/`** (GET) 
- **Parameter:** `developer` (str) 
- **Description:** 
    - Returns the number of games per year for a developer. 
    - Calculates the percentage of "Free to Play" games per year. 

---

#### 2. **`/userdata/`** (GET) 
- **Parameter:** `user_id` (str) 
- **Description:** 
    - Shows the total spent by a user on games. 
    - Calculates the percentage of positive recommendations made by the user. 
    - Indicates the number of games the user has in their catalog. 

---

#### 3. **`/UserForGenre/`** (GET) 
- **Parameter:** `genre` (str) 
- **Description:** 
    - Finds the user with the most hours played in a specific genre. 
    - Shows the hours played per year for that genre. 

---

#### 4. **`/best_developer_year/`** (GET) 
- **Parameter:** `year` (int) 
- **Description:** 
    - Identifies the three developers with the most positive or neutral ratings in a given year. 

---

#### 5. **`/developer_reviews_analysis/`** (GET) 
- **Parameter:** `developer` (str) 
- **Description:** 
    - Returns the number of positive and negative ratings for a specific developer. 

---

#### 6. **`/recomendacion_usuario/`** (GET) 
- **Parameter:** `user_id` (str) 
- **Description:** 
    - Returns the top 5 personalized game recommendations for a user. 

---

Below are captures of the implementation of the endpoints:

<div style="display: flex; justify-content: center;">
    <div style="margin-right: 70px;">
        <img src="./src/app_consultas1.png" height=500>
    </div>
    <div>
        <img src="./src/app_consultas2.png" height=500>
    </div>
</div>

<span style="float:right;">[top](#table-of-contents)</span> 

<br>

## **7. Next Steps**

*   New functionalities, such as searching for games by genre. 
*   Improve the accuracy of the recommendation system using more advanced algorithms.
*   Optimize the performance of the API to support a greater number of requests.

<span style="float:right;">[top](#table-of-contents)</span> 

<br>

## **8. Contact**

Thank you for stopping by!
Did you find the project interesting? Then don't forget to give me a ⭐. This helps me with the visibility of my work.
Do you have an idea in mind or found a bug? Please open an issue or start a discussion.

**To contact me, write to the following email: zavalah222@gmail.com** 
**Or you can use my networks:**
[![X (formerly Twitter) URL](https://img.shields.io/twitter/url?url=https%3A%2F%2Ftwitter.com%2Fpseeker222&label=%40pseeker222)](https://twitter.com/pseeker222)
[![Follow us on LinkedIn](https://img.shields.io/badge/LinkedIn-pseeker-blue?style=flat&logo=linkedin&logoColor=b0c0c0&labelColor=363D44)](https://www.linkedin.com/in/hoover-zavala-63a64825b/)

<span style="float:right;">[top](#table-of-contents)</span> 