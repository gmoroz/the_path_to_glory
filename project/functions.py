from project.container import heroes


def check_heroes() -> bool:
    return heroes.get("player") and heroes.get("enemy")
