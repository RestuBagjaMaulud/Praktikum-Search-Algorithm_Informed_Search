# -*- coding: utf-8 -*-
"""a_star_graph.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cBAX1joTVftf2DQxU3hc9eKZ10MqpvXS
"""

from queue import PriorityQueue

# Fungsi untuk algoritma A* Graph Search
def a_star_graph_search(graph, start, goal, heuristic):
    frontier = PriorityQueue()  # Antrian prioritas berdasarkan f(n) = g(n) + h(n)
    frontier.put((0, start, []))  # (biaya, simpul, jalur)
    explored = {}  # Dictionary untuk menyimpan biaya terendah ke setiap simpul

    while not frontier.empty():
        current_cost, current_node, path = frontier.get()  # Ambil simpul dengan prioritas terendah
        path = path + [current_node]  # Tambahkan simpul ke jalur

        if current_node == goal:
            print("\nSimpul tujuan ditemukan!")
            print("Jalur yang ditemukan:", " → ".join(path))
            print("Total biaya jalur:", current_cost)
            return  # Berhenti jika simpul tujuan ditemukan

        explored[current_node] = current_cost  # Tandai simpul sebagai dieksplorasi

        for neighbor, cost in graph[current_node].items():
            new_cost = current_cost + cost  # g(n)
            total_cost = new_cost + heuristic[neighbor]  # f(n) = g(n) + h(n)

            # Jika simpul belum dieksplorasi atau ditemukan jalur dengan biaya lebih rendah
            if neighbor not in explored or new_cost < explored[neighbor]:
                explored[neighbor] = new_cost
                frontier.put((total_cost, neighbor, path))  # Masukkan simpul ke frontier

    print("\nSimpul tujuan tidak ditemukan!")

# Daftar heuristik untuk setiap simpul
heuristic = {
    'S': 6,
    'A': 4,
    'B': 3,
    'C': 3,
    'D': 1,
    'G': 0
}

# Graf (dalam bentuk daftar kejadian)
graph = {
    'S': {'A': 3, 'B': 2},
    'A': {'D': 5, 'B': 1},
    'B': {'C': 2},
    'C': {'D': 3, 'G': 4},
    'D': {'G': 1}
}

# Titik awal dan tujuan
start_node = 'S'
goal_node = 'G'

# Panggil fungsi A* Graph Search
a_star_graph_search(graph, start_node, goal_node, heuristic)