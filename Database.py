import json
import os

class budgetDatabase(object):
    def __init__(self, location):
        self.location = os.path.expanduser(location)
        self.load()

    def load(self):
        if os.path.exists(self.location):
            self._load()
        else:
            self.db = {}
        return True

    def _load(self):
        self.db = json.load(open(self.location, "r"))

    def dumpdb(self):
        try:
            json.dump(self.db, open(self.location, "w+"))
            return True
        except:
            return False
    def set(self, key, value):
        try:
            self.db[str(key)] = value
            self.dumpdb()
            return True
        except Exception as e:
            print("[X] Error Saving Values to Database")
            return False

    def get(self, key):
        try:
            return self.db[key]
        except KeyError:
            print("No Value can be Found for" + str(key))
            return False

    def gather_keys(self):
        try:
            return list(key for key in self.db.keys())
            return True
        except Exception as e:
            print(e)
            return False

    def delete(self, key):
        if not key in self.db:
            return False
        del self.db[key]
        self.dumpdb()
        return True

    def resetdb(self):
        self.db = {}
        self.dumpdb()
        return True


if __name__ == "__main__":
    DC_GOAL = {
        "key": "Living in Washington DC",
        "value":{
            "description": "Rent an apartment for 1k per month in DC",
            "cost": 6000,
            "saved": 1000,
            "associated account": "Foo Bar LLC."

    }
    }

    myDB = budgetDatabase(location=r"C:\code\BudgetApp\database\myDB.json")
    myDB.set(DC_GOAL["key"], DC_GOAL["value"])