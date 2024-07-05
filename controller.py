#!/usr/bin/env python3
import sys

from simulation import SimulationRobobo
from car import train_q_table, initialize_q_table, print_q_table, load_q_table, play_q_table

if __name__ == "__main__":
    # You can do better argument parsing than this!

    rob = SimulationRobobo()
     
    # Load or initialize the Q-table
    q_table = initialize_q_table()

    # Print the initial Q-table
    print("Initial Q-table:")
    print_q_table(q_table)

    # Train the Q-table
    #train_q_table(rob, q_table, num_episodes=50)
    
    # Print the trained Q-table
    trained_q_table = load_q_table(file_path='q_table.pkl')
    
    print("Trained Q-table:")
    print_q_table(trained_q_table, num_entries = 81)

    #play_q_table(rob, trained_q_table)