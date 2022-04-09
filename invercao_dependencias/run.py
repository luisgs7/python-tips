from use_case.my_usecase import MyUseCase
from database.some_database_1 import Database1
from database.some_database_2 import Database2

use_case = MyUseCase(Database2())

use_case.search_something()
use_case.insert_something()