from attack.AttackObject import AttackObject

from attack.AttackBase import AttackBase

if __name__ == "__main__":
    # attackObject = AttackObject()
    # attackObject.timeout = 20
    # attackObject.threads = 30
    # attacker = AttackBase(attackObject)
    # attacker.attack()
    l = ['192.168.1.24', '192.168.1.25', '192.168.1.22', '192.168.1.23', '192.168.1.20', '192.168.1.21', '192.168.1.7', '192.168.1.6', '192.168.1.5', '192.168.1.4', '192.168.1.3', '192.168.1.2', '192.168.1.1', '192.168.1.9', '192.168.1.8', '192.168.1.19', '192.168.1.18', '192.168.1.13', '192.168.1.12', '192.168.1.11', '192.168.1.10', '192.168.1.17', '192.168.1.16', '192.168.1.15', '192.168.1.14']
    print l.sort(lambda x,y: cmp(''.join( [ i.rjust(3, '0') for i in x.split('.')] ), ''.join( [ i.rjust(3, '0') for i in y.split('.')] ) ) )
    print l