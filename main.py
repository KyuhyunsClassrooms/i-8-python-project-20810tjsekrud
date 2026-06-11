# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 20810
# 프로젝트 주제: 게임 아이템 관리 및 추천 시스템

items = [
    ["나무검", "무기", 15, 100],
    ["철검", "무기", 25, 300],
    ["몽둥이", "무기", 3, 0],
    ["흡혈 낫", "무기", 30, 800],
    ["철퇴", "무기", 35, 800],
    ["단검", "무기", 25, 800],
    ["활", "무기", 0, 200],
    ["더 좋은 활", "무기", 5, 600],
    ["계엄령", "소비", 123, 2025],
    ["천갑옷", "방어구", 30, 300],
    ["철갑옷", "방어구", 50, 800],
    ["비키니", "방어구", 123, 30000],
    ["화살x100", "소비", 20, 400],
]


def get_user_input():
    print("아이템 종류: 무기, 방어구, 소비")
    item_type = input("찾고 싶은 아이템 종류를 입력하세요: ")
    min_power = int(input("최소 능력치를 입력하세요: "))
    return item_type, min_power


def search_items(item_type, min_power):
    results = []

    for item in items:
        if item[1] == item_type and item[2] >= min_power:
            results.append(item)

    return results


def print_result(results):
    if len(results) == 0:
        print("조건에 맞는 아이템이 없습니다.")
    else:
        print("\n검색 결과")
        print("-" * 30)

        best_item = results[0]

        for item in results:
            print(
                f"이름: {item[0]}, 종류: {item[1]}, 능력치: {item[2]}, 가격: {item[3]}"
            )

            if item[2] > best_item[2]:
                best_item = item

        print("-" * 30)
        print("추천 아이템:", best_item[0])
        print("최고 능력치:", best_item[2])


def main():
    item_type, min_power = get_user_input()
    results = search_items(item_type, min_power)
    print_result(results)


main()