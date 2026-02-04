
import random
import time

def generate_participants(count=200):
    participants = []
    for i in range(1, count + 1):
        participants.append({"name": f"員工{i:03d}", "id": f"EID-{i:03d}"})
    return participants

def define_prizes():
    prizes = [
        {"name": "🎉特獎🎉", "item": "豪華電動汽車一台，讓你從此不用擠捷運！", "quantity": 1},
        {"name": "✈️頭獎✈️", "item": "雙人國外豪華旅遊套票，想去哪就去哪！老闆買單！", "quantity": 2},
        {"name": "📱二獎📱", "item": "最新款高階智慧型手機，滑社群更順暢！", "quantity": 5},
        {"name": "💰三獎💰", "item": "百貨公司禮券 5000 元，血拚不用看價格！", "quantity": 10},
        {"name": "🎁普獎🎁", "item": "精美時尚家電一台，讓你的生活更有品味！", "quantity": 30},
    ]
    return prizes

def run_grand_lottery():
    print("\n\033[1;33m" + "📢📢📢 各位嘉賓，各位夥伴，大家晚安！今晚星光熠熠，氣氛High到爆炸！" + "\033[0m")
    time.sleep(1.5)
    print("\033[1;36m" + "我是您今晚最嗨的主持人 CuteClaw！🥳" + "\033[0m")
    time.sleep(2)
    print("\033[1;35m" + "今晚，我們齊聚一堂，共同慶祝豐收的一年，也要把所有不可能變成可能！" + "\033[0m")
    time.sleep(2.5)
    print("\033[1;31m" + "沒錯！就是我們的——尾牙感恩抽獎晚會！🎉🎉🎉")
    time.sleep(2.5)
    print("\033[1;32m" + "準備好了嗎？深呼吸！尖叫聲！把屋頂掀開來好不好！" + "\033[0m")
    time.sleep(2)

    print("\n" + "\033[1;47;30m" + "--- 💖 掌聲鼓勵！尖叫聲！準備好迎接幸運之神的眷顧了嗎？！ 💖 ---" + "\033[0m" + "\n")
    time.sleep(2.5)

    all_participants = generate_participants()
    drawing_pool = list(all_participants) # 建立可供抽獎的池
    prizes = define_prizes()
    all_winners = {} # 儲存所有獎項的中獎者

    # 按照獎項價值從高到低抽獎
    for prize in prizes:
        prize_name = prize["name"]
        prize_item = prize["item"]
        quantity = prize["quantity"]

        print(f"\n\n\033[1;44;37m" + f"✨✨✨ 接下來要抽出的是我們今晚的【{prize_name}】！" + "\033[0m")
        time.sleep(2)
        print(f"\033[1;33m" + f"獎品是：{prize_item}！總共要抽出 {quantity} 位超級幸運兒！" + "\033[0m")
        time.sleep(2.5)

        if len(drawing_pool) < quantity:
            print(f"\033[1;31m" + f"😭 哎呀！我們的抽獎池人數不足以抽出 {quantity} 位【{prize_name}】得主了！只好期待下次囉！" + "\033[0m")
            break

        print("\n" + "\033[1;36m" + "主持人：誰會是這位萬眾矚目的幸運兒呢？讓我們屏息以待！..." + "\033[0m")
        time.sleep(3)
        print("\033[1;35m" + "🥁🥁🥁 燈光！音效！心跳加速！準備揭曉——！！！" + "\033[0m")
        time.sleep(2.5)

        winners_for_this_prize = random.sample(drawing_pool, quantity)
        all_winners[prize_name] = winners_for_this_prize

        print(f"\n\033[1;42;30m" + f"恭喜以下 {len(winners_for_this_prize)} 位【{prize_name}】幸運得主！掌聲加尖叫聲！🌟" + "\033[0m")
        for winner in winners_for_this_prize:
            print(f"\033[1;37;41m" + f"     🎉🎉🎉 {winner['name']} (工號: {winner['id']})！🎉🎉🎉" + "\033[0m")
            drawing_pool.remove(winner) # 從抽獎池中移除中獎者
            time.sleep(1.5) # 宣佈每個得主後稍作停頓，製造節奏感
        time.sleep(2)
        print("\033[1;32m" + "再次恭喜所有得主！請繼續期待下一個更刺激的獎項！" + "\033[0m")
        time.sleep(2.5)

    print("\n\n\033[1;33m" + "🎊🎊🎊 各位，今晚的尾牙抽獎活動圓滿結束！🎊🎊🎊" + "\033[0m")
    time.sleep(2)
    print("\033[1;36m" + "感謝所有參與的夥伴們！無論有沒有中獎，都感謝您們一年來的辛勞與付出！" + "\033[0m")
    time.sleep(2.5)
    print("\033[1;35m" + "祝大家新年快樂，身體健康，財源廣進，明年尾牙再見！謝謝大家！💖💖💖" + "\033[0m")

    # 顯示總結
    print("\n\n" + "\033[1;47;30m" + "--- 尾牙抽獎結果總覽 (請中獎者核對工號領獎！) ---" + "\033[0m")
    for prize_name, winners in all_winners.items():
        original_prize = next((p for p in prizes if p['name'] == prize_name), None)
        prize_item_summary = original_prize['item'] if original_prize else "未知獎品"
        print(f"\n\033[1;34m" + f"【{prize_name}】 ({prize_item_summary})" + "\033[0m")
        if winners:
            for winner in winners:
                print(f"  - {winner['name']} (工號: {winner['id']})")
        else:
            print("  - 無中獎者")
    print("\033[1;47;30m" + "------------------------------------------------------" + "\033[0m" + "\n")


if __name__ == "__main__":
    run_grand_lottery()
