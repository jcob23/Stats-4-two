import webbrowser
from itertools import zip_longest

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def createHTML(name_s1, name_s2, uniqueChampions, sharedChampions, winningComps, number_of_games):
    data_frame_html = uniqueChampions.to_html(escape=False)
    data_frame_html2 = sharedChampions.to_html(escape=False)
    data_frame_html3 = winningComps.to_html(escape=False)

    html_content = f'''
           <html>
    <head>
    <style>
         body {{
                    background-image: url('poppy_bg.jpg');
                    background-size: cover;
                    background-repeat: no-repeat;
                    color: white;  
                }}
        .data-frame3 {{
            margin-right: 10px;
            direction: lrt;
            float: left;
        }}
        .data-frame1 {{
            margin-right: 10px;
            direction: lrt;
            float: left;
        }}
        .data-frame2 {{
            direction: lrt;
            float: left;
        }}
        .figure1 {{
            position: relative;
            background-size:contain;
            background-repeat:no-repeat;
            background-position:center; 
            clear: both
            direction: lrt;
            float: left;
            margin-left: 120px;
        }}
        .figure2 {{
            direction: lrt;
            float: left;
        }}
        .figure3 {{
            direction: lrt;
            float: left;

            
        }}
    </style>
</head>
<body>
    <div style="text-align: center; font-size: 25px;">
    LICZBA GIER: {number_of_games}
</div>
    <div class="data-frame3">
        {data_frame_html3}
    </div>
    <div class="data-frame1">
        {data_frame_html}
    </div>
    <div class="data-frame2">
        {data_frame_html2}
    </div>
    <div class="figure2">
         <img src="wykres_{name_s1.lower().replace(' ', '_')}.png" alt="Wykres"/>
    </div>
    <div class="figure3">
        <img src="wykres_{name_s2.lower().replace(' ', '_')}.png" alt="Wykres"/>
    </div>
    <div class="figure1">
        <img src="wykres.png" alt="Wykres"width="1200" height="920"/>/>
    </div>
    
</body>
</html>

               '''

    with open('output.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

    webbrowser.open('output.html')


def createTableUniqueChampions(name_s1, name_s2,
                               uniqueChampions_s1, uniqueChampions_s2):
    urls_s1 = []
    urls_s2 = []

    for championName_s1 in uniqueChampions_s1:
        urls_s1.append("champion_squares/" + championName_s1.lower() + ".png")
    for championName_s2 in uniqueChampions_s2:
        urls_s2.append("champion_squares/" + championName_s2.lower() + ".png")

    urls_s1 = sorted(urls_s1)
    urls_s2 = sorted(urls_s2)
    data = (list(zip_longest(urls_s1, urls_s2)))

    columns = [name_s1, name_s2]

    data_frame = pd.DataFrame(data, columns=columns)

    for col in data_frame.columns:
        data_frame[col] = data_frame[col].apply(image_tag)

    return data_frame


def createTableSharedChampions(sharedChampions):
    urls_s1 = []

    for championName in sharedChampions:
        urls_s1.append("champion_squares/" + championName.lower() + ".png")

    sorted(urls_s1)

    data_frame = pd.DataFrame(urls_s1, columns=["Shared Champions"])

    for col in data_frame.columns:
        data_frame[col] = data_frame[col].apply(image_tag)

    return data_frame


def createWinningComps(duoData):
    urls_s1 = []
    urls_s2 = []
    wins = []

    for stats in duoData:
        if stats.wins > 0:

            urls_s1.append("champion_squares/" + stats.name_s1.lower() + ".png")
            urls_s2.append("champion_squares/" + stats.name_s2.lower() + ".png")
            wins.append(stats.wins)

    data = list(zip(urls_s1, urls_s2, wins))

    columns = ["champ1", "champ2", "wins"]

    data_frame = pd.DataFrame(data, columns=columns)

    data_frame['champ1'] = data_frame['champ1'].apply(image_tag)

    data_frame['champ2'] = data_frame['champ2'].apply(image_tag)

    data_frame['wins'] = data_frame['wins'].apply(lambda x: f'<div style="text-align: center;">{x}</div>')

    return data_frame


def image_tag(url, alt_text=''):
    return f'<img src="{url}" alt="{alt_text}" style="max-width:80px;"/>'


def createGraphs(name_s1, name_s2,
                 classDistribution_s1, classDistribution_s2,
                 top_champs_s1, top_champs_s2, ):
    fig, axs = plt.subplots(1, 1, figsize=(20, 15))
    fig.patch.set_facecolor('none')

    print('name_s1: ', name_s1)
    print('name_s2: ', name_s2)
    pieChart(classDistribution_s1, name_s1)
    pieChart(classDistribution_s2, name_s2)

    barChart(name_s1, name_s2, top_champs_s1, top_champs_s2, axs)
    fig.savefig("wykres.png")


def barChart(name_s1, name_s2, stats_s1, stats_s2, ax):
    champions_s1 = []
    win_rates_s1 = []
    number_of_games_s1 = []

    champions_s2 = []
    win_rates_s2 = []
    number_of_games_s2 = []

    for stats in stats_s1:
        champions_s1.append(stats[0])
        win_rates_s1.append(stats[1])
        number_of_games_s1.append(stats[2])

    for stats in stats_s2:
        champions_s2.append(stats[0])
        win_rates_s2.append(stats[1])
        number_of_games_s2.append(stats[2])

    ax.bar(champions_s1, win_rates_s1, color='b', width=0.4)
    ax.bar(champions_s2, win_rates_s2, color='r', width=0.4)
    ax.set_xlabel("Champions", fontsize=25, color='white')
    ax.set_ylabel("WinRates[%]", fontsize=25, color='white')
    ax.legend(labels=[name_s1, name_s2], loc='upper right', bbox_to_anchor=(1, 1.1), fontsize=25)

    rects = ax.patches
    labels = number_of_games_s1 + number_of_games_s2

    for spine in ax.spines.values():
        spine.set_edgecolor('white')

    ax.grid(True, axis='y', color='white')
    ax.set_facecolor('none')
    ax.figure.patch.set_alpha(0.0)

    for rect, label in zip(rects, labels):
        height = rect.get_height()
        ax.text(
            rect.get_x() + rect.get_width() / 2, height, label, ha="center", va="bottom", fontsize=25, color='white'
        )

    ax.set_xticklabels(ax.get_xticklabels(), fontsize=20, color='white')
    ax.set_yticklabels(ax.get_yticklabels(), fontsize=20, color='white')


def pieChart(stats, name):
    data = []
    labels = []
    for role, value in stats.items():
        if value == 0:
            continue
        data.append(value)
        labels.append(role)

    colors = sns.color_palette('pastel', n_colors=len(data))

    fig, ax = plt.subplots()
    pie = ax.pie(data, labels=labels, colors=colors, autopct='%.0f%%', textprops={'fontsize': 14})

    ax.set_title(name, color="white", fontsize='15')

    for text in pie[1]:  # Indeks 1 zawiera tekstu etykiet
        text.set_color('white')

    fig.patch.set_facecolor('none')
    ax.set_facecolor('none')
    ax.figure.patch.set_alpha(0.0)
    fig.savefig(f"wykres_{name.lower().replace(' ', '_')}.png")
