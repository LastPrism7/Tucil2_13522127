import matplotlib.pyplot as plt
import numpy as np
from time import process_time

def input_menu():
    list_point = []
    for i in range (0,3):
        while (True):
            point_str = input("Masukkan titik (Format x,y): ")
            try:
                x, y = map(float, point_str.split(','))
                list_point.append([x, y])
                break
            except ValueError:
                print("Input tidak valid.")
    while True:
        print("Pilihan:")
        print("1. Divide and Conquer")
        print("2. Brute Force")
        choice = int(input("Masukkan Pilihan: "))
        print(choice)
        if choice != 1 and choice != 2:
            print("Input Tidak Valid.")
        else:
            break

    while True:
        iterasi = int(input("Jumlah Iterasi: "))
        if choice <1:
            print("Jumlah Iterasi Minimal 1.")
        else:
            break
    
    if choice == 1:
        dnc_start_time = process_time()

        res_list = [list_point[0]]
        res_list += (bezier_dnc(list_point[0],list_point[1],list_point[2],0.5, iterasi))
        res_list += [list_point[2]]
        res_list = np.array(res_list)
        
        dnc_end_time = process_time()
        time_elapsed = (dnc_end_time - dnc_start_time)*1000
        print("Waktu Algoritma DnC:",time_elapsed, "ms")

        plot_curve(list_point, res_list)


    elif choice == 2:
        bruteforce_start_time = process_time()

        res_list = []
        bezier_bruteforce(list_point,res_list,iterasi)
        res_list = np.array(res_list)

        bruteforce_end_time = process_time()
        time_elapsed = (bruteforce_end_time - bruteforce_start_time)*1000
        print("Waktu Algoritma BF:",time_elapsed, "ms")
        
        plot_curve(list_point, res_list)


def bezier_dnc(P0, P1, P2, t, iter_cnt):
    Left = [((1-t)*P0[0] + t*P1[0]), ((1-t)*P0[1] + t*P1[1])]
    Right = [((1-t)*P1[0] + t*P2[0]), ((1-t)*P1[1] + t*P2[1])]
    Middle = [((1-t)*Left[0] + t*Right[0]), ((1-t)*Left[1] + t*Right[1])]
    if iter_cnt == 1:
        return [Middle]
    else:
        left_bez = bezier_dnc(P0,Left,Middle,t,iter_cnt-1)
        right_bez = bezier_dnc(Middle,Right,P2,t,iter_cnt-1)
        return left_bez + [Middle] + right_bez

def bezier_bruteforce(points_list, result_list, iter_cnt: int):
    result_list.append(points_list[0])
    divv = 1/(2**iter_cnt)
    t = 0
    for i in range(1,2**(iter_cnt)):
        t+=divv
        x=((1-t)**2)*points_list[0][0] + 2*(1-t)*t*points_list[1][0] + (t**2)*points_list[2][0]
        y=((1-t)**2)*points_list[0][1] + 2*(1-t)*t*points_list[1][1] + (t**2)*points_list[2][1]
        result_list.append([x,y])
    result_list.append(points_list[2])

def plot_curve(control ,points):
    plt.figure(figsize=(7,7))
    plt.axhline(0, color='red', linewidth=0.75)  
    plt.axvline(0, color='red', linewidth=0.75)  
    plt.plot(points[:,0], points[:,1], label="Curve", color="blue")
    plt.scatter([control[0][0], control[1][0], control[2][0]], [control[0][1], control[1][1], control[2][1]], color="purple",label="Control Points")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.axis('on')
    plt.legend()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.xlim(min(control[0][0], control[1][0], control[2][0]) - 1, max(control[0][0], control[1][0], control[2][0]) + 1)
    plt.ylim(min(control[0][1], control[1][1], control[2][1]) - 1, max(control[0][1], control[1][1], control[2][1]) + 1)
    plt.show()

input_menu()