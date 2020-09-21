import streamlit as st
import requests
import time
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0'}

sport = st.sidebar.radio('Sports', ('Football', 'Basketball', 'Tennis'))
operatores = ['Bet365', 'Betfrair', 'Marathon', 'Willhill', 'Bwin', 'Luckia', 'Codere', 'Sportium']

premier_league = 'http://www.elcomparador.com/futbol/inglaterra/premierleague'
liga = 'http://www.elcomparador.com/futbol/espa%C3%B1a/primeradivision'
serie_a = "http://www.elcomparador.com/futbol/italia/seriea"
bundesliga = 'http://www.elcomparador.com/futbol/alemania/bundesliga1'
liga_2 = 'http://www.elcomparador.com/futbol/espa%C3%B1a/segundadivision'
ligue_1 = 'http://www.elcomparador.com/futbol/francia/ligue1'
champions_league = 'http://www.elcomparador.com/futbol/europa/championsleague'
europa_league = 'http://www.elcomparador.com/futbol/europa/europaleague'
copa_libertadores = 'http://www.elcomparador.com/futbol/america/copalibertadores'
mls = 'http://www.elcomparador.com/futbol/usa/msl'
brasil_seriea = 'http://www.elcomparador.com/futbol/brasil/seriea'
argentina_liga = 'http://www.elcomparador.com/futbol/argentina/ligaprofesional'
mexico_liga_mx = 'http://www.elcomparador.com/futbol/mexico/ligamx'


competition_foot_url = [premier_league, liga, serie_a, bundesliga, liga_2, ligue_1, champions_league, europa_league,
                        copa_libertadores, mls, brasil_seriea, argentina_liga, mexico_liga_mx]

name_foot = ['Premier League', 'Liga', 'Serie A', 'Bundesliga', 'Liga 2', 'Ligue 1', 'Champions League', 'Europa League',
             'Copa Libertadores', 'MLS', 'Brasil Serie A', 'Argentina Liga', 'Mexico Liga']

nba = 'http://www.elcomparador.com/baloncesto/estadosunidos/nba'
liga_acb = 'http://www.elcomparador.com/baloncesto/espa%C3%B1a/acb'

competition_basket_url = [nba, liga_acb]

name_basket = ['NBA', 'Liga ACB']



if sport == 'Football' :
    st.markdown(
        "<h3 style='text-align: center; color: grey; size = 0'>Benchmark Football</h3>",
        unsafe_allow_html=True)

    tempo_url_foot = []
    tempo_name_foot = []

    tableau = pd.DataFrame(list(zip(name_foot, competition_foot_url)), columns=['Selection', 'Url'])
    options = st.multiselect('Quelle compétition ?', name_foot)


    for item in options:
        for j in range(len(tableau)):
            if item == tableau.iloc[j,0]:
                tempo_url_foot.append(tableau.iloc[j,1])
                tempo_name_foot.append(tableau.iloc[j,0])

    # Benchmark
    nb_rencontres = st.slider('Combien de rencontres à prendre en compte maximum ?', 0, 20, 2)
    #moyenne = st.checkbox('Faire la moyenne ?')
    lancement = st.button('Lancez le benchmark')

    if lancement :
        bench_final = pd.DataFrame(index=[i for i in operatores])
        for division in tempo_url_foot:
            page = requests.get(division, headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser')

            a = 0
            b = 0
            c = 0
            d = 0
            e = 0
            f = 0
            g = 0
            h = 0
            j = 0
            k = 0
            l = 0
            m = 0
            n = 0
            o = 0
            p = 0
            q = 0
            r = 0
            s = 0
            t = 0
            u = 0
            v = 0
            w = 0

            cote_bet365 = []
            cote_codere = []
            cote_willhill = []
            cote_bwin = []
            cote_luckia = []
            cote_sportium = []
            cote_marathon = []
            cote_betway = []
            cote_betsson = []
            cote_marcaapuestas = []
            cote_888 = []
            cote_betfair = []

            for i in range(24 * nb_rencontres):
                try :
                    item = soup.find_all('div', {'class': "impar"})[i].get_text()
                    if item.strip() == '-':
                        item = '0'
                    if (12 + i) % 12 == 0:
                        cote_bet365.append(item.strip())
                    elif (12 + i + a) % 13 == 0:
                        cote_codere.append(item.strip())
                        a += 1
                    elif (12 + i + b) % 14 == 0:
                        cote_willhill.append(item.strip())
                        b += 2
                    elif (12 + i + c) % 15 == 0:
                        cote_bwin.append(item.strip())
                        c += 3
                    elif (12 + i + d) % 16 == 0:
                        cote_luckia.append(item.strip())
                        d += 4
                    elif (12 + i + e) % 17 == 0:
                        cote_sportium.append(item.strip())
                        e += 5
                    elif (12 + i + f) % 18 == 0:
                        cote_marathon.append(item.strip())
                        f += 6
                    elif (12 + i + g) % 19 == 0:
                        cote_betway.append(item.strip())
                        g += 7
                    elif (12 + i + h) % 20 == 0:
                        cote_betsson.append(item.strip())
                        h += 8
                    elif (12 + i + j) % 21 == 0:
                        cote_marcaapuestas.append(item.strip())
                        j += 9
                    elif (12 + i + k) % 22 == 0:
                        cote_888.append(item.strip())
                        k += 10
                    elif (12 + i + l) % 23 == 0:
                        cote_betfair.append(item.strip())
                        l += 11
                except :
                    break

            for i in range(12 * nb_rencontres):
                try :
                    item = soup.find_all('div', {'class': "par"})[i].get_text()
                    if item.strip() == '-':
                        item = '0'
                    if (12 + i) % 12 == 0:
                        cote_bet365.append(item.strip())
                    elif (12 + i + m) % 13 == 0:
                        cote_codere.append(item.strip())
                        m += 1
                    elif (12 + i + n) % 14 == 0:
                        cote_willhill.append(item.strip())
                        n += 2
                    elif (12 + i + o) % 15 == 0:
                        cote_bwin.append(item.strip())
                        o += 3
                    elif (12 + i + p) % 16 == 0:
                        cote_luckia.append(item.strip())
                        p += 4
                    elif (12 + i + q) % 17 == 0:
                        cote_sportium.append(item.strip())
                        q += 5
                    elif (12 + i + r) % 18 == 0:
                        cote_marathon.append(item.strip())
                        r += 6
                    elif (12 + i + s) % 19 == 0:
                        cote_betway.append(item.strip())
                        s += 7
                    elif (12 + i + t) % 20 == 0:
                        cote_betsson.append(item.strip())
                        t += 8
                    elif (12 + i + u) % 21 == 0:
                        cote_marcaapuestas.append(item.strip())
                        u += 9
                    elif (12 + i + v) % 22 == 0:
                        cote_888.append(item.strip())
                        v += 10
                    elif (12 + i + w) % 23 == 0:
                        cote_betfair.append(item.strip())
                        w += 11
                    time.sleep(0.2)
                except :
                    break

            liste_trj = []

            liste_cotes = [cote_bet365, cote_betfair, cote_marathon, cote_willhill, cote_bwin, cote_luckia, cote_codere,
                           cote_sportium]

            for liste in liste_cotes:
                trj_totaux = []
                trj_moyenne = 0
                nb_matchs = int(len(liste) / 3)
                for a in range(nb_matchs):
                    if float(liste[2 * a]) != 0 and float(liste[2 * a + 1]) != 0 and float(liste[a + 2 * nb_matchs]) != 0:
                        trj_totaux.append(float("{:.2f}".format(float(1 / (
                                    (1 / (float(liste[2 * a]))) + (1 / (float(liste[2 * a + 1]))) + (
                                        1 / (float(liste[a + 2 * nb_matchs])))) * 100))))

                if len(trj_totaux) != 0:
                    trj_moyenne = "{:.2f}".format(round(sum(trj_totaux) / len(trj_totaux), 2))
                else:
                    trj_moyenne = 0

                liste_trj.append(trj_moyenne)
            bench_tempo = pd.DataFrame(data=liste_trj, index=[i for i in operatores])
            bench_final = bench_final.merge(bench_tempo, left_index=True, right_index=True)
        bench_final.columns = tempo_name_foot
        bench_final.loc["Moyenne Compétition"] = bench_final.mean()
        st.table(bench_final)



if sport == 'Basketball' :
    st.markdown(
        "<h3 style='text-align: center; color: grey; size = 0'>Benchmark Basketball</h3>",
        unsafe_allow_html=True)

    tempo_url_basket = []
    tempo_name_basket = []

    tableau = pd.DataFrame(list(zip(name_basket, competition_basket_url)), columns=['Selection', 'Url'])
    options = st.multiselect('Quelle compétition ?', name_basket)

    for item in options:
        for j in range(len(tableau)):
            if item == tableau.iloc[j,0]:
                tempo_url_basket.append(tableau.iloc[j,1])
                tempo_name_basket.append(tableau.iloc[j,0])

    # Benchmark
    nb_rencontres = st.slider('Combien de rencontres à prendre en compte maximum ?', 0, 20, 2)
    #moyenne = st.checkbox('Faire la moyenne ?')
    lancement = st.button('Lancez le benchmark')

    if lancement :
        bench_final = pd.DataFrame(index=[i for i in operatores])
        for division in tempo_url_basket:
            page = requests.get(division, headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser')

            a = 0
            b = 0
            c = 0
            d = 0
            e = 0
            f = 0
            g = 0
            h = 0
            j = 0
            k = 0
            l = 0

            cote_bet365 = []
            cote_codere = []
            cote_willhill = []
            cote_bwin = []
            cote_luckia = []
            cote_sportium = []
            cote_marathon = []
            cote_betway = []
            cote_betsson = []
            cote_marcaapuestas = []
            cote_888 = []
            cote_betfair = []

            for i in range(24 * nb_rencontres):
                item = soup.find_all('div', {'class': "impar"})[i].get_text()
                if item.strip() == '-':
                    item = '0'
                if (12 + i) % 12 == 0:
                    cote_bet365.append(item.strip())
                elif (12 + i + a) % 13 == 0:
                    cote_codere.append(item.strip())
                    a += 1
                elif (12 + i + b) % 14 == 0:
                    cote_willhill.append(item.strip())
                    b += 2
                elif (12 + i + c) % 15 == 0:
                    cote_bwin.append(item.strip())
                    c += 3
                elif (12 + i + d) % 16 == 0:
                    cote_luckia.append(item.strip())
                    d += 4
                elif (12 + i + e) % 17 == 0:
                    cote_sportium.append(item.strip())
                    e += 5
                elif (12 + i + f) % 18 == 0:
                    cote_marathon.append(item.strip())
                    f += 6
                elif (12 + i + g) % 19 == 0:
                    cote_betway.append(item.strip())
                    g += 7
                elif (12 + i + h) % 20 == 0:
                    cote_betsson.append(item.strip())
                    h += 8
                elif (12 + i + j) % 21 == 0:
                    cote_marcaapuestas.append(item.strip())
                    j += 9
                elif (12 + i + k) % 22 == 0:
                    cote_888.append(item.strip())
                    k += 10
                elif (12 + i + l) % 23 == 0:
                    cote_betfair.append(item.strip())
                    l += 11


            liste_trj = []

            liste_cotes = [cote_bet365, cote_betfair, cote_marathon, cote_willhill, cote_bwin, cote_luckia, cote_codere,
                           cote_sportium]

            for liste in liste_cotes:
                trj_totaux = []
                trj_moyenne = 0
                nb_matchs = int(len(liste) / 2)
                for a in range(nb_matchs):
                    if float(liste[2 * a]) != 0 and float(liste[2 * a + 1]) != 0 :
                        trj_totaux.append(float("{:.2f}".format(float(1 / (
                                    (1 / (float(liste[2 * a]))) + (1 / (float(liste[2 * a + 1])))) * 100))))

                if len(trj_totaux) != 0:
                    trj_moyenne = "{:.2f}".format(round(sum(trj_totaux) / len(trj_totaux), 2))
                else:
                    trj_moyenne = 0

                liste_trj.append(trj_moyenne)
            bench_tempo = pd.DataFrame(data=liste_trj, index=[i for i in operatores])
            bench_final = bench_final.merge(bench_tempo, left_index=True, right_index=True)
        bench_final.columns = tempo_name_basket
        nb_operateurs = len(bench_final)
        for compet in bench_final.columns:
            bench_final[compet].sum()
            #bench_final.loc['Moyenne compétition', compet] = float((bench_final[compet].sum())) / nb_operateurs
        st.table(bench_final)




if sport == 'Tennis':
    st.markdown(
        "<h3 style='text-align: center; color: grey; size = 0'>Benchmark Tennis</h3>",
        unsafe_allow_html=True)

    tempo_url_tennis = ['http://www.elcomparador.com/tenis']
    tempo_name_tennis = ['Competition en cours']
    competition_tennis_url = ['http://www.elcomparador.com/tenis']
    name_tennis = ['Competition en cours']


    start_match, end_match = st.select_slider('Choisissez la position des matchs à bencher',
    options = [i for i in range(51)],
    value = (0,50))

    # Benchmark
    #moyenne = st.checkbox('Faire la moyenne ?')
    lancement = st.button('Lancez le benchmark')

    if lancement :
        bench_final = pd.DataFrame(index=[i for i in operatores])
        for division in tempo_url_tennis:
            page = requests.get(division, headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser')

            a = start_match*2
            b = start_match*4
            c = start_match*6
            d = start_match*8
            e = start_match*10
            f = start_match*12
            g = start_match*14
            h = start_match*16
            j = start_match*18
            k = start_match*20
            l = start_match*22

            cote_bet365 = []
            cote_codere = []
            cote_willhill = []
            cote_bwin = []
            cote_luckia = []
            cote_sportium = []
            cote_marathon = []
            cote_betway = []
            cote_betsson = []
            cote_marcaapuestas = []
            cote_888 = []
            cote_betfair = []

            for i in range(24 * start_match, 24 * end_match, 1):
                item = soup.find_all('div', {'class': "impar"})[i].get_text()
                if item.strip() == '-':
                    item = '0'
                if (12 + i) % 12 == 0:
                    cote_bet365.append(item.strip())
                elif (12 + i + a) % 13 == 0:
                    cote_codere.append(item.strip())
                    a += 1
                elif (12 + i + b) % 14 == 0:
                    cote_willhill.append(item.strip())
                    b += 2
                elif (12 + i + c) % 15 == 0:
                    cote_bwin.append(item.strip())
                    c += 3
                elif (12 + i + d) % 16 == 0:
                    cote_luckia.append(item.strip())
                    d += 4
                elif (12 + i + e) % 17 == 0:
                    cote_sportium.append(item.strip())
                    e += 5
                elif (12 + i + f) % 18 == 0:
                    cote_marathon.append(item.strip())
                    f += 6
                elif (12 + i + g) % 19 == 0:
                    cote_betway.append(item.strip())
                    g += 7
                elif (12 + i + h) % 20 == 0:
                    cote_betsson.append(item.strip())
                    h += 8
                elif (12 + i + j) % 21 == 0:
                    cote_marcaapuestas.append(item.strip())
                    j += 9
                elif (12 + i + k) % 22 == 0:
                    cote_888.append(item.strip())
                    k += 10
                elif (12 + i + l) % 23 == 0:
                    cote_betfair.append(item.strip())
                    l += 11


            liste_trj = []

            liste_cotes = [cote_bet365, cote_betfair, cote_marathon, cote_willhill, cote_bwin, cote_luckia, cote_codere,
                           cote_sportium]

            for liste in liste_cotes:
                trj_totaux = []
                trj_moyenne = 0
                nb_matchs = int(len(liste) / 2)
                for a in range(nb_matchs):
                    if float(liste[2 * a]) != 0 and float(liste[2 * a + 1]) != 0 :
                        trj_totaux.append(float("{:.2f}".format(float(1 / (
                                    (1 / (float(liste[2 * a]))) + (1 / (float(liste[2 * a + 1])))) * 100))))

                if len(trj_totaux) != 0:
                    trj_moyenne = "{:.2f}".format(round(sum(trj_totaux) / len(trj_totaux), 2))
                else:
                    trj_moyenne = 0

                liste_trj.append(trj_moyenne)
            bench_tempo = pd.DataFrame(data=liste_trj, index=[i for i in operatores])
            bench_final = bench_final.merge(bench_tempo, left_index=True, right_index=True)
        bench_final.columns = tempo_name_tennis

        st.table(bench_final)



