import urllib.request, bs4


def hos2():

    web_page = urllib.request.urlopen("http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun=")

    result_code = bs4.BeautifulSoup(web_page, 'html.parser')
    find_info = result_code.find_all(class_="data_table mgt16 tbl_scrl_m mini")

    taget = find_info[1]
    print(taget.get_text())