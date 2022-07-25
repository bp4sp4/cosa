import urllib.request, bs4, cx_Oracle
import requests


def hos0():

    web_page = urllib.request.urlopen("http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun=")

    result_code = bs4.BeautifulSoup(web_page, 'html.parser')
    find_info = result_code.find_all(class_="caseTable")

    taget = find_info[0]
    print(taget.get_text())

    conn = cx_Oracle.connect()




