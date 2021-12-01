import PySimpleGUI as sg

from View import View
from Database import budgetDatabase

goalDataBase = budgetDatabase("C:\code\BudgetApp\database\myDB.json")
myView = View(goalDataBase)

def print_basic_info_about_goal(saved, goal_db_entry):
    print(f'Amount Saved: {saved}, Total Cost: {goal_db_entry["cost"]}')
    print(f'Associated Account: {goal_db_entry["associated account"]}')
    print()

while True:
    event, values = myView.window.read()
    if event in(sg.WIN_CLOSED, 'Close') or event is None:
        break

    elif event == 'View Progress':
        goal_key = values['-GOALLISTBOX-'][0]
        goal_db_entry = goalDataBase.get(goal_key)

        print_basic_info_about_goal(goal_db_entry["saved"] ,goal_db_entry)

        myView.progress_bar.UpdateBar(goal_db_entry["saved"], goal_db_entry["cost"])

    elif event == 'Update Progress [Enter]':
        goal_key = values['-GOALLISTBOX-'][0]
        goal_db_entry = goalDataBase.get(goal_key)

        if values[0] == True:
            my_goal_savings_now = goal_db_entry["saved"] + int(values['-AMOUNT-'])
        elif values[1] == True:
            my_goal_savings_now = goal_db_entry["saved"] - int(values['-AMOUNT-'])

        print_basic_info_about_goal(my_goal_savings_now, goal_db_entry)

        goalDataBase.set(key=goal_key, value={
            "description": goal_db_entry["description"],
            "cost": goal_db_entry["cost"],
            "saved": my_goal_savings_now,
            "associated account": goal_db_entry["associated account"]
        })

        myView.progress_bar.UpdateBar(my_goal_savings_now, goal_db_entry["cost"])
