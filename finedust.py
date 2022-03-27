{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "finedust.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMjVOFL8JOVqZ1CUYvtYZeY",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/hunsucki/suki/blob/main/finedust.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "1oxFfXyV_sYc"
      },
      "outputs": [],
      "source": [
        "from bs4 import BeautifulSoup\n",
        "import time\n",
        "import requests\n",
        "import urllib.request\n",
        "import urllib.parse\n",
        "Time = time.strftime('%Y%m%d%H')\n",
        "Current_time = int(Time) +int(8)\n",
        "key = 'gHStf7x6cwy%2FOx6meAjMGLU6%2BpnQGv65wTGhMgPvf7cxVz5%2B664v5XhLKIeEibwfWfR8CTUqXZYYStXDkUcd2w%3D%3D'\n",
        "key_1 = 'gHStf7x6cwy%2FOx6meAjMGLU6%2BpnQGv65wTGhMgPvf7cxVz5%2B664v5XhLKIeEibwfWfR8CTUqXZYYStXDkUcd2w%3D%3D'\n",
        "url = \"http://apis.data.go.kr/6260000/AirQualityInfoService/getAirQualityInfoClassifiedByStation?serviceKey=\" + key_1 + \"&pageNo=1&numOfRows=5&resultType=xml&areaIndex=\"\n",
        " \n",
        "area = { '광복동':221112, '초량동':221131, '태종대':221141, '전포동':221152, '온천동':221163, '명장동':221163, '대연동':221172,\n",
        "         '학장동':221181, '덕천동':221182, '청룡동':221191, '좌동'  :221192, '장림동':221202, '대저동':221211, '녹산동':221212,\n",
        "         '연산동':221221, '기장읍':221231, '용수리':221233, '수정동':221241, '부곡동':221251, '광안동':221271, '대신동':221281\n",
        "       }\n",
        "area_list = list(area.keys())\n",
        "print(area_list,'중 하나를 입력해 주세요.')\n",
        "Current_location = str(input())\n",
        " \n",
        "if Current_location not in area.keys():\n",
        "    print(Current_location,'은/는 목록에 없어요.')\n",
        " \n",
        "elif Current_location in area.keys():\n",
        "    area_code = area.get(Current_location)\n",
        "    furl = url + str(area_code) + \"&controlnumber=\" + str(Current_time)\n",
        "    response = requests.get(furl)\n",
        "    response_text = response.text\n",
        "    soup = BeautifulSoup(response_text ,\"html.parser\")\n",
        "    \n",
        " \n",
        "    for response in soup.find_all(\"item\"):\n",
        "      time = response.find(\"controlnumber\").get_text()\n",
        "      time = time[0:4] + '년 ' + time[4:6] + '월 ' + time[6:8] + '일 ' + time[8:10] + '시'\n",
        "      site = response.find(\"site\").get_text()\n",
        "      PM10 = response.find(\"pm10\").get_text()\n",
        "      PM25 = response.find(\"pm25\").get_text()\n",
        "      print(\n",
        "          \"측정소:\", site, \"측정소\\n\"\n",
        "          \"측정소 코드:\", area_code, \"\\n\"\n",
        "          \"측정시간:\", time , \"\\n\"\n",
        "          \"미세먼지 농도:\", PM10, \"㎍/㎥ \\n\"\n",
        "          \"초미세먼지 농도:\", PM25, \"㎍/㎥ \\n\"\n",
        "      )"
      ]
    }
  ]
}