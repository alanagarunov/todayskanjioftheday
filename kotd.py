from bs4 import BeautifulSoup
import requests
import random
import math
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

allkanji = "日一人年大十二本中出三見月生五上四金九入学円子八六下気小七山女百先名川千水国長男時行分後前間東今高校土外木来車話北午書半白西電天語聞食何南火右万左休毎母読友父雨立手力目田正文会同自社地方新場口町明京空通言理体作用強足公野思家多心教早元近考画海売知道計事朝字発台広音者業員開少問代工動止主題切意度持花赤青世安楽院店界親重集物使品死始運終答夜住帰真古有歌買急送図週室歩転不風紙研黒春以究起着病待族色銀走秋夏医仕去別味写特夕注料建悪館屋試験英習曜駅肉洋旅鳥質冬犬服昼茶私弟飲牛魚兄勉映借妹堂姉飯貸漢村合市内回米当首石数記点活原交組引直対部相定実決全表調化期番取都和平算受区竹県進森線指声予向勝面委形反林頭所次門王係感投打島両式議民連談流谷玉選局放関光球科戦最細丸役身約太由法的要治成消神戸協機加配続育改乗初想農州産助府園共得追馬商葉告軍落参利信負側求顔昨守官美命変福各政横深果船申必様港争無位置草階羽路経現他費付橋説岸客性岩夫制務登速角央総号害副領席設池残支星念根象報苦労例然具解資際査伝働景好判寺賞辺遠低在件団絵任鉄失差課末返増極種短情油示量望植宿薬観察確型倍勢減容党演達能良再弱格候史過波満敗税管常兵状営職積可構録省比防幸練周軽材断晴等境規術飛殺導曲備単庭完輸血述競権温武給済庫歴限辞額坂愛耳未退準認息造技航復冷虫移雪類個児論印輪板非列熱革清覚遊億芸君財識毛便停陸疑程帯努固接散章静効供喜囲卒割旧酒順難黄補悲秒優師収易雲老令糸券宅暗徒破編警貨鳴責訪採季陽域欠因皮底富担歯貿講河柱願希祭適婦寄筆余禁逆童若笑脳久束妻仲暴栄札蔵段険均圧許畑呼緑包礼留罪針専折昔値精則焼測豊厚泳略処承荷照絶否版存損才座仏績築除降混並危居雑招永炭刊像将漁賛貯犯布貝装諸亡劇湖湯箱訓浴複塩似背麦迷夢兆燃歳署祝延預乱衣与氷寒群庁臣城拾浅違層裏勤困快著誌勇刻械菜欧宇被刷渡欲痛枚郵含探孫骨届巻況慣鼻閉毒突暮液簡貧臓律祖湾粉純捜超吸療捕翌介片敬迎販泉幅彼般舞忘込皿宝換胸砂占鉱誤灯頼洗途枝抜尊伸窓爆胃普婚齢幼浮押倒了患絡募捨払綿銅昇腹遅乳紅冊香更抱恐耕卵戻巨震干頂越触依籍汚互逃傾緒跡駐紹晩雇替拝棒贈薄奥詰掛双刺到寝盗悩御蒸荒硬埋袋吹封娘賢腕床詞柔殿濃肩机零怒泊杯甘掃掘灰疲皆軟沈凍煙恋郊腰踊眠怖珍喫溶涙匹鋭塗軒叫乾祈髪忙汗湿瓶咲召缶隻脂肌靴鈍恥泥隅偶辛磨姓筒粒偉畳膚濯猫塔沸菓幾帽枯涼舟符憎肯燥畜坊挟曇滴伺第氏宮結案整挙統保基昭松価提票応検器士証級健護態条幹独隊率派衛張里義策評標製裁司康授紀博救展視修織故矢弁功株素養街姿閣益衆節興推郡詩討憲激系批盟志典従拡就丁異厳遺倉模唱属宣盛皇臨企旗源豆創障筋災沢暑善援帳梅施銭井謝鮮仮密賀我幕染傷秘監環徳審訴刀弓牧縮影泣撃佐核序融射舎揮渉響賃貴藤敵請径攻納崎樹督催酸至宗及宙離桜操句摘脈郎誕孝訳鏡看奏振郷献維己浜塁邦墓汽忠遣抗沿雄誠緊巣俳廃江僚飼聖吉羊踏壊債恩儀往継闘葬避逮迫潮惑崩聴芽脱肥鋼笛締俵執縦房撤削措載陣為抑眼択秀徴弾償拠拒刑塚致繰尾描仁鈴盤項喪伴懸腸契掲躍棄邸還穴潔慮暖朗枠恵露沖伊肺緩需購充貢却端熟獲併徹衝焦奪陛浦析譲称挑誘紛促慎控握俊渋銃糖携診託撮侵括駆透津壁稲裂敏是排裕堅芝綱覧扱顧訟戒祉誉歓奮勧奈騒閥甲縄揺免既薦隣華範隠哲杉釈妥威豪滞微隆症暫肝喚妙索后襲懇班柄驚麻舌剤瀬趣陥斎貫仙慰旬兼旨即柳偽較覇詳抵脅鹿茂犠距雅飾網竜繁翼潟魅嫌斉敷擁寸圏罰滅礎腐脚智磁尽僕滑孤炎賠寿頑鎖彩摩励輝蓄軸巡稼瞬垂砲噴誇祥牲秩帝唆阻泰賄撲堀弘菊絞穀縁唯膨耐塾漏慶猛芳懲剣彰棋恒揚冒倫陳憶潜熊克岳概拘黙偏雰遇彦諮狭卓阿糧簿炉殊殖艦輩奇慢謀拍李丈浩寛覆胞隔浄没暇貞鑑陰銘随烈尋稿丹啓丘棟壌漫玄粘悟舗妊騰遂狂岐緯培衰艇屈淡抽披廷准奨浸剰胆繊虚霊悔諭絹惨虐翻墜沼据徐搭盾滝軌妨擦尺鯨荘諾雷漂懐勘栽拐駄添冠斜宏浪亜詐壇勲魔酬紫紋卸欄逸涯拓獄尚彫穏顕巧矛垣欺釣粧之粛愚遭架鬼庶梨稚滋幻煮姫須誓把践呈疎仰剛疾征砕謡亀嫁謙嘆菌頻琴棚酷鶴宰廊寂昌伏碁俗漠邪晶墨鎮靖洞履劣殴娠奉憂朴亭也怪酔惜穫佳潤旭悼乏該赴桑髄盆穂壮堤飢傍疫累痴搬癒錦郭磯尿凶吐宴賓虜駒陶鐘憾昆粗訂傘騎寧循忍怠如寮鉛珠凝苗獣哀跳匠蛇澄縫僧眺唐呉凡憩聡溝恭刈睡錯伯曙陵霧魂弊妃舶餓窮掌麗臭悦刃縛暦宜盲粋辱轄萩猿弦窒炊栗洪摂飽嘉冗桃狩朱渦紳枢碑鍛鼓裸猶塊旋幣膜扇槽慈鎌伐蚕漬糾墳坪紺慌娯辰霞羅峡俸厘峰醸弔乙汁尼遍衡那薫猟款閲淳偵喝敢胎酵憤豚鳩遮扉硫赦窃泡又慨紡恨肪桂扶戯虎忌晋濁奔斗迅肖鉢朽殻享晃桐藩媒鶏禅嘱鷹胴迭挿猪紘弥陪剖譜庄悠淑敦帆暁傑奴祐錠鵬遷拙侍峠篤渇叔雌堪叙酢亘吟逓甚媛崇笹漆岬癖愉礁屯姻綾擬塀唇閑幽毅曹詠稔卑侮鋳抹尉隷禍酪茎帥逝匿襟蛍寡痢庸坑楊駿賊搾亮畔孔吾椿拷嬢渓翁圭廉蓮謹窯褒醜升殉煩劾堕租桟婿慕瑞罷矯某囚伍泌蘭漸蚊秦茅厄藻沙輔嫡嵐椎嚇凸郁韻霜硝楠勅玲棺儒拳翔肇愁楼亨薪褐嶺喬賜繕栓寅乃凹洲樺槙巌睦錬胡峻衷逐斥槻蝶詔琢蕉宵"

hirarom_map = {'あ':'a', 'い':'i', 'う':'u', 'え':'e', 'お':'o', 'か':'ka', 'き':'ki', 'く':'ku', 'け':'ke', 'こ':'ko', 'さ':'sa', 'し':'shi', 'す':'su', 'せ':'se', 'そ':'so', 'た':'ta', 'ち':'chi', 'つ':'tsu', 'て':'te', 'と':'to', 'な':'na', 'に':'ni', 'ぬ':'nu', 'ね':'ne', 'の':'no', 'は':'ha', 'ひ':'hi', 'ふ':'fu', 'へ':'he', 'ほ':'ho', 'ま':'ma', 'み':'mi', 'む':'mu', 'め':'me', 'も':'mo', 'や':'ya', 'ゆ':'yu', 'よ':'yo', 'ら':'ra', 'り':'ri', 'る':'ru', 'れ':'re', 'ろ':'ro', 'わ':'wa', 'ゐ':'wi', 'ゑ':'we', 'を':'o', 'ん':'n'}
dakuhirarom_map = {'が':'ga', 'ぎ':'gi', 'ぐ':'gu', 'げ':'ge', 'ご':'go', 'ざ':'za', 'じ':'ji', 'ず':'zu', 'ぜ':'ze', 'ぞ':'zo', 'だ':'da', 'ぢ':'ji', 'づ':'zu', 'で':'de', 'ど':'do', 'ば':'ba', 'び':'bi', 'ぶ':'bu', 'べ':'be', 'ぼ':'bo'}
smallhira = {'ゃ':'ya', 'ょ':'yo', 'ゅ':'yu'}

katarom_map = {'ア':'a', 'イ':'i', 'ウ':'u', 'エ':'e', 'オ':'o', 'カ':'ka', 'キ':'ki', 'ク':'ku', 'ケ':'ke', 'コ':'ko', 'サ':'sa', 'シ':'shi', 'ス':'su', 'セ':'se', 'ソ':'so', 'タ':'ta', 'チ':'chi', 'ツ':'tsu', 'テ':'te', 'ト':'to', 'ナ':'na', 'ニ':'ni', 'ヌ':'nu', 'ネ':'ne', 'ノ':'no', 'ハ':'ha', 'ヒ':'hi', 'フ':'fu', 'ヘ':'he', 'ホ':'ho', 'マ':'ma', 'ミ':'mi', 'ム':'mu', 'メ':'me', 'モ':'mo', 'ヤ':'ya', 'ユ':'yu', 'ヨ':'yo', 'ラ':'ra', 'リ':'ri', 'ル':'ru', 'レ':'re', 'ロ':'ro', 'ワ':'wa', 'ヰ':'wi', 'ヱ':'we', 'ヲ':'o', 'ン':'n'}
dakukatarom_map = {'ガ':'ga', 'ギ':'gi', 'グ':'gu', 'ゲ':'ge', 'ゴ':'go', 'ザ':'za', 'ジ':'ji', 'ズ':'zu', 'ゼ':'ze', 'ゾ':'zo', 'ダ':'da', 'ヂ':'ji', 'ヅ':'zu', 'デ':'de', 'ド':'do', 'バ':'ba', 'ビ':'bi', 'ブ':'bu', 'ベ':'be', 'ボ':'bo'}
smallkata = {'ャ':'ya', 'ョ':'yo', 'ュ':'yu'}

todayskanji = allkanji[random.randint(0, len(allkanji))]


cities = ["New York"]
weather_str = "```"
for x in cities:
    soup = BeautifulSoup((requests.get(f"https://www.google.com/search?q="+"weather "+x, headers=headers)).text, 'html.parser')
    temp = soup.find('span', attrs={'class': 'wob_t q8U8x'}).text
    temp = math.trunc((int(temp) - 32) * 0.5556)
    condition = soup.find('span', id='wob_dc').text
    #weather_str += x + " : " + str(temp) + "C " + condition + "\n"  
    weather_str += f"{x:16} : {temp:3} C {condition:} \n"
    
weather_str += "```"
print("Chatot Weather" + "\n" + weather_str)


res = requests.get(f'https://jisho.org/search/' + todayskanji + '%20%23kanji', headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
    
#soup = BeautifulSoup(res.text, 'html.parser')
def reading_examples(soup):
    try:
        threeway = lambda x: (
            x[: x.index("【")],
            x[x.index("【") + 1 : x.index("】")],
            x[x.index("】") + 1 :],
        )
        process = lambda x: [
            {
                "kanji": k.replace("\n", "").strip(),
                "reading": r.replace("\n", "").strip(),
                "meanings": m.replace("\n", "").strip().split(", "),
            }
            for k, r, m in x
        ]

        res = soup.find_all("ul", {"class": "no-bullet"})
        on = res[0].find_all("li")
        ons = process([threeway(o.text) for o in on])

        try:
            kun = res[1].find_all("li")
            kuns = process([threeway(k.text) for k in kun])
        except:
            kuns = None

        return {
            "on": ons,
            "kun": kuns,
        }
    except:
        return None


def main_meanings(soup):
    return (
        soup.find_all("div", {"class": "kanji-details__main-meanings"})[0]
        .text.strip()
        .split(", ")
    )


def main_readings(soup):
    res = soup.find_all("div", {"class": "kanji-details__main-readings"})
    try:
        kun = (
            res[0]
            .find_all("dl", {"class": "dictionary_entry kun_yomi"})[0]
            .text.replace("\n", "")
            .replace("Kun:", "")
            .split("、 ")
        )
    except:
        kun = None

    try:
        on = (
            res[0]
            .find_all("dl", {"class": "dictionary_entry on_yomi"})[0]
            .text.replace("\n", "")
            .replace("On:", "")
            .split("、 ")
        )
    except:
        on = None
    return {"kun": kun, "on": on}
    
def get_on_romanji(on):
    on_result = ""
    for x in on:
        if x in katarom_map:
            on_result += katarom_map[x]
        if x in dakukatarom_map:
            on_result += dakukatarom_map[x]
        if x in smallkata:
            if on[on.index(x)-1] == "シ":
                on_result = on_result[:len(on_result)-3]
                if on[on.index(x)] == "ョ": 
                    on_result += "sho"
                if on[on.index(x)] == "ュ": 
                    on_result += "shu"
                if on[on.index(x)] == "ャ": 
                    on_result += "sha"
            elif on[on.index(x)-1] == "チ":
                on_result = on_result[:len(on_result)-3]
                if on[on.index(x)] == "ョ": 
                    on_result += "cho"
                if on[on.index(x)] == "ュ": 
                    on_result += "chu"
                if on[on.index(x)] == "ャ": 
                    on_result += "cha"
            else:
                on_result = on_result[:len(on_result)-1]
                on_result += smallkata[x]
        if x == ',':
            on_result += ',　'
            
    return on_result
    
def get_kun_romanji(kun):
    kun_result = ""
    #kun_result += smallkata[x]
    for x in kun:
        if x in hirarom_map:
            kun_result += hirarom_map[x]
        if x in dakuhirarom_map:
            kun_result += dakuhirarom_map[x]
        if x in smallkata:
            if kun[kun.index(x)-1] == "し":
                kun_result = kun_result[:len(kun_result)-3]
                if kun[kun.index(x)] == "ょ": 
                    kun_result += 'sho'
                if kun[kun.index(x)] == "ゅ":
                    kun_result += 'shu'
                if kun[kun.index(x)] == "ゃ":
                    kun_result += 'sha'
            elif kun[kun.index(x)-1] == "ち":
                kun_result = kun_result[:len(kun_result)-3]
                if kun[kun.index(x)] == "ょ": 
                    kun_result += 'cho'
                if kun[kun.index(x)] == "ゅ":
                    kun_result += 'chu'
                if kun[kun.index(x)] == "ゃ":
                    kun_result += 'cha'
            else:
                kun_result = kun_result[:len(kun_result)-1]
                kun_result += smallhira[x]
        if x == ',':
            kun_result += ',　'
        if x == '.':
            kun_result += '.'
            
    return kun_result

on = "Kunyomi only kanji (if you see this something has gone terribly wrong)"
kun = "Onyomi only kanji"
final_on_examples1 = ""
final_on_examples2 = ""
final_kun_examples1 = ""
final_kun_examples2 = ""

#onkanji1, onreading1, onromaji1, onmeaning1, onkanji2, onreading2, onromaji2, onmeaning2, kunkanji1, kunreading1, kunromaji1, kunmeaning1, kunkanji2, kunreading2, kunromaji2, kunmeaning2 = [""]*16

def get_on_examples(on_examples):
    onkanji1, onreading1, onromaji1, onmeaning1, onkanji2, onreading2, onromaji2, onmeaning2 = [""]*8
    try:
        onkanji1 = on_examples[0].get("kanji")
        onreading1 = on_examples[0].get("reading")
        onromaji1 = get_on_romanji(on_examples[0].get("reading"))
        onmeaning1 = ",　".join(on_examples[0].get("meanings"))
        
        onkanji2 = on_examples[1].get("kanji")
        onreading2 = on_examples[1].get("reading")
        onromaji2 = get_on_romanji(on_examples[1].get("reading"))
        onmeaning2 = ",　".join(on_examples[1].get("meanings"))
    except:
        pass
    return f"{onkanji1:6} {onreading1:14} {onromaji1:14} {onmeaning1:}\n{onkanji2:6} {onreading2:14} {onromaji2:14} {onmeaning2:}"

def get_kun_examples(kun_examples):
    kunkanji1, kunreading1, kunromaji1, kunmeaning1, kunkanji2, kunreading2, kunromaji2, kunmeaning2 = [""]*8
    try:
        kunkanji1 = kun_examples[0].get("kanji")
        kunreading1 = kun_examples[0].get("reading")
        kunromaji1 = get_kun_romanji(kun_examples[0].get("reading"))
        kunmeanings1 = ",　".join(kun_examples[0].get("meanings"))
        
        kunkanji2 = kun_examples[1].get("kanji")
        kunreading2 = kun_examples[1].get("reading")
        kunromaji2 = get_kun_romanji(kun_examples[1].get("reading"))
        kunmeanings2 = ",　".join(kun_examples[1].get("meanings"))
    except:
        pass
    
    return f"{kunkanji1:6} {kunreading1:14} {kunromaji1:14} {kunmeaning1:}\n{kunkanji2:6} {kunreading2:14} {kunromaji2:14} {kunmeaning2:}"

try:
    on = ",　".join(main_readings(soup).get("on"))
    on = on + "　" + get_on_romanji(on)
    kun = ",　".join(main_readings(soup).get("kun"))
    kun = kun + "　" + get_kun_romanji(kun)
    
except:
    pass

on_examples = reading_examples(soup).get("on")
kun_examples = reading_examples(soup).get("kun")

kusa = ", ".join(main_meanings(soup))
print(f"Todays kanji of the day is \n```{todayskanji:1} {kusa:}")
print(f"onyomi: {on:7} \nkunyomi: {kun:}")
print(get_on_examples(on_examples))
print(get_kun_examples(kun_examples)+"```")
