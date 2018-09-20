#!/usr/bin/env python3
#get_data_from_api.py - connect to my api to get students data

import json, requests, urllib

def main():
    class Person:
        """Base class for Student, other w8ing for implementation"""
        def __init__(self, name, last_name):
            self.name = name
            self.last_name = last_name
    class Student(Person):
        """Inherited from Person class - implements basic functionalities for Student"""
        def __init__(self, name, last_name, index_nr, marks, absence):
            super().__init__(name, last_name)
            self.index_nr    = index_nr
            self.marks    = marks
            self.absence = absence
        def mean_marks(self):
            """Returns mean marks for student"""
            mean = np.mean(self.marks)
            return mean
        def attendance(self):
            """Returns string depending on nr of missed days"""
            if self.absence <= 2:
                return "good"
            else:
                return "bad"
        def identify(self):
            """Returns string: name, last_name, index: index_nr marks mean: mean_marks and is a student with
            attendance() - absence days"""
            print("%s %s, index: %s marks mean: %.1f, and is a student with %s attendance - %i days" % 
                  (self.name, self.last_name, self.index_nr, self.mean_marks(), self.attendance(), self.absence))
    
    # download the JSON data from API
    class ConnectionAPI:
        def __init__(self):
            pass
        @staticmethod
        def get_data(limit):
            url ='https://still-sea-49183.herokuapp.com/api/v1/users?access_token=abracadabra&limit=%i' % (limit)
            response = requests.get(url)
            response.raise_for_status()
            studentData = json.loads(response.text)
            studentArray = list()
            for entry in studentData['users']:
                studentArray.append(Student(entry['name'], entry['last_name'], entry['index_nr'], entry['marks'], entry['absence']))
            return studentArray
            
    students = ConnectionAPI.get_data(3)
    
    
    
    print(students)
    print(students[2].name)
    
if __name__ == "__main__":
    main()