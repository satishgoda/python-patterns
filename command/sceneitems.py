from collections import deque

class Item(object):
    def __init__(self, name, color='red', pos=(0, 0)):
        self.name = name
        self.color = color
        self.pos = pos
    
    def __repr__(self):
        return "<Item {0} {1} {2} {3}>".format(self.name, self.color, *self.pos)
    
    def setColor(self, color):
        self.color = color
    
    def setPos(self, pos):
        self.pos = pos

class Scene(object):
    def __init__(self):
        self.items = []
        
    def addItem(self, item):
        self.items.append(item)
    
    def removeItem(self, item):
        self.items.remove(item)

##

class CommandQueue(object):
    def __init__(self):
        self._undo = deque()
        self._redo = deque()
    
    def undo_queue(self, command):
        self._undo.append(command)
        print self._undo
    
    def redo_queue(self, command):
        self._redo.append(command)
        print self._redo
    
    def undo(self):
        command = self._undo.pop()
        print self._undo
        self.redo_queue(command)
        return command

    def redo(self):
        command = self._redo.pop()
        print self._redo
        self.undo_queue(command)
        return command

cq = CommandQueue()
cq.undo()
cq.redo()
cq.undo_queue("add-item")
cq.undo_queue("set-color")
cq.undo_queue("set-pos")
cq.undo()
cq.redo()

##
class Command(object):
    def __repr__(self):
        return "<Cmd {0}>".format(self.cmd_type)

class AddItemCommand(Command):
    cmd_type = 'add-item'
    
    def __init__(self, ctx):
        self.ctx = ctx
        self.item = None
    
    def redo(self):
        self.item = Item('unnamed')
        self.ctx.scene.addItem(self.item)
        self.ctx.item = self.item
        
    def undo(self):
        self.ctx.scene.removeItem(self.item)
        self.item = None
        self.ctx.item = None

class SetColorCommand(Command):
    cmd_type = 'set-color'
    
    def __init__(self, ctx, color):
        self.ctx = ctx
        self.color = color
        self.prevColor = self.ctx.item.color
    
    def redo(self):
        self.ctx.item.setColor(self.color)
        
    def undo(self):
        self.ctx.item.setColor(self.prevColor)
##
    
scene = Scene()
ctx = Context()
commandqueue = CommandQueue()

ctx.scene = scene

addItemCmd = AddItemCommand(ctx)
addItemCmd.redo()
ctx.scene.items
ctx.item
commandqueue.undo_queue(addItemCmd)

# ctx.scene.items
# ctx.item = ctx.scene.items[0]

setColorCmd = SetColorCommand(ctx, 'blue')
setColorCmd.redo()
ctx.item
commandqueue.undo_queue(setColorCmd)

cmd = commandqueue.undo()
cmd.undo()
ctx.item

cmd = commandqueue.undo()
cmd.undo()
ctx.scene.items
ctx.item
