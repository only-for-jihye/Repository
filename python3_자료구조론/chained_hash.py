# 체인법으로 해시 함수 구현하기

from __future__ import annotations
from typing import Any, Sequence
import hashlib

class Node:
    """해시를 구성하는 노드"""

    def __init__(self, key: Any, value: Any, next: Node) -> None:
        """초기화"""
        self.key = key      # 키
        self.value = value  # 값
        self.next = next    # 뒤쪽 노드를 참조

class ChainedHash:
    """체인법으로 해시 클래스 구현"""
    
    def __init__(self, capacity: int) -> None:
        """초기화"""
        self.capacity = capacity                # 해시 테이블의 크기를 지정
        self.table = [None] * self.capacity     # 해시 테이블(리스트)을 선언
    
    def hash_value(self, key: Any) -> int:
        """해시값을 구함"""
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)
        
        # sha256 알고리즘 : hashlib 모듈에서 제공하는 sha256은 RSA의 FIPS 알고리즘을 바탕으로 하며, 주어진 byte 문자열의 해시값을 구하는 해시 알고리즘의 생성자
        #                 hashlib 모듈은 sha256 외에도 MD5 알고리즘인 md5 등 다양한 해시 알고리즘을 제공함
        # encode() 함수 : hashlib.sha256에는 byte 문자열의 인수를 전달해야함. key를 str형 문자열로 변환한 뒤 그 문자열을 encode() 함수에 전달하여 byte 문자열을 생성함
        # hexdigest() 함수 : sha256 알고리즘에서 해시값을 16진수 문자열로 꺼냄
        # int() : hexdigest()로 꺼낸 문자열을 16진수 문자열로 하는 int형으로 변환함

    def search(self, key: Any) -> Any:
        """키가 key인 원소를 검색하여 값을 반환"""
        hash = self.hash_value(key)         # 검색하는 키의 해시값
        p = self.table[hash]                # 노드를 주목

        while p is not None:
            if p.key == key:
                return p.value              # 검색 성공
            p = p.next                      # 뒤쪽 노드를 주목

        return None
    
    def add(self, key: Any, value: Any) -> bool:
        """키가 key이고 값이 value인 원소를 추가"""
        hash = self.hash_value(key)         # 추가하는 key의 해시값
        p = self.table[hash]                # 노드를 주목

        while p is not None:
            if p.key == key:
                return False                # 추가 실패
            p = p.next                      # 뒤쪽 노드를 주목
        
        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp             # 노드를 추가
        return True                         # 추가 성공

    def remove(self, key: Any) -> bool:
        """키가 value인 원소를 삭제"""
        hash = self.hash_value(key)         # 삭제할 key의 해시값
        p = self.table[hash]                # 노드를 주목
        pp = None                           # 바로 앞의 노드를 주목
        
        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True                 # key 삭제 성공
            pp = p
            p = p.next                      # 뒤쪽 노드를 주목
        return False
    
    def dump(self) -> None:
        """해시 테이블을 덤프"""
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f'    -> {p.key} ({p.value})', end='')
                p = p.next
            print()
