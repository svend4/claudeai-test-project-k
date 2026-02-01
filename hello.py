#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Простой приветственный скрипт
Демонстрирует базовые возможности Python
"""

def greet(name):
    """Приветствует пользователя по имени"""
    return f"Привет, {name}! 👋"

def main():
    """Главная функция"""
    print("=" * 50)
    print("  ДОБРО ПОЖАЛОВАТЬ В ТЕСТОВЫЙ ПРОЕКТ!")
    print("=" * 50)
    print()
    
    # Запрашиваем имя
    name = input("Как вас зовут? ")
    
    # Выводим приветствие
    message = greet(name)
    print()
    print(message)
    print()
    print("Этот скрипт создан через Desktop Commander!")
    print("=" * 50)

if __name__ == "__main__":
    main()
