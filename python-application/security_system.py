import ino_com
import logging
import database

log = logging
logFormat = '%(asctime)-15s %(levelname)s %(threadName)s %(message)s'
log.basicConfig(format=logFormat, level="DEBUG")


class SecuritySystem(object):
	def __init__(self, serial):
		self.db = database.DatabaseCommunication()
		self.ino_serial = serial
		self.inovonics = ino_com.InovonicsCommunication(self.ino_serial, log)
		self.devices = self.db.single_column("SELECT serial FROM alarm_device")
		self.device_list = {}
		for device in self.devices:
			self.device_list[device] = {"alarm1":False, "alarm2":False, "alarm3":False, "alarm4":False, "tamper":False, "low_battery":False}

	def start_system(self):
		self.inovonics.start_processing()
		self.event_processing()

	def alarm_needed(self, uid):
		armed, system_alarm = self.db.single_row("SELECT zone.armed, endpoint.system_alarm FROM endpoint LEFT JOIN zone ON endpoint.zone_id = zone.id WHERE endpoint.serial_id = '%s'" % (uid))
		if armed and not system_alarm:
			return armed

	def create_alarm (self, uid):
		zone, endpoint = self.db.single_row("SELECT zone.description, endpoint.description FROM endpoint LEFT JOIN zone ON endpoint.zone_id = zone.id WHERE endpoint.serial_id = '%s'" % (uid))
		self.db.write("INSERT INTO alarm (start_time, next_alert, alarm_text) VALUES (NOW(), NOW(), 'ALARM! in %s zone on %s')" % (zone, endpoint))
		self.db.write("UPDATE endpoint SET system_alarm = 1 WHERE serial_id = '%s'" % (uid))


	def event_processing(self):
		while True:
			#try:
				event = self.inovonics.event_queue.get()
				if event['uid'] in self.device_list:
					device_status = self.device_list[event['uid']]
					if ("Alarm 1" in event['status']) and not device_status['alarm1']:
						if self.alarm_needed('%s_1' % (event['uid'])):
							self.create_alarm('%s_1' % (event['uid']))
						self.db.write("INSERT INTO event (event_type_id, device_event, serial, timestamp) VALUES (1, 0, '%s_1', NOW())" % (event['uid']))
						self.db.write("UPDATE endpoint SET alarm_status = 1 WHERE serial_id = '%s_1'" % event['uid'])
						self.db.write("UPDATE alarm_device SET checkin = NOW() WHERE serial = '%s'" % event['uid'])
						device_status['alarm1'] = True
					elif ("Alarm 1" not in event['status']) and device_status['alarm1']:
						self.db.write("INSERT INTO event (event_type_id, device_event, serial, timestamp) VALUES (2, 0, '%s_1', NOW())" % (event['uid']))
						self.db.write("UPDATE endpoint SET alarm_status = 0 WHERE serial_id = '%s_1'" % event['uid'])
						self.db.write("UPDATE alarm_device SET checkin = NOW() WHERE serial = '%s'" % event['uid'])
						device_status['alarm1'] = False

					if ("Alarm 2" in event['status']) and not device_status['alarm2']:
						if self.alarm_needed('%s_2' % (event['uid'])):
							self.create_alarm('%s_2' % (event['uid']))
						self.db.write("INSERT INTO event (event_type_id, device_event, serial, timestamp) VALUES (1, 0, '%s_2', NOW())" % (event['uid']))
						self.db.write("UPDATE endpoint SET alarm_status = 1 WHERE serial_id = '%s_2'" % event['uid'])
						self.db.write("UPDATE alarm_device SET checkin = NOW() WHERE serial = '%s'" % event['uid'])
						device_status['alarm2'] = True
					elif ("Alarm 2" not in event['status']) and device_status['alarm2']:
						self.db.write("INSERT INTO event (event_type_id, device_event, serial, timestamp) VALUES (2, 0, '%s_2', NOW())" % (event['uid']))
						self.db.write("UPDATE endpoint SET alarm_status = 0 WHERE serial_id = '%s_2'" % event['uid'])
						self.db.write("UPDATE alarm_device SET checkin = NOW() WHERE serial = '%s'" % event['uid'])
						device_status['alarm2'] = False

					if ("Alarm 3" in event['status']) and not device_status['alarm3']:
						if self.alarm_needed('%s_3' % (event['uid'])):
							self.create_alarm('%s_3' % (event['uid']))
						self.db.write("INSERT INTO event (event_type_id, device_event, serial, timestamp) VALUES (1, 0, '%s_3', NOW())" % (event['uid']))
						self.db.write("UPDATE endpoint SET alarm_status = 1 WHERE serial_id = '%s_3'" % event['uid'])
						self.db.write("UPDATE alarm_device SET checkin = NOW() WHERE serial = '%s'" % event['uid'])
						device_status['alarm3'] = True
					elif ("Alarm 3" not in event['status']) and device_status['alarm3']:
						self.db.write("INSERT INTO event (event_type_id, device_event, serial, timestamp) VALUES (2, 0, '%s_3', NOW())" % (event['uid']))
						self.db.write("UPDATE endpoint SET alarm_status = 0 WHERE serial_id = '%s_3'" % event['uid'])
						self.db.write("UPDATE alarm_device SET checkin = NOW() WHERE serial = '%s'" % event['uid'])
						device_status['alarm3'] = False

					if ("Alarm 4" in event['status']) and not device_status['alarm4']:
						if self.alarm_needed('%s_4' % (event['uid'])):
							self.create_alarm('%s_4' % (event['uid']))
						self.db.write("INSERT INTO event (event_type_id, device_event, serial, timestamp) VALUES (1, 0, '%s_4', NOW())" % (event['uid']))
						self.db.write("UPDATE endpoint SET alarm_status = 1 WHERE serial_id = '%s_4'" % event['uid'])
						self.db.write("UPDATE alarm_device SET checkin = NOW() WHERE serial = '%s'" % event['uid'])
						device_status['alarm4'] = True
					elif ("Alarm 4" not in event['status']) and device_status['alarm4']:
						self.db.write("INSERT INTO event (event_type_id, device_event, serial, timestamp) VALUES (2, 0, '%s_4', NOW())" % (event['uid']))
						self.db.write("UPDATE endpoint SET alarm_status = 0 WHERE serial_id = '%s_4'" % event['uid'])
						self.db.write("UPDATE alarm_device SET checkin = NOW() WHERE serial = '%s'" % event['uid'])
						device_status['alarm4'] = False

					if ("Case and Wall Tamper" in event['status']) and not device_status['tamper']:
						self.db.write("INSERT INTO event (event_type_id, device_event, serial, timestamp) VALUES (3, 1, '%s', NOW())" % (event['uid']))
						self.db.write("UPDATE alarm_device SET tamper = 1, checkin = NOW() WHERE serial = '%s'" % event['uid'])
						device_status['tamper'] = True
					elif ("Case and Wall Tamper" not in event['status']) and device_status['tamper']:
						self.db.write("INSERT INTO event (event_type_id, device_event, serial, timestamp) VALUES (4, 1, '%s', NOW())" % (event['uid']))
						self.db.write("UPDATE alarm_device SET tamper = 0, checkin = NOW() WHERE serial = '%s'" % event['uid'])
						device_status['tamper'] = False

					if ("Low Battery" in event['status']) and not device_status['low_battery']:
						self.db.write("INSERT INTO event (event_type_id, device_event, serial, timestamp) VALUES (5, 1, '%s', NOW())" % (event['uid']))
						self.db.write("UPDATE alarm_device SET low_battery = 1, checkin = NOW() WHERE serial = '%s'" % event['uid'])
						device_status['low_battery'] = True
					elif ("Low Battery" not in event['status']) and device_status['low_battery']:
						self.db.write("INSERT INTO event (event_type_id, device_event, serial, timestamp) VALUES (6, 1, '%s', NOW())" % (event['uid']))
						self.db.write("UPDATE alarm_device SET low_battery = 0, checkin = NOW() WHERE serial = '%s'" % event['uid'])
						device_status['low_battery'] = False

					if ("No Change" in event['status']):
						self.db.write("UPDATE alarm_device SET checkin = NOW() WHERE serial = '%s'" % event['uid'])

					if ("Reset" in event['status']):
						self.db.write("INSERT INTO event (event_type_id, device_event, serial, timestamp) VALUES (7, 1, '%s', NOW())" % (event['uid']))
						self.db.write("UPDATE alarm_device SET checkin = NOW() WHERE serial = '%s'" % event['uid'])

				elif event['uid'] not in self.devices:
					if ("Reset" in event['status']):
						self.device_list[event['uid']] = {"alarm1":False, "alarm2":False, "alarm3":False, "alarm4":False, "tamper":False, "low_battery":False}
						alarm_device_id = self.db.write("INSERT INTO alarm_device (serial, pti, checkin) VALUES ('%s','%s',NOW())" % (event['uid'], event['pti']['pti']))
						for i in range(1, 5):
							self.db.write("INSERT INTO endpoint (alarm_device_id, serial_id) VALUES ('%s','%s_%s')" % (alarm_device_id, event['uid'], i))
						self.db.write("INSERT INTO event (event_type_id, device_event, serial, timestamp) VALUES (7, 1, '%s', NOW())" % (event['uid']))

			# except Exception as e:
			# 	print e

security = SecuritySystem('/dev/ttyUSB0')
security.start_system()


