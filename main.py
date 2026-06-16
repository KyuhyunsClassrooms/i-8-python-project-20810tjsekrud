# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 20810
# 프로젝트 주제: 게임 아이템 관리 및 추천 시스템
import random

symbols = [
    [1, "🍒"],
    [2, "🍋"],
    [3, "🔔"],
    [4, "⭐"],
    [5, "💎"]
]

def show_money(money):
    print("\n현재 소지금:", money, "원")

def spin_slot():
    result = []

    for i in range(3):
        idx = random.randint(0, len(symbols) - 1)
        result.append(symbols[idx][1])

    return result

def calculate_reward(bet, result):
    if result[0] == result[1] == result[2]:
        return bet * 10

    elif result[0] == result[1] or result[0] == result[2] or result[1] == result[2]:
        return bet

    else:
        return 0

def print_result(result, reward):
    print("\n결과")
    print(result[0], result[1], result[2])

    if reward == 0:
        print("꽝!")

    elif result[0] == result[1] == result[2]:
        print("대박! 3개 일치!")
        print(reward, "원 획득!")

    else:
        print("2개 일치!")
        print(reward, "원 획득!")

def main():
    money = 100000

    print("=== 슬롯머신 게임 ===")

    while money > 0:

        show_money(money)

        try:
            bet = int(input("베팅 금액 입력 (0 입력 시 종료): "))
        except ValueError:
            print("정수만 입력하세요.")
            continue

        if bet == 0:
            print("게임을 종료합니다.")
            break

        if bet > money:
            print("소지금보다 많이 베팅할 수 없습니다.")
            continue

        if bet < 0:
            print("올바른 금액을 입력하세요.")
            continue

        money -= bet

        result = spin_slot()

        reward = calculate_reward(bet, result)

        money += reward

        print_result(result, reward)

    if money <= 0:
        print("\n소지금이 모두 소진되었습니다.")
        print("게임 종료!")

main()