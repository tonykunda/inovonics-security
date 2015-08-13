import serial
import threading
import inovonics_products
from binascii import hexlify
from bitstring import BitStream
from Queue import Queue

class InovonicsCommunication(object):

	def __init__(self, serial_port, logging):
		self.logging = logging
		self.serial_port = serial_port
		self.message_queue = Queue(maxsize=0)
		self.event_queue = Queue(maxsize=0)
		self.serial_thread = threading.Thread(target=self.inovonics_serial_read, name="Ino Serial")
		self.message_processing = threading.Thread(target=self.inovonics_message_processing, name="Ino Processing")

	def start_processing(self):
		self.serial_thread.start()
		self.message_processing.start()

	def serial_to_dec(self, source):
		hex_data = ''.join('%02x' % ord(c) for c in source)
		return int(hex_data, 16)
		
	def inovonics_serial_read(self):
		ser = serial.Serial(self.serial_port)
		self.logging.info("Opening " + str(ser.name))
		previous_packet = 0
		while True:
			header = ser.read(1)
			# Incoming Message
			if header == '\x13':
				data_length = ser.read(1)
				packet = ser.read(self.serial_to_dec(data_length) - 1)
				packet_bitstream = BitStream(bytes=header+data_length+packet)
				# Filter out duplicate messages, don't filter check in messages, Eg: (\x10)
				stat0 = (packet_bitstream[96:104])
				packet_without_rssi = (packet_bitstream[:-24])
				if packet_without_rssi == previous_packet and stat0 is not '\x10':
					pass
				else:
					self.message_queue.put(packet_bitstream)
					previous_packet = packet_without_rssi
			# Receiver Message
			elif header == '\x11':
				data_length = ser.read(1)
				packet = ser.read(self.serial_to_dec(data_length) - 1)
				packet_bitstream = BitStream(bytes=header+data_length+packet)
				self.message_queue.put(packet_bitstream)
			# Toss Everything Else
			else:
				self.logging.debug("Unknown Byte -- Discarded")
				self.logging.debug(''.join('%02x' % ord(c) for c in header))

	def inovonics_message_processing(self):
		while True:
			packet = self.message_queue.get()
			self.logging.debug(packet)
			ino_header = packet[0:8].hex
			if ino_header == "13":
				ino_length = packet[8:16].int
				ino_mid = packet[16:24].hex
				ino_uid = packet[24:48].uint
				ino_receiver_type = packet[48:56].hex
				ino_receiver_uid = packet[56:80].uint
				ino_pti = packet[80:88].int
				ino_stat1 = packet[88:96].bin
				ino_stat0 = packet[96:104].bin
				ino_level = packet[104:112].int
				ino_margin = packet[112:120].int
				ino_cksum = packet[120:128].hex
				self.event_queue.put(self.inovonics_security_message(ino_stat1+ino_stat0, ino_uid, inovonics_products.inovonics_product(ino_pti)))
			elif ino_header == "11":
				ino_length = packet[8:16].int
				ino_data = packet[16:24].int
				ino_stat1 = packet[24:32].bin
				ino_cksum = packet[32:40].hex

	def inovonics_security_message(self, status, uid, pti):
		status_list = []
		# Stat1
		if int(status[0:1]): status_list.append("EOL Tamper")
		if int(status[1:2]): status_list.append("Clean Me")
		if int(status[2:3]): status_list.append("Reserved")
		if int(status[3:4]): status_list.append("Reserved")
		if int(status[4:5]): status_list.append("Alarm 4")
		if int(status[5:6]): status_list.append("Alarm 3")
		if int(status[6:7]): status_list.append("Alarm 2")
		if int(status[7:8]): status_list.append("Alarm 1")
		# Stat0
		if int(status[8:9]): status_list.append("Reserved")
		if int(status[9:10]): status_list.append("Low Battery")
		if int(status[10:11]): status_list.append("Case and Wall Tamper")
		if int(status[11:12]): status_list.append("No Change")
		if int(status[12:13]): status_list.append("Reset")
		if int(status[13:14]): status_list.append("Reserved")
		if int(status[14:15]): status_list.append("Reserved")
		if int(status[15:16]): status_list.append("Reserved")
		return {"uid":uid, "pti":pti, "status":status_list, "event_type":"device"}