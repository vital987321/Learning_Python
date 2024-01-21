1. Correct scores file format:
Name    Level	Score
darkforce   Normal	7
Stepan	Normal	6
2. Exceptions. Is everything ok?
3. ~~exceptions.py: Містить клас GameOver - унаслідований від Exception. В класі має бути реалізований метод для збереження фінального рахунку гри по її завершенню.~~
4. Some class methods could be privat
5. do we really need participant class? Give it common staf or remove it.
6. add Hard game level. При виборі Hard кілкість життів противника множиться на N та кількість очків множиться на N
N зберігається в налаштуваннях
7. annotations, docstrings
8. replace score.txtx by a constant
9. format to pep8
10. Partisipant abstract method shall raise exception
11. ?posibility to exit game in the middle of the game (keyboard Interupted)