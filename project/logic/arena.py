from project.constants import DRAW, LOSE, WIN
from project.logic.unit import BaseUnit


class BaseSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Arena(metaclass=BaseSingleton):
    STAMINA_PER_ROUND = 1
    player = None
    enemy = None
    game_is_running = False
    battle_result = "Игра завершена"

    def start_game(self, player: BaseUnit, enemy: BaseUnit) -> None:
        self.player = player
        self.enemy = enemy
        self.game_is_running = True

    def _check_players_hp(self) -> bool | None:
        if self.player.hp <= 0:
            self.battle_result = WIN
            return True
        if self.enemy.hp <= 0:
            self.battle_result = LOSE
            return True
        if self.enemy.hp <= 0 and self.player.hp <= 0:
            self.battle_result = DRAW
            return True

    def _check_stamina(self, unit: BaseUnit) -> bool:
        return (
            unit.unit_class.max_stamina
            >= unit.stamina + unit.unit_class.stamina * self.STAMINA_PER_ROUND
        )

    def _stamina_regeneration(self) -> None:
        if self._check_stamina(self.player):
            self.player.stamina = round(
                self.player.stamina
                + self.player.unit_class.stamina * self.STAMINA_PER_ROUND,
                1,
            )
        if self._check_stamina(self.enemy):
            self.enemy.stamina = round(
                self.enemy.stamina
                + self.enemy.unit_class.stamina * self.STAMINA_PER_ROUND,
                1,
            )

    def next_turn(self) -> str:
        if self._check_players_hp():
            self.game_is_running = False
            return self.battle_result
        self._stamina_regeneration()
        return self.enemy.hit(self.player)

    def _end_game(self) -> str:
        self._instances = {}
        self.game_is_running = False
        return self.battle_result

    def player_hit(self) -> str:
        res = self.player.hit(self.enemy)
        self.next_turn()
        return res

    def player_use_skill(self) -> str:
        res = self.player.use_skill(self.enemy)
        self.next_turn()
        return res
