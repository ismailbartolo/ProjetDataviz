import streamlit as st
import os
    # importing numpy and pandas for to work with sample data.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt



st.set_page_config(page_title="Immo",layout="wide", initial_sidebar_state="expanded")

st.title('Projet Datavisualization')



@st.cache(suppress_st_warning=True)
def load_data():
    file = 'full_2020_2.csv'
    data = pd.read_csv(file)
    
    return data



# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 121000rows of data into the dataframe.

data=load_data()




# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache)")

########################################


def df_map_France_PrixInf_mean_Appartement():
    data.dropna(subset = ["longitude"], inplace =True)
    data.dropna(subset = ["latitude"], inplace =True)
    dfff = data.mask(data["type_local"]!= 'Appartement')
    dfff = dfff.where(data["valeur_fonciere"] < 750000)
    
    dfff.dropna(subset = ["longitude"], inplace =True) 
    dfff.dropna(subset = ["latitude"], inplace =True)
    return dfff

df_map_France_PrixInf_mean_Appartement = df_map_France_PrixInf_mean_Appartement()

def df_map_France_PrixSup_mean_Appartement():
    data.dropna(subset = ["longitude"], inplace =True)
    data.dropna(subset = ["latitude"], inplace =True)
    dfff = data.mask(data["type_local"]!= 'Appartement')
    dfff = dfff.where(data["valeur_fonciere"] > 1999999)#moyeene des prix
    
    dfff.dropna(subset = ["longitude"], inplace =True) 
    dfff.dropna(subset = ["latitude"], inplace =True)
    return dfff

df_map_France_PrixSup_mean_Appartement = df_map_France_PrixSup_mean_Appartement()


def df_map_France_PrixInf_mean_Maison():
    data.dropna(subset = ["longitude"], inplace =True)
    data.dropna(subset = ["latitude"], inplace =True)
    dfff = data.mask(data["type_local"]!= 'Maison')
    dfff = dfff.where(data["valeur_fonciere"] < 751173)
    
    dfff.dropna(subset = ["longitude"], inplace =True) 
    dfff.dropna(subset = ["latitude"], inplace =True)
    return dfff

df_map_France_PrixInf_mean_Maison = df_map_France_PrixInf_mean_Maison()

def df_map_France_PrixSup_mean_Maison():
    data.dropna(subset = ["longitude"], inplace =True)
    data.dropna(subset = ["latitude"], inplace =True)
    dfff = data.mask(data["type_local"]!= 'Maison')
    dfff = dfff.where(data["valeur_fonciere"] > 751173)
    
    dfff.dropna(subset = ["longitude"], inplace =True) 
    dfff.dropna(subset = ["latitude"], inplace =True)
    return dfff

df_map_France_PrixSup_mean_Maison = df_map_France_PrixSup_mean_Maison()

    
#####################################################




def get_prix_bati69():
    batiments = data[['code_departement','valeur_fonciere', 'surface_reelle_bati', 'nombre_pieces_principales','code_type_local', 'type_local']].drop_duplicates()
    batiments = batiments.mask(batiments["code_departement"]!=69)
    batiment_prix69= batiments['valeur_fonciere']
    batiments = batiments.sort_values(by=['code_type_local'])
    return batiment_prix69

########################################################

def get_info69():
    batiments = data[['code_departement','valeur_fonciere', 'surface_reelle_bati', 'nombre_pieces_principales','code_type_local', 'type_local']].drop_duplicates()
    batiments = batiments.mask(batiments["code_departement"]!=69)
    batiments = batiments.dropna()
    batiment_info = batiments.describe()
    return batiment_info

def get_info75():
    batiments = data[['code_departement','valeur_fonciere', 'surface_reelle_bati', 'nombre_pieces_principales','code_type_local', 'type_local']].drop_duplicates()
    batiments = batiments.mask(batiments["code_departement"]!=75)
    batiments = batiments.dropna()
    batiment_info = batiments.describe()
    return batiment_info

def get_info13():
    batiments = data[['code_departement','valeur_fonciere', 'surface_reelle_bati', 'nombre_pieces_principales','code_type_local', 'type_local']].drop_duplicates()
    batiments = batiments.mask(batiments["code_departement"]!=13)
    batiments = batiments.dropna()
    batiment_info = batiments.describe()
    return batiment_info
##################################################################


def get_nomCommune69():
    nom_commune69 = data[['nom_commune','code_departement','nature_mutation',]].drop_duplicates()
    nom_commune_69 = nom_commune69.mask(nom_commune69['code_departement']!=69)
    nom_commune_69_ = nom_commune_69.dropna()
    return nom_commune_69_

def get_nomCommune75():
    nom_commune75 = data[['nom_commune','code_departement','nature_mutation']].drop_duplicates()
    nom_commune_75 = nom_commune75.mask(nom_commune75['code_departement']!=75)
    nom_commune_75_ = nom_commune_75.dropna()
    return nom_commune_75_


def get_nomCommune13():
    nom_commune75 = data[['nom_commune','code_departement','nature_mutation']].drop_duplicates()
    nom_commune_75 = nom_commune75.mask(nom_commune75['code_departement']!=13)
    nom_commune_75_ = nom_commune_75.dropna()
    return nom_commune_75_
###################################################################


def get_mean69():
    batiments = data[['code_departement','valeur_fonciere', 'surface_reelle_bati', 'nombre_pieces_principales','code_type_local', 'type_local']].drop_duplicates()
    batiments = batiments.mask(batiments["code_departement"]!=69)
    batiments = batiments.dropna()
    batiment_mean= batiments['valeur_fonciere'].mean()
    batiments = batiments.sort_values(by=['code_type_local'])
    return  batiment_mean



def get_mean75():
    batiments = data[['code_departement','valeur_fonciere', 'surface_reelle_bati', 'nombre_pieces_principales','code_type_local', 'type_local']].drop_duplicates()
    batiments = batiments.mask(batiments["code_departement"]!=75)
    batiments = batiments.dropna()
    batiments = batiments.sort_values(by=['code_type_local'])
    batiment_mean= batiments['valeur_fonciere'].mean()
    return  batiment_mean


def get_mean13():
    batiments = data[['code_departement','valeur_fonciere', 'surface_reelle_bati', 'nombre_pieces_principales','code_type_local', 'type_local']].drop_duplicates()
    batiments = batiments.mask(batiments["code_departement"]!=13)
    batiments = batiments.dropna()
    batiments = batiments.sort_values(by=['code_type_local'])
    batiment_mean= batiments['valeur_fonciere'].mean()
    return  batiment_mean
###################################################################


def get_batiment69():
    batiments = data[['code_departement','valeur_fonciere', 'surface_reelle_bati', 'nombre_pieces_principales','code_type_local', 'type_local']].drop_duplicates()
    batiments = batiments.mask(batiments["code_departement"]!=69)
    batiments = batiments.sort_values(by=['code_type_local'])
    batiments = batiments.dropna()
    return  batiments



def get_batiment75():
    batiments = data[['code_departement','valeur_fonciere', 'surface_reelle_bati', 'nombre_pieces_principales','code_type_local', 'type_local']].drop_duplicates()
    batiments = batiments.mask(batiments["code_departement"]!=75)
    batiments = batiments.dropna()
    batiments = batiments.sort_values(by=['code_type_local'])
    return  batiments


def get_batiment13():
    batiments = data[['code_departement','valeur_fonciere', 'surface_reelle_bati', 'nombre_pieces_principales','code_type_local', 'type_local']].drop_duplicates()
    batiments = batiments.mask(batiments["code_departement"]!=13)
    batiments = batiments.dropna()
    batiments = batiments.sort_values(by=['code_type_local'])
    return  batiments

###############################################################
##############################################################

#ici j'utilise la fonction get_batiment() dans la fonction plotChart75. 

def plotChart75():
    pp = get_batiment75()
    pp
    chart = alt.Chart(pp).mark_bar().encode(
        x = 'valeur_fonciere' ,
        y = 'type_local'
    )
    chart = chart.properties(
        width=alt.Step(80)
    )
    a=st.write(chart)
    return a




#########################################################
###########################################



# Dataframe pour plot valeur fonciere en fonction de la surface des appart region 69

def df4():
    df = data[['code_departement','valeur_fonciere', 'surface_reelle_bati', 'nombre_pieces_principales','code_type_local', 'type_local']].drop_duplicates()
    df1 = df.mask(df["code_departement"]!=69)
    df1 = df1.mask(df1["surface_reelle_bati"]>107)
    df1 = df1.mask(df1["valeur_fonciere"]>275706) # 3ème quartile
    df1 = df1.mask(df1["type_local"]!='Appartement')
    df1 = df1.dropna()
    df1 = df1.sort_values(by=['surface_reelle_bati'])
    return df1

###################################################################################################

# fonction qui sert à recuperer une sous dataframe extraite trier par code_commune region 75,69,13
def df75():
    df = data[['code_departement','code_commune','valeur_fonciere', 'surface_reelle_bati', 'nombre_pieces_principales','code_type_local', 'type_local']].drop_duplicates()
    df1 = df.mask(df["code_departement"]!=75)
    df1 = df1.mask(df1["surface_reelle_bati"]>107)
    df1 = df1.mask(df1["valeur_fonciere"]>275706)
    df1 = df1.mask(df1["type_local"]!='Appartement')
    df1 = df1.dropna()
    df1 = df1.sort_values(by=['code_commune'])
    return df1

def df69():
    df = data[['code_departement','code_commune','valeur_fonciere', 'surface_reelle_bati', 'nombre_pieces_principales','code_type_local', 'type_local']].drop_duplicates()
    df1 = df.mask(df["code_departement"]!=69)
    df1 = df1.mask(df1["surface_reelle_bati"]>107)
    df1 = df1.mask(df1["valeur_fonciere"]>275706)
    df1 = df1.mask(df1["type_local"]!='Appartement')
    df1 = df1.dropna()
    df1 = df1.sort_values(by=['code_commune'])
    return df1

def df13():
    df = data[['code_departement','code_commune','valeur_fonciere', 'surface_reelle_bati', 'nombre_pieces_principales','code_type_local', 'type_local']].drop_duplicates()
    df1 = df.mask(df["code_departement"]!=13)
    df1 = df1.mask(df1["surface_reelle_bati"]>107)
    df1 = df1.mask(df1["valeur_fonciere"]>275706)
    df1 = df1.mask(df1["type_local"]!='Appartement')
    df1 = df1.dropna()
    df1 = df1.sort_values(by=['code_commune'])
    return df1

########################################################################################################

#Fonction qui sert à recuperer les données trier par type_local region 75 pour plot
def df_plot_Cir75():
    df = data[['code_departement','code_commune','valeur_fonciere', 'surface_reelle_bati', 'nombre_pieces_principales','code_type_local', 'type_local']]
    df1 = df.mask(df["code_departement"]!=75)
    df1 = df1.mask(df1["surface_reelle_bati"]>107)
    df1 = df1.mask(df1["valeur_fonciere"]>275706)
    df1 = df1.dropna()
    df1 = df1.sort_values(by=['type_local'])
    return df1

def df_plot_Camembert75():
    df = data[['nombre_pieces_principales','code_departement','surface_reelle_bati','valeur_fonciere']]
    df1 = df.mask(df["code_departement"]!=75)
    df1 = df1.mask(df1["surface_reelle_bati"]>107)
    df1 = df1.mask(df1["valeur_fonciere"]>275706)
    df1 = df1.mask(df1["nombre_pieces_principales"]<1)
    df1 = df1['nombre_pieces_principales']
    
    df1 = df1.dropna()
    return df1

def df_plot_Camembert69():
    df = data[['nombre_pieces_principales','code_departement','surface_reelle_bati','valeur_fonciere']]
    df1 = df.mask(df["code_departement"]!=69)
    df1 = df1.mask(df1["surface_reelle_bati"]>107)
    df1 = df1.mask(df1["valeur_fonciere"]>275706)
    df1 = df1.mask(df1["nombre_pieces_principales"]<1)
    df1 = df1['nombre_pieces_principales']
    
    df1 = df1.dropna()
    return df1

def df_plot_Camembert13():
    df = data[['nombre_pieces_principales','code_departement','surface_reelle_bati','valeur_fonciere']]
    df1 = df.mask(df["code_departement"]!=13)
    df1 = df1.mask(df1["surface_reelle_bati"]>107)
    df1 = df1.mask(df1["valeur_fonciere"]>275706)
    df1 = df1.mask(df1["nombre_pieces_principales"]<1)
    df1 = df1['nombre_pieces_principales']
    
    df1 = df1.dropna()
    return df1



###########################################################

@st.cache(suppress_st_warning=True)
def map_info():
#df_coord = data[['longitude','latitude']]
    batiment69 = get_batiment69()
    batiment75 = get_batiment75()
    batiment13 = get_batiment13()
    
    batiment_info69 = get_info69()
    batiment_info75 = get_info75()
    batiment_info13 = get_info13()
    

    Valeur_moyenne69 = get_mean69()
    Valeur_moyenne75 = get_mean75()
    Valeur_moyenne13 = get_mean13()
    
    g = get_nomCommune75()
    oo = get_nomCommune69()
    d = get_nomCommune13()
    
    data.dropna(subset = ["longitude"], inplace =True)
    data.dropna(subset = ["latitude"], inplace =True)


    df_map69 = data.mask(data["code_departement"]!=69)
    df_map69.dropna(subset = ["longitude"], inplace =True)
    df_map69.dropna(subset = ["latitude"], inplace =True)


    df_map75 = data.mask(data["code_departement"]!=75)
    df_map75.dropna(subset = ["longitude"], inplace =True)
    df_map75.dropna(subset = ["latitude"], inplace =True)

    df_map13 = data.mask(data["code_departement"]!=13)
    df_map13.dropna(subset = ["longitude"], inplace =True)
    df_map13.dropna(subset = ["latitude"], inplace =True)

    if st.checkbox("Show/Hide all houses "):
        st.map(data)

    

    st.write("--------------------------------------------------------------------------------------")

    multiselect = st.multiselect('Choisir de voir sur la carte le type de logement', ['Appartement','Maison'])
    if "Appartement" in multiselect:
        if st.checkbox('Appuyer pour consulter la carte des appartements.'):
            a1 = st.slider('Slider prix Appartement', 0, 1502346)
            if a1 < 751173:
                st.map(df_map_France_PrixInf_mean_Appartement)
            if a1 > 751173:
                st.map(df_map_France_PrixSup_mean_Appartement)
                st.write("On remarque bien que les appartements qui sont au dessus de la moyenne au niveau de la valeur fonciere sont centrées en Ile-de-France.")

            
    if "Maison" in multiselect:
        if st.checkbox('Appuyer pour consulter la carte des maisons.'):
            a2 = st.slider('Slider prix Maison', 0, 1502346)
            if a2 < 751173:
                st.map(df_map_France_PrixInf_mean_Maison)
            if a2 > 751173:
                st.map(df_map_France_PrixSup_mean_Maison)



                


    st.sidebar.subheader("Bienvenue sur votre Dashbord")


    option = st.sidebar.selectbox('Choisir un département',('69', '75','13'))

    if option == '69':
        st.header("Département Rhône-Alpes")
        if st.checkbox('Appuyer pour consulter la carte des biens dans le 69'):
            st.map(df_map69)
        if st.checkbox("Appuyer pour consulter l'ensemble des biens"):
            st.write(batiment69)
        if st.checkbox("Appuyer pour consulter la moyenne de la valeure foncière en Rhône-Alpes"):
            st.title(Valeur_moyenne69)
            st.write(batiment_info69)
            

        if st.checkbox('Afficher la répartition des natures de mutation'):
            ax = sns.countplot(y="nature_mutation", hue="code_departement", data=oo)
            st.pyplot()
            st.write("D' après ce graphique nous pouvons en deduire que les majeures transactions sont des ventes immobilières ")
        
    if option == '75':
        st.header("Département Ile-de-France")
        if st.checkbox('Appuyer pour consulter sur la carte les biens dans le 75'):
            st.map(df_map75)
        if st.checkbox("Appuyer pour consulter l'ensemble des biens"):
            st.write(batiment75)
            
        if st.checkbox("Appuyer pour consulter la moyenne de la valeure foncière en Iles-de-France"):
            st.title(Valeur_moyenne75)
            st.write(batiment_info75)

        if st.checkbox('Afficher la répartition des natures de mutation'):
            ax = sns.countplot(y="nature_mutation", hue="code_departement", data=g)
            st.pyplot()
            st.write("D' après ce graphique nous pouvons en deduire que les majeures transactions sont des ventes immobilières ")
            


            
    
    if option == '13':
        st.header("Département Boûche-du-Rhône")
        if st.checkbox('Appuyer pour consulter sur la carte des biens dans le 13'):
            st.map(df_map13)
        if st.checkbox("Appuyer pour consulter l'ensemble des biens"):
            st.write(batiment13)
        if st.checkbox("Appuyer pour consulter la moyenne de la valeure foncière au Bouche-du-Rhônes"):
            st.title(Valeur_moyenne13)
            st.write(batiment_info13)

        if st.checkbox('Afficher la répartition des natures de mutation'):
            ax = sns.countplot(y="nature_mutation", hue="code_departement", data=oo)
            st.pyplot()
            st.write("D' après ce graphique nous pouvons en deduire que les majeures transactions sont des ventes immobilières ")
            
        


oo_load_state = st.text('Loading data...')
oo=map_info()
oo_load_state.text("Done! (using st.cache)")

@st.cache(suppress_st_warning=True)
def fonction2():

    # on elève les doublons de la liste des villes 
#nom_commune= data.drop_duplicates(subset ="nom_commune", keep = 'first', inplace=True)
    data__=data['nom_commune'].tolist()
    data__.sort()
    data__series = pd.Series(data__)

#st.write(data__)
    # on cree une liste de villes
    city_list1 = data.groupby("nom_commune").agg('sum').index.tolist() #data.groupby("nom_commune").agg('sum').index.tolist()
    city_list1.sort()
    city_list = ["Toutes les villes"]+city_list1

#convert the list to serie in order to use .mask
    city_series=pd.Series(city_list)
    df_ville  = city_series.mask(city_series == "Toutes les villes")
    df_ville.dropna(inplace =True)

    df_ville_choose  = city_series.mask(city_series != "Abancourt")
    df_ville_choose.dropna(inplace =True)

    ville = "Dans toutes les villes"
    all_city = st.sidebar.selectbox('Consulter toutes les villes:', city_list1)
    

batiments = data[['code_departement','valeur_fonciere', 'surface_reelle_bati', 'nombre_pieces_principales','code_type_local', 'type_local']].drop_duplicates()
batiments = batiments.mask(batiments["code_departement"]!=69)
batiments = batiments.dropna()



oo = get_nomCommune69()
g = get_nomCommune75()
d = get_nomCommune13()

df4 = df4()

df1 = df75()
df69 = df69()
df13 = df13()


dFF = df_plot_Cir75()

dfCam = df_plot_Camembert75()
dfCam69 = df_plot_Camembert69()
dfCam13 = df_plot_Camembert13()




st.write("--------------------------------------------------------------------------------------")
st.write("--------------------------------------------------------------------------------------")
st.write("--------------------------------------------------------------------------------------")

#######################################################################################
@st.cache(suppress_st_warning=True)
def graphes():
    
    
    option = st.sidebar.selectbox('Choisir une département pour afficher des autres visualisations',('69', '75','13'))
    
    if option == '69':
        st.header("Région Rhône-Alpes: autre graphe intéressant")
        if st.checkbox("Afficher le graphe montrant la valeure des appartements en fonction de la surface réelle des batiments de type appartement"):
            
            d = sns.lineplot( data = df69 ,x='code_commune',y= 'valeur_fonciere')
            st.pyplot()
            
            t = df69.plot.scatter(x='code_commune', y= 'valeur_fonciere',c='DarkBlue', marker = 'o')
            st.pyplot()

            a = df4.plot.scatter( x='surface_reelle_bati',y= 'valeur_fonciere',c='DarkBlue', marker = 'o')
            st.pyplot()
        
        if st.checkbox("Voir la répartition du nombres de pièce principales "):
            
            effectif69 = dfCam69.value_counts()
            j69 = plt.pie(effectif69,labels=effectif69.index)
            st.pyplot()
            st.write("On remarque très bien ici que plus de la moitié des appartements au Boûche-du-Rhône ....")

    if option == '75':
        st.header("Ile-de-France: autre graphe intéressant")
        
        if st.checkbox("Afficher les graphes qui montre la correlation entre (valeur foncière/commmune) et (valeur foncière/surface réelle) "):
            
            b = sns.lineplot( data = df1 ,x='code_commune',y= 'valeur_fonciere')
            st.pyplot()
            st.write("Ici on passe l'ensemble des données en mode long-form, les valeurs répétées (de chaque commune) seront agrégées pour montrer la moyenne et l'intervalle de confiance à 95%:. En effet, la valeur foncière des communes d'Iles-de-France est bien inégalitaire car d'après ce graphique on remarque des disparités qui pourraient refleter également des inégalités sociales(à vérifier) car entre les communes 75112 à 75120 les valeurs extremes sont centrées autour de la moyenne. Contrairement entre 75000 et 75107 où les valeurs fluctuent fortement et ne sont pas centrées autour de la moyenne. Si on prends l'exemple du VIIe arrondissement de Paris. Au 75107 on remarque bien une inégalité des biens ce qui nous surprends pas avec notamment le quartier Gros Caillou 6")
            
            d = df1.plot.scatter(x='code_commune', y= 'valeur_fonciere',c='DarkBlue', marker = 'o')
            st.pyplot()
            
            c = df1.plot.scatter(x='surface_reelle_bati',y= 'valeur_fonciere',c='DarkBlue', marker = 'o')
            st.pyplot()

            
        
        if st.checkbox("Voir la répartition du nombres de pièce principales "):
            
            effectif = dfCam.value_counts()
            j = plt.pie(effectif,labels=effectif.index)
            st.pyplot()
            st.write("On remarque très bien ici que plus de la moitié des appartements en Iles-de-France n'ont qu'une pièce principale T1")
    
    
    if option == '13':
        st.header("Rhône-Alpes: autre graphe intéressant")

        if st.checkbox("Afficher le graphe montrant la valeure des appartements en fonction de la surface réelle des batiments de type appartement"):

            i = sns.lineplot(data = df13,x='code_commune', y= 'valeur_fonciere')
            st.pyplot()
            st.write("explication")

            y = df13.plot.scatter(x='code_commune', y= 'valeur_fonciere',c='DarkBlue', marker = 'o')
            st.pyplot()

            v = df13.plot.scatter(x='surface_reelle_bati',y= 'valeur_fonciere',c='DarkBlue', marker = 'o')
            st.pyplot()
        
        if st.checkbox("Voir la répartition du nombres de pièce principales "):
            effectif13 = dfCam13.value_counts()
            j13 = plt.pie(effectif13,labels=effectif13.index)
            st.pyplot()
            st.write("On remarque très bien ici que plus de la moitié des appartements en Rhône-Alpes ....")

        
    



        


#################################################################################################    


graphes = graphes()

effectif = dfCam.value_counts()
effectif69 = dfCam69.value_counts()
effectif13 = dfCam13.value_counts()

j = plt.pie(effectif,labels=effectif.index)
j69 = plt.pie(effectif69,labels=effectif69.index)
j13 = plt.pie(effectif13,labels=effectif13.index)
#o = sns.distplot(batiments['valeur_fonciere'], hist_kws={'alpha': 0.9})
#st.set_option('deprecation.showPyplotGlobalUse', False)
#st.pyplot()


#a = sns.factorplot('HeatingQC', 'SalePrice', hue = 'CentralAir', estimator = np.mean, data = train, size = 4.5, aspect = 1.4)




st.sidebar.write("&nbsp[![Connect](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ismail-bartolo-8427b41b2?challengeId=AQGFZtVsm6gT-AAAAXyQXDmy4lWMHHBgZbPnECfcPwf0vexOlzzFKxEKGsWuqLwHgC06ZUQDrre7fLSDNzJLbklQk5yjLupKaA&submissionId=8f2a3b2d-c3f1-ae16-f57f-d909ff87fa4e)")

