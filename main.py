#Класс EGRUser
# атрибуты пользователя системы
#__s_userF - Фамилия пользователя, обязательный атрибут
#__s_userI - Имя пользователя, обязательный атрибут
#__s_userO - Отчество пользователя, обязательный атрибут
#__s_userLogin - логин пользователя
#__s_userPost - должность пользователя
#__s_userDep - отдел пользователя
#__s_userTelN - телефонный номер пользователя
#__s_userEmail - емайл пользователя
#__s_userActive - признак работающего пользователя (работает, уволен, декрет, отпуск)
# методы


class EGRUser:
    '''
    #Класс EGRUser
        атрибуты пользователя системы
        __s_userF - Фамилия пользователя, обязательный атрибут
        __s_userI - Имя пользователя, обязательный атрибут
        __s_userO - Отчество пользователя, обязательный атрибут
        __s_userLogin - логин пользователя
        __s_userPost - должность пользователя
        __s_userDep - отдел пользователя
        __s_userTelN - телефонный номер пользователя
        __s_userEmail - емайл пользователя
        __s_userActive - признак работающего пользователя (работает, уволен, декрет, отпуск)
        методы
    '''

    # первичная инициализация пользователя
    # принимает строки - Фамилия, Имя, Отчество
    def __init__(self, f, i, o):
        self.__s_userF = f
        self.__s_userI = i
        self.__s_userO = o
        self.__s_userLogin = ''
        self.__s_userPost = ''
        self.__s_userDep = ''
        self.__s_userTelN = ''
        self.__s_userEmail = ''

    #Блок Get-Set методов
    #
    def getUserF(self):
        return self.__s_userF

    def setUserF(self, f):
        self.__s_userF = f

    def getUserI(self):
        return self.__s_userI

    def setUserI(self, i):
        self.__s_userI = i

    def getUserO(self):
        return self.__s_userO

    def setUserO(self, o):
        self.__s_userO = o

    def getUserLogin(self):
        return self.__s_userLogin
    ##генерируется автоматический
    #def setUserLogin(self):
    #    self.__s_userLogin = genLogin(self.__s_userF, self.__s_userI, self.__s_userO, self.__s_Dep)

    def getUserPost(self):
        return self.__s_userPost

    def setUserPost(self, post):
        self.__s_userPost = post

    def getUserDep(self):
        return self.__s_userDep

    def setUserDep(self, dep):
        self.__s_userDep = dep

    def __str__(self):
        userinfo = ("ФИО: " + self.__s_userF + " " + self.__s_userI + " " + self.__s_userO)
        return userinfo


def main():
    print("Тестирование Класса EGRUSER")
    userf = str(input("Введите Фамилию пользователя: "))
    useri = str(input("Введите Имя пользователя: "))
    usero = str(input("Введите Отчество пользователя: "))

    testuser = EGRUser(userf, useri, usero)
    print(testuser)

    testuser.setUserF("Тоткого")
    testuser.setUserI("Нельзя")
    testuser.setUserO("Называть")

    print(testuser)


if __name__ == '__main__':
    main()
