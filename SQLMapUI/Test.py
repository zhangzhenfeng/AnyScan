from attack.AttackObject import AttackObject

from attack.AttackBase import AttackBase

if __name__ == "__main__":
    attackObject = AttackObject()
    attackObject.timeout = 20
    attackObject.threads = 30
    attacker = AttackBase(attackObject)
    attacker.attack()