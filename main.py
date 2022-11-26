from package.application import salary
from package.application.db import people
import emoji



if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()

    print(emoji.emojize('Python is :thumbsup:', language='alias'))

