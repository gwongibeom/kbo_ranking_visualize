import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import datetime
import io

url = "https://sports.news.naver.com/kbaseball/record/index?category=kbo"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
table = soup.find(id="regularTeamRecordList_table")

if table is None:
    print("Table not found")
    exit()

rows = table.find_all("tr") # type: ignore
team_logos = []
team_names = []
games_behind_values = []
plt.rcParams['font.family'] = 'NanumGothic'

logo_urls = {
    "SSG": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/emblem/regular/fixed/emblem_SK.png",
    "키움": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/emblem/regular/fixed/emblem_WO.png",
    "LG": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/emblem/regular/fixed/emblem_LG.png",
    "KT": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/emblem/regular/fixed/emblem_KT.png",
    "KIA": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/emblem/regular/fixed/emblem_HT.png",
    "NC": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/emblem/regular/fixed/emblem_NC.png",
    "삼성": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/emblem/regular/fixed/emblem_SS.png",
    "롯데": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/emblem/regular/fixed/emblem_LT.png",
    "두산": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/emblem/regular/fixed/emblem_OB.png",
    "한화": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/emblem/regular/fixed/emblem_HH.png"
}

for row in rows:
    columns = row.find_all("td")
    if len(columns) > 0:
        rank = row.th.text.strip()
        team_name = columns[0].div.text.strip()
        logo_url = logo_urls.get(team_name)
        if logo_url:
            logo_response = requests.get(logo_url)
            logo_data = logo_response.content
            logo = OffsetImage(plt.imread(io.BytesIO(logo_data)), zoom=0.5)
            team_logos.append(logo)
            team_names.append(team_name)
            games_behind = float(columns[6].text.strip())
            games_behind_values.append(games_behind)

sorted_data = sorted(zip(team_logos, team_names, games_behind_values), key=lambda x: x[2], reverse=True)
team_logos, team_names, games_behind_values = zip(*sorted_data)

fig, ax = plt.subplots(figsize=(5, 8))
ax.bar(range(len(team_logos)), games_behind_values, zorder=2,)

ax.invert_xaxis()
ax.set_xticks(range(len(team_logos)))
ax.set_xticklabels(team_names, rotation='horizontal')
ax.invert_yaxis()

today = datetime.date.today()
ax.set_title(f'KBO {today} 게임차', fontsize=16, fontweight='bold')

colors = {
    "키움": "#570514",
    "두산": "#131230",
    "롯데": "#041E42",
    "삼성": "#074CA1",
    "한화": "#FF6600",
    "KIA": "#EA0029",
    "LG": "#C30452",
    "SSG": "#CE0E2D",
    "NC": "#315288",
    "KT": "#000000"
}

ax.tick_params(axis='x', labelsize=12)
ax.tick_params(axis='y', labelsize=12)

# Set the tick unit to 0.5
ax.set_yticks([i * 0.5 for i in range(int(max(games_behind_values) * 2) + 1)])

ax.yaxis.grid(True, alpha=0.3, zorder=1)


for i, (logo, value) in enumerate(zip(team_logos, games_behind_values)):
    ab = AnnotationBbox(logo, (i, value), frameon=False, pad=0.5)
    ax.add_artist(ab)
    ax.get_children()[i].set_color(colors.get(team_names[i], "blue"))

ax.text(0.5, 0.5, 'github.com/gwongibeom/kbo_ranking_visualize \n 디시인사이드 한화이글스 갤러리', transform=ax.transAxes,
        fontsize=15, color='gray', alpha=0.5,
        ha='center', va='center', rotation=34)

plt.tight_layout()
plt.savefig(f'KBO{today}.png')
plt.show()
