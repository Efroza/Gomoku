##
## EPITECH PROJECT, 2022
## B-MAT-500-PAR-5-1-pbrain-gomoku-ai-luc1.schmitt
## File description:
## Makefile
##

FILE	=	src/*.py

NAME	=	pbrain-gomoku-ai

$(NAME):
			cp -r $(FILE) .
			mv pbrain-gomoku-ai.py pbrain-gomoku-ai
			chmod 777 pbrain-gomoku-ai

all	:	$(NAME)

clean	:
		rm -rf pbrain-gomoku-ai
		rm -rf pbrain-gomoku-ai.spec

fclean :	clean
		rm -rf dist
		rm -rf build
		rm -rf __pycache__
		rm -f *.py

re	:	fclean all

exe	:
		python3 -m pip install pyinstaller
		python3 -m PyInstaller --onefile ./src/$(NAME).py

.PHONY: all clean fclean re
