import random
import time
from math import exp
N_QUEENS = 1000
temperature = 5000
step = 50000
#------- Số cặp hậu đe doạ nhau trên 1 đường chéo---------
def threat_calculation(n):
    if n < 2: 
        return 0
    if n == 2:
        return 1
    return (n-1) * n/ 2

#------- Khởi tạo bàn cờ ban đầu -----------
def create_board(n):
    board = list(range(n))
    random.shuffle(board)
    return board

#-------- Tính cost = số đôi hậu đang đe doạ nhau trên đường chéo chính/phụ của bàn cờ---------
def cost(board):
    threat = 0
    m_chessboard = {}
    a_chessboard = {}

    for col, row in enumerate(board):
        temp_m = col - row
        temp_a = col + row

        m_chessboard[temp_m] = m_chessboard.get(temp_m, 0) + 1
        a_chessboard[temp_a] = a_chessboard.get(temp_a, 0) + 1

    for count in m_chessboard.values():
        threat += threat_calculation(count)
    for count in a_chessboard.values():
        threat += threat_calculation(count)

    return threat

#--------- Thuật toán ---------
def simulated_annealing():
    solution_found = False
    answer = create_board(N_QUEENS)

    cost_answer = cost(answer)

    t = temperature
    alpha = 0.995
    loop=0
    k=1.8
    T0 = temperature
    max_steps = step

    for i in range(1, max_steps + 1):
        loop+=1
        t = max(1e-8, T0 * (alpha ** (i ** k)))

        successor = None #tuong duong bien x* de luu trang thai tot nhat tung khao sat
        
        best_cost = float('inf')
        for _ in range(5):
            temp_board = answer.copy()
            i, j = random.sample(range(N_QUEENS), 2)
            temp_board[i], temp_board[j] = temp_board[j], temp_board[i]
            temp_cost = cost(temp_board)
            if temp_cost < best_cost:
                best_cost = temp_cost
                successor = temp_board
    
        delta = best_cost - cost_answer 

        if delta < 0 or random.uniform(0, 1) < exp(-delta / t):
            answer = successor
            cost_answer = cost(answer)
    
        if cost_answer == 0:
            solution_found = True
            print_chess_board(answer)
            print(loop)
            break  

    if solution_found is False:
        print("Failed")
def print_chess_board(board):
    for col, row in enumerate(board):
        print(f"{col} ; {row}")
def main():
    start = time.time()
    simulated_annealing()
    print("Runtime in second:", time.time() - start)
if __name__ == "__main__":
    main()