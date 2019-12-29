class MyBlock:
    def __init__(self, id, name, next, parent):
        self.id = id
        self.name = name
        self.next = next
        self.parent = parent
        self.substack = None
        self.substack2 = None
        self.procId = None
        self.condition = None
        self.broadcast = ''
        self.location = -1
        self.listName = ''
        self.listContent = ''
        self.isDead = False

    def getCount(self):
        return MyBlock.blockCount

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getNext(self):
        return self.next

    def getParent(self):
        return self.parent

    def getIsDead(self):
        return self.isDead

    def setIsDead(self, bool):
        self.isDead = bool

    def getSubstack(self):
        return self.substack

    def setSubstack(self, id):
        self.substack = id

    def getSubstack2(self):
        return self.substack2

    def setSubstack2(self, id):
        self.substack2 = id

    def getProcId(self):
        return self.procId

    def setProcId(self, id):
        self.procId = id

    def getCondition(self):
        return self.condition

    def setCondition(self, condition):
        self.condition = condition

    def getBroadcast(self):
        return self.broadcast

    def setBroadcast(self, broadcast):
        self.broadcast = broadcast

    def getLocation(self):
        return self.location

    def setLocation(self, location):
        self.location = location
    def getListName(self):
        return self.listName

    def setListName(self, name):
        self.listName = name

    def getListContent(self):
        return self.listContent

    def setListContent(self, content):
        self.listContent = content