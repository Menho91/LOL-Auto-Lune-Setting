from urllib import request
from bs4 import BeautifulSoup
import time
import pyautogui as mouse

champion_list = []
champion_eng_list = []

# 챔피언 리스트에서 챔피언의 이름들을 불러옵니다.
with open("champion.txt", "r", encoding="UTF-8") as file:
    for line in file:
        champion_list.append(line.replace("\n", ""))
with open("champion_eng.txt", "r") as file2:
    for line in file2:
        if line.replace("\n", "").isalpha() == False:
            output = ""
            for i in range(0, len(line)):
                if line[i].isalpha() == True:
                    output += line[i]
            champion_eng_list.append(output)
        else:
            champion_eng_list.append(line.replace("\n", ""))

# 선택한 챔피언의 이름을 입력받습니다.
while 1:
    champion = input("챔피언 이름을 입력하세요> ")
    if champion not in champion_list:
        print("챔피언 이름을 정확하게 입력해주세요.")
    else:
        break
print("{}을(를) 골랐습니다.".format(champion))

# 챔피언의 룬 정보를 불러옵니다.
trans_dic = {}
for i in range(0, len(champion_list)):
    trans_dic[champion_list[i]] = champion_eng_list[i]

def translator(name):
    return trans_dic[name]

target = request.urlopen("https://poro.gg/champions/{}/aram".format(translator(champion)))

soup = BeautifulSoup(target, "html.parser")
output1 = soup.select("div.champion-rune-builds .active", limit=11)

current_lune = []
for img in output1:
    output = img.attrs
    current_lune.append(output["alt"])

# 불러온 룬 정보를 마우스 포인터 입력값으로 변환합니다.
point_list = []

def lune_to_point(arg):
    point_list.clear()
    if arg[0] == "정밀":
        point_list.append((466,333))
    elif arg[0] == "지배":
        point_list.append((511,333))
    elif arg[0] == "결의":
        point_list.append((564,333))
    elif arg[0] == "마법":
        point_list.append((614,333))
    elif arg[0] == "영감":
        point_list.append((666,333))
    else:
        pass
    if arg[1] == "집중 공격" or arg[1] == "감전":
        point_list.append((469,484))
    elif arg[1] == "치명적 속도" or arg[1] == "포식자":
        point_list.append((535,484))
    elif arg[1] == "기민한 발놀림" or arg[1] == "어둠의 수확":
        point_list.append((594,484))
    elif arg[1] == "정복자" or arg[1] == "칼날비":
        point_list.append((657,484))
    elif arg[1] == "콩콩이 소환" or arg[1] == "착취의 손아귀" or arg[1] == "빙결 강화":
        point_list.append((480,484))
    elif arg[1] == "신비로운 유성" or arg[1] == "여진" or arg[1] == "봉인 풀린 주문서":
        point_list.append((566,484))
    elif arg[1] == "난입" or arg[1] == "수호자" or arg[1] == "프로토타입: 만능의 돌":
        point_list.append((646,484))
    else:
        pass
    if arg[2] == "과다치유" or arg[2] == "비열한 한 방" or arg[2] == "무효화 구체" or arg[2] == "철거" or arg[2] == "마법공학 점멸기":
        point_list.append((484,609))
    elif arg[2] == "승전보" or arg[2] == "피의 맛" or arg[2] == "마나순환 팔찌" or arg[2] == "생명의 샘" or arg[2] == "마법의 신발":
        point_list.append((563,609))
    elif arg[2] == "침착" or arg[2] == "돌발 일격" or arg[2] == "빛의 망토" or arg[2] == "보호막 강타" or arg[2] == "완벽한 타이밍":
        point_list.append((646,609))
    else:
        pass
    if arg[3] == "전설: 민첩함" or arg[3] == "좀비 와드" or arg[3] == "깨달음" or arg[3] == "사전 준비" or arg[3] == "외상":
        point_list.append((484,716))
    elif arg[3] == "전설: 강인함" or arg[3] == "유령 포로" or arg[3] == "기민함" or arg[3] == "재생의 바람" or arg[3] == "미니언 해체분석기":
        point_list.append((563,716))
    elif arg[3] == "전설: 핏빛 길" or arg[3] == "사냥의 증표" or arg[3] == "절대 집중" or arg[3] == "뼈 방패" or arg[3] == "비스킷 배달":
        point_list.append((646,716))
    else:
        pass
    if arg[4] == "최후의 일격" or arg[4] == "주문 작열" or arg[4] == "과잉 성장" or arg[4] == "우주적 통찰력":
        point_list.append((484,824))
    elif arg[4] == "체력차 극복" or arg[4] == "물 위를 걷는 자" or arg[4] == "소생" or arg[4] == "쾌속 접근":
        point_list.append((563,824))
    elif arg[4] == "최후의 저항" or arg[4] == "폭풍의 결집" or arg[4] == "불굴의 의지" or arg[4] == "시간 왜곡 물약":
        point_list.append((646,824))
    elif arg[4] == "굶주린 사냥꾼":
        point_list.append((477,824))
    elif arg[4] == "영리한 사냥꾼":
        point_list.append((531,824))
    elif arg[4] == "끈질긴 사냥꾼":
        point_list.append((589,824))
    elif arg[4] == "궁극의 사냥꾼":
        point_list.append((659,824))
    else:
        pass
    if arg[5] == "정밀":
        point_list.append((876, 338))
    elif arg[5] == "지배":
        if arg[0] == "정밀":
            point_list.append((876, 338))
        else:
            point_list.append((940, 338))
    elif arg[5] == "결의":
        if arg[0] == "정밀" or arg[0] == "지배":
            point_list.append((940, 338))
        else:
            point_list.append((1000, 338))
    elif arg[5] == "마법":
        if arg[0] == "정밀" or arg[0] == "지배" or arg[0] == "결의":
            point_list.append((1000, 338))
        else:
            point_list.append((1064, 338))
    elif arg[5] == "영감":
        point_list.append((1064, 338))
    else:
        pass
    if arg[6] == "과다치유" or arg[6] == "비열한 한 방" or arg[6] == "무효화 구체" or arg[6] == "철거" or arg[6] == "마법공학 점멸기":
        point_list.append((891, 445))
    elif arg[6] == "승전보" or arg[6] == "피의 맛" or arg[6] == "마나순환 팔찌" or arg[6] == "생명의 샘" or arg[6] == "마법의 신발":
        point_list.append((973, 445))
    elif arg[6] == "침착" or arg[6] == "돌발 일격" or arg[6] == "빛의 망토" or arg[6] == "보호막 강타" or arg[6] == "완벽한 타이밍":
        point_list.append((1055, 445))
    elif arg[6] == "전설: 민첩함" or arg[6] == "좀비 와드" or arg[6] == "깨달음" or arg[6] == "사전 준비" or arg[6] == "외상":
        point_list.append((891, 542))
    elif arg[6] == "전설: 강인함" or arg[6] == "유령 포로" or arg[6] == "기민함" or arg[6] == "재생의 바람" or arg[6] == "미니언 해체분석기":
        point_list.append((973, 542))
    elif arg[6] == "전설: 핏빛 길" or arg[6] == "사냥의 증표" or arg[6] == "절대 집중" or arg[6] == "뼈 방패" or arg[6] == "비스킷 배달":
        point_list.append((1055, 542))
    else:
        pass
    if arg[7] == "전설: 민첩함" or arg[7] == "좀비 와드" or arg[7] == "깨달음" or arg[7] == "사전 준비" or arg[7] == "외상":
        point_list.append((891, 542))
    elif arg[7] == "전설: 강인함" or arg[7] == "유령 포로" or arg[7] == "기민함" or arg[7] == "재생의 바람" or arg[7] == "미니언 해체분석기":
        point_list.append((973, 542))
    elif arg[7] == "전설: 핏빛 길" or arg[7] == "사냥의 증표" or arg[7] == "절대 집중" or arg[7] == "뼈 방패" or arg[7] == "비스킷 배달":
        point_list.append((1055, 542))
    elif arg[7] == "최후의 일격" or arg[7] == "주문 작열" or arg[7] == "과잉 성장" or arg[7] == "우주적 통찰력":
        point_list.append((891, 642))
    elif arg[7] == "체력차 극복" or arg[7] == "물 위를 걷는 자" or arg[7] == "소생" or arg[7] == "쾌속 접근":
        point_list.append((973, 642))
    elif arg[7] == "최후의 저항" or arg[7] == "폭풍의 결집" or arg[7] == "불굴의 의지" or arg[7] == "시간 왜곡 물약":
        point_list.append((1055, 642))
    elif arg[7] == "굶주린 사냥꾼":
        point_list.append((879, 642))
    elif arg[7] == "영리한 사냥꾼":
        point_list.append((937, 642))
    elif arg[7] == "끈질긴 사냥꾼":
        point_list.append((1001, 642))
    elif arg[7] == "궁극의 사냥꾼":
        point_list.append((1064, 642))
    else:
        pass
    if arg[8] == "Adaptive":
        point_list.append((888, 716))
    elif arg[8] == "AttackSpeed":
        point_list.append((971, 716))
    elif arg[8] == "CDRScaling":
        point_list.append((1053, 716))
    else:
        pass
    if arg[9] == "Adaptive":
        point_list.append((888, 771))
    elif arg[9] == "Armor":
        point_list.append((971, 771))
    elif arg[9] == "MagicRes":
        point_list.append((1053, 771))
    else:
        pass
    if arg[10] == "HealthScaling":
        point_list.append((888, 823))
    elif arg[10] == "Armor":
        point_list.append((971, 823))
    elif arg[10] == "MagicRes":
        point_list.append((1053, 823))
    else:
        pass

# 마우스를 움직여 룬 정보대로 클릭합니다.
def click_point(arg):
    mouse.click(703, 923)
    for i in range(0, len(arg)):
        time.sleep(0.5)
        mouse.click(arg[i])
    time.sleep(0.5)
    mouse.click(795, 228)
    time.sleep(0.5)
    mouse.click(1620, 164)

# 실행합니다.
lune_to_point(current_lune)
click_point(point_list)