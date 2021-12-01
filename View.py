import threading
import time
import PySimpleGUI as sg


sg.theme('BlueMono')

class View:
    def __init__(self, DB_MGMT):

        # Retrieve list of goals from the database
        goalList = DB_MGMT.gather_keys()

        layout = \
        [
            [sg.Text('Select a Goal:')],
            [sg.Listbox(values=goalList,
                        size=(100, len(goalList)),
                        change_submits=True,
                        bind_return_key=True,
                        auto_size_text=True,
                        default_values=goalList[0],
                        key='-GOALLISTBOX-', enable_events=True)],
            [sg.Output(key='-OUT-', size=(100, 20))],
            [sg.Button('View Progress', bind_return_key=False), sg.Button('Close')],
            [[sg.Text('Your progess:')], [sg.ProgressBar(1, orientation='h', size=(100, 50), key='-PROGRESS-')]],

            # Use the fields below to enter a transaction into the ledger

            [sg.Text('Transaction Amount'), sg.Input(key="-AMOUNT-", size=(20, 1))],
            [sg.Radio('Deposit into goal', "-RADIO1-", default=True)],
            [sg.Radio('Withdraw from goal', "-RADIO1-", default=False)],
            [sg.Button('Update Progress [Enter]', bind_return_key=True), sg.Button('Close')],
        ]

        self.window = sg.Window('Goal Tracker', layout, finalize=True)
        self.window['-OUT-'].TKOut.output.config(wrap='word')
        self.progress_bar = self.window['-PROGRESS-']
