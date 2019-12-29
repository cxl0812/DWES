# Generated from C:/Users/cxl/Desktop/Scratch3Analysis\Scratch.g4 by ANTLR 4.7
from antlr4 import *
import json
from MyBlock import MyBlock
if __name__ is not None and "." in __name__:
    from .ScratchParser import ScratchParser
else:
    from ScratchParser import ScratchParser

# This class defines a complete listener for a parse tree produced by ScratchParser.
class ScratchListener(ParseTreeListener):
    def __init__(self):
        self.id_block = {}
        self.block_count = 0
        self.sprite_count = 0
        self.comment_count = 0
        self.broadcast_received = []
        self.broadcast = []
        self.list = {}

    # Enter a parse tree produced by ScratchParser#json.
    def enterJson(self, ctx:ScratchParser.JsonContext):
        pass

    # Exit a parse tree produced by ScratchParser#json.
    def exitJson(self, ctx:ScratchParser.JsonContext):
        pass


    # Enter a parse tree produced by ScratchParser#AnObject.
    def enterAnObject(self, ctx:ScratchParser.AnObjectContext):
        pass

    # Exit a parse tree produced by ScratchParser#AnObject.
    def exitAnObject(self, ctx:ScratchParser.AnObjectContext):
        pass


    # Enter a parse tree produced by ScratchParser#EmptyObject.
    def enterEmptyObject(self, ctx:ScratchParser.EmptyObjectContext):
        pass

    # Exit a parse tree produced by ScratchParser#EmptyObject.
    def exitEmptyObject(self, ctx:ScratchParser.EmptyObjectContext):
        pass


    # Enter a parse tree produced by ScratchParser#APair.
    def enterAPair(self, ctx:ScratchParser.APairContext):
        key = ctx.getChild(0).getText().replace('\"', '')
        if key == "targets":
            value = json.loads(ctx.getChild(2).getText())
            # print("enter targets!!!!!", value)
            for dicc in value:
                for dicc_key, dicc_value in dicc.items():
                    if dicc_key == "isStage":
                        if dicc_value is False:
                            self.sprite_count += 1

                    if dicc_key == "lists":
                        for list_id, list_value in dicc_value.items():
                            list_name = list_value[0]
                            index_list = list_value[1]
                            self.list[list_name] = index_list

                    if dicc_key == "blocks":
                        for block_id, block_value in dicc_value.items():
                            next_id = None
                            parent_id = None
                            substack = None
                            substack2 = None
                            condition = None
                            list_name = None
                            list_location = None
                            list_content = None
                            id = block_id
                            if type(block_value) is dict:
                                for key, value in block_value.items():
                                    # print('key value', key, value)
                                    if key == "opcode":
                                        name = value
                                    if key == "next":
                                        next_id = value
                                    if key == "parent":
                                        parent_id = value
                                    if key == "inputs":
                                        input_item = value
                                        for input, input_content in input_item.items():
                                            if input == "CONDITION":
                                                condition = input_content[1]
                                            if input == "SUBSTACK":
                                                substack = input_content[1]
                                            if input == "SUBSTACK2":
                                                substack2 = input_content[1]
                                            if input == "BROADCAST_INPUT":
                                                if type(input_content[1]) is list:
                                                    broadcast_name = input_content[1][1]
                                                else:
                                                    broadcast_name = input_content[1]
                                                self.broadcast.append(broadcast_name)
                                            if input == "INDEX":
                                                if type(input_content[1]) is list:
                                                    list_location = input_content[1][1]
                                                else:
                                                    list_location = input_content[1]
                                            if input == "ITEM":
                                                if type(input_content[1]) is list:
                                                    list_content = input_content[1][1]
                                                else:
                                                    list_content = input_content[1]
                                    if key == "fields":
                                        field_item = value
                                        for field, field_content in field_item.items():
                                            if field == "LIST":
                                                list_name = field_content[0]
                                                if type(list_name) is list:
                                                    list_name = str(list_name).replace('[', '').replace(']',
                                                                                                        '').replace(
                                                        "'", '').replace(" ", '')
                                                # print('listname!!!!!', list_name, type(list_name))
                                            if field == "BROADCAST_OPTION":
                                                broadcast_name = field_content[0]
                                                self.broadcast_received.append(broadcast_name)

                                myBlock = MyBlock(id, name, next_id, parent_id)
                                cblock = {'control_repeat', 'control_forever', 'control_if', 'control_if_else',
                                          'control_repeat_until'}
                                condition_block = {'control_if', 'control_if_else', 'control_wait_until',
                                                   'control_repeat_until'}
                                broadcast_block = {'event_whenbroadcastreceived', 'event_broadcast',
                                                   'event_broadcastandwait'}
                                location_block = {'data_deleteoflist', 'data_insertatlist', 'data_replaceitemoflist'}
                                listname_block = {'data_addtolist', 'data_deleteoflist', 'data_deletealloflist',
                                                  'data_insertatlist',
                                                  'data_replaceitemoflist', 'data_itemoflist', 'data_itemnumoflist',
                                                  'data_lengthoflist',
                                                  'data_listcontainsitem', 'data_showlist', 'data_hidelist'}
                                listContent_block = {'data_addtolist', 'data_insertatlist', 'data_replaceitemoflist'}
                                if name in cblock and substack is not None:
                                    myBlock.setSubstack(substack)
                                if name == 'control_if_else' and substack2 is not None:
                                    myBlock.setSubstack2(substack2)
                                if name in condition_block:
                                    myBlock.setCondition(condition)

                                if name in broadcast_block:
                                    myBlock.setBroadcast(broadcast_name)

                                if name in location_block:
                                    myBlock.setLocation(list_location)

                                if name in listname_block:
                                    myBlock.setListName(list_name)

                                if name in listContent_block:
                                    myBlock.setListContent(list_content)

                                self.id_block[id] = myBlock
                                self.block_count += 1

                    if dicc_key == "comments":
                        for comment_id, comment_value in dicc_value.items():
                            self.comment_count += 1
        pass

    # Exit a parse tree produced by ScratchParser#APair.
    def exitAPair(self, ctx:ScratchParser.APairContext):







        pass


    # Enter a parse tree produced by ScratchParser#ArrayOfValues.
    def enterArrayOfValues(self, ctx:ScratchParser.ArrayOfValuesContext):
        pass

    # Exit a parse tree produced by ScratchParser#ArrayOfValues.
    def exitArrayOfValues(self, ctx:ScratchParser.ArrayOfValuesContext):
        pass


    # Enter a parse tree produced by ScratchParser#EmptyArray.
    def enterEmptyArray(self, ctx:ScratchParser.EmptyArrayContext):
        pass

    # Exit a parse tree produced by ScratchParser#EmptyArray.
    def exitEmptyArray(self, ctx:ScratchParser.EmptyArrayContext):
        pass


    # Enter a parse tree produced by ScratchParser#Stringjson.
    def enterStringjson(self, ctx:ScratchParser.StringjsonContext):
        pass

    # Exit a parse tree produced by ScratchParser#Stringjson.
    def exitStringjson(self, ctx:ScratchParser.StringjsonContext):
        pass


    # Enter a parse tree produced by ScratchParser#Atom.
    def enterAtom(self, ctx:ScratchParser.AtomContext):
        pass

    # Exit a parse tree produced by ScratchParser#Atom.
    def exitAtom(self, ctx:ScratchParser.AtomContext):
        pass


    # Enter a parse tree produced by ScratchParser#ObjectValue.
    def enterObjectValue(self, ctx:ScratchParser.ObjectValueContext):
        pass

    # Exit a parse tree produced by ScratchParser#ObjectValue.
    def exitObjectValue(self, ctx:ScratchParser.ObjectValueContext):
        pass


    # Enter a parse tree produced by ScratchParser#ArrayValue.
    def enterArrayValue(self, ctx:ScratchParser.ArrayValueContext):
        pass

    # Exit a parse tree produced by ScratchParser#ArrayValue.
    def exitArrayValue(self, ctx:ScratchParser.ArrayValueContext):
        pass


