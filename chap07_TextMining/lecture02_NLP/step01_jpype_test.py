"""  
step01_jpype_test.py

JAVA 가상머신 사용을 위한 패키지 설치와 테스트
"""
import jpype
path = jpype.get_default_jvm_path()
path