# Thailand.py
class ThailandPackage:
    def detail(): # 
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")

				
				
# Vietnam.py
class VietnamPackage:
    def detail():
        print("[베트남 패키지 3박 5일] 방콕, 다낭 효도 여행 60만원")
				
				
				
# __init__.py	
__all__ = ["Vietnam", "Thailand"]



#Traveltest.py

# import Travel.Thailand # Travel 패키지 밑에 있는 Thailand 모듈 불러옴

# trip_to = Travel.Thailand.ThilandPackage # trip_to 객체 생성 , 클래스 불러옴( detail 함수 사용 가능 )

# trip_to.detail()

# --------------------------------------------

from Travel import * # Travel 패키지 안에 있는 모든 것들을 들고 온다

trip_to = Thailand.ThailandPackage # trip_to 객체 생성 , 클래스 불러옴( detail 함수 사용 가능 )
trip_to.detail()

trip_to2 = Vietnam.VietnamPackage
trip_to2.detail()

# ------------------------------------

# from Travel.Thailand import ThailandPackage
# trip_to = ThailandPackage
# trip_to.detail()