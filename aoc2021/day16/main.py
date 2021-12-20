#!/usr/bin/env python3

import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

class Packet:

    def __init__(self, packet_str):
        self.packet = packet_str
        self.idx = 0
        self.children = []

    def consume_padding(self):
        return True
    
    def next(self, len:int):
        tmp = self.packet[self.idx:self.idx + len]
        self.idx += len
        return tmp 

    def peak(self, len:int=None):
        if len == None:
            return self.packet[self.idx:]
        return self.packet[self.idx:self.idx + len]

    def rewind(self, len:int = -1): 
        start = self.idx
        if len == -1: 
            self.idx = 0
        else:
            self.idx = max(0, self.idx - len)
        return start - self.idx

    def length(self):
        if self.idx == len(self.packet):
            return self.idx
        return self.idx - 1

    def value(self):
        if hasattr(self, 'result'): 
            return self.result
        elif hasattr(self, 'literal'):
            return self.literal
        else: 
            raise ValueError("This packet does not have a value.")

    def add_child(self, child):
        self.children.append(child)
        if isinstance(child, SubPacket):
            child.add_parent(self)

    def __repr__(self, prefix:str=""):
        attrs = vars(self)
        representation = ["\n"]
        keys = ['packet', 'idx', 'version', 'type_id', 'literal', 'len_type_id', 'total_length', 'result']
        for key in keys:
            if key in attrs.keys():
                representation.append(f"{prefix}{key}: {attrs[key]}\n") 
        representation.append(f"{prefix}children: %d"%(len(self.children)))
        for child in self.children:
            representation.append(child.__repr__(" | "))
            representation.append(f"\n{prefix}  |" + '-'*21)

        return(' '.join(representation)) 

class SubPacket(Packet):

    def consume_padding(self):
        return False

    def add_parent(self, parent):
        self.parent = parent

def read_packet(packet:Packet):
    '''
    Literal value packets encode a single binary number. To do this, the binary number is padded with leading zeroes until its length is a multiple of four bits, and then it is broken into groups of four bits. Each group is prefixed by a 1 bit except the last group, which is prefixed by a 0 bit. These groups of five bits immediately follow the packet header. For example, the hexadecimal string D2FE28 becomes:

    110100101111111000101000
    VVVTTTAAAAABBBBBCCCCC
    '''

    packet.version = int(packet.next(3),2)
    packet.type_id = int(packet.next(3),2)
    
    if packet.type_id == 4: 
        # Value packet
        val = []
        while True: 
            # read 5 bytes
            nxt = packet.next(5)
            val.append(nxt[1:])
            # if starts with 0, we are at the last byte
            if nxt[0] == '0':
                break
        packet.literal = int(''.join(val),2)

        # if packet.consume_padding():
        #     paddings = 0
        #     while packet.peak(1) == '0':
        #         packet.next(1)
        #         paddings += 1
            
        # print("Remainder: %s" % packet.peak())
    else: 
        packet.len_type_id = packet.next(1)
        if packet.len_type_id == '0':
            packet.total_length = int(packet.next(15),2)

            sub_packets = packet.next(packet.total_length)
            start_idx = 0
            while start_idx < packet.total_length:
                sub_packet = sub_packets[start_idx:]
                sub_packet = Packet(sub_packet)
                start_idx += read_packet(sub_packet) + 1
                packet.add_child(sub_packet)

        else:
            packet.sub_packets = int(packet.next(11),2)
            
            leftover = packet.peak()
            for i in range(packet.sub_packets):
                sub = SubPacket(leftover)
                pkt_len = read_packet(sub) + 1
                packet.next(pkt_len)
                packet.add_child(sub)

                leftover = packet.peak()
        
        # Compute the calculation in part 2
        if packet.type_id == 0: 
            # Sum the packets
            packet.result = 0
            for child in packet.children:
                packet.result += child.value()
        elif packet.type_id == 1:
            packet.result = 1
            for child in packet.children:
                packet.result *= child.value()
        elif packet.type_id == 2:
            packet.result = packet.children[0].value()
            for child in packet.children[1:]:
                packet.result = min(packet.result, child.value())
        elif packet.type_id == 3:
            packet.result = packet.children[0].value()
            for child in packet.children[1:]:
                packet.result = max(packet.result, child.value())
        elif packet.type_id == 5:
            packet.result = int(packet.children[0].value() > packet.children[1].value())
        elif packet.type_id == 6:
            packet.result = int(packet.children[0].value() < packet.children[1].value())
        elif packet.type_id == 7:
            packet.result = int(packet.children[0].value() == packet.children[1].value())

    return packet.length()

def sum_versions(packet):

    summed = packet.version
    if packet.children: 
        for child in packet.children:
            summed += sum_versions(child)
    return summed

line = ''
with open(f"{dir_path}/input.txt", "r") as f:
# with open(f"{dir_path}/sample.txt", "r") as f:
# with open(f"{dir_path}/sample2.txt", "r") as f:

    lines = [line.strip() for line in f.readlines()]

    for original in lines:
        line = ''.join(['{:04b}'.format(int(chr,16)) for chr in original])
        print("Original: %s\n" % original.strip())
        # print("Decoded: %s\n" % line)

        packet = Packet(line)
        read_packet(packet)

        # pt 1
        print('pt 1 - Sum of packet versions: %d' % sum_versions(packet))
        # pt 2
        print("pt 2 - End value of packet calculation(s): %d" % packet.result)
        print('-'*80)
